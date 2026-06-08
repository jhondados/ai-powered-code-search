"""Semantic code indexer using CodeBERT embeddings."""
from transformers import AutoTokenizer, AutoModel
import torch
import ast
from pathlib import Path
from typing import List, Tuple
import numpy as np

class CodeSearchIndexer:
    MODEL = "microsoft/codebert-base"
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.MODEL)
        self.model = AutoModel.from_pretrained(self.MODEL)
        self.model.eval()
        self.index = []  # (embedding, metadata)

    def embed_code(self, code: str) -> np.ndarray:
        inputs = self.tokenizer(code, return_tensors="pt", max_length=512, truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state[:, 0, :].numpy()[0]

    def index_file(self, filepath: str):
        code = Path(filepath).read_text(errors="ignore")
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    func_code = ast.get_source_segment(code, node) or ""
                    emb = self.embed_code(func_code)
                    self.index.append((emb, {"file": filepath, "function": node.name, "line": node.lineno, "code": func_code[:200]}))
        except SyntaxError:
            pass

    def search(self, query: str, top_k: int = 10) -> List[Tuple[float, dict]]:
        query_emb = self.embed_code(query)
        scores = [(np.dot(query_emb, idx_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(idx_emb)), meta)
                  for idx_emb, meta in self.index]
        return sorted(scores, key=lambda x: x[0], reverse=True)[:top_k]
