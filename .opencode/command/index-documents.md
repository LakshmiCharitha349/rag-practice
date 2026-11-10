---
description: Index multiple documents into the ChromaDB RAG collection
---

Inspect the existing RAG implementation and extend it to support
multiple transcript files.

Requirements:
- Discover all files in data/documents/transcripts/.
- Load each document independently.
- Reuse the existing chunking implementation.
- Generate embeddings using all-MiniLM-L6-v2.
- Store chunks in the existing finance_documents collection.
- Store source filename in metadata.
- Generate globally unique chunk IDs.
- Prevent duplicate indexing.
- Support updating individual documents.
- Preserve unchanged documents.
- Update retrieval to work across all documents.
- Preserve the existing Ollama generation pipeline.
- Add tests for indexing, updates, duplicates, and retrieval.

Do not delete existing ChromaDB data.
Inspect the project first, explain your proposed changes,
and then implement and test them.