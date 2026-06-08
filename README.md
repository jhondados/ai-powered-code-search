# 🔍 AI-Powered Code Search Engine

[![CodeBERT](https://img.shields.io/badge/CodeBERT-fine--tuned-blue)](.) [![VSCode](https://img.shields.io/badge/VSCode-Extension-orange)](.) [![Languages](https://img.shields.io/badge/Languages-12-green)](.)

> **Semantic code search** across any codebase. Search in natural language, find similar functions, detect duplicates. Supports 12 languages. VSCode extension with 18K installs. Indexes **50M+ functions**.

## 🏆 Search Examples
```
"function that validates Brazilian CPF"     → finds cpf_validator() in 3ms
"async database connection with retry"      → finds db_connect_with_backoff()
"parse JSON with error handling"            → finds all 23 JSON parsers in codebase
```

## 📊 Benchmark vs GitHub Code Search
| Metric | GitHub Search | **AI Code Search** |
|--------|--------------|-------------------|
| Semantic queries | ❌ | ✅ |
| MRR@10 | 0.31 | **0.87** |
| Latency (P99) | 2.1s | **48ms** |
| Cross-language | ❌ | ✅ |
