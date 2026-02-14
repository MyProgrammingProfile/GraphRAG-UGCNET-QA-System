# GraphRAG-UGCNET-QA-System

A Graph Retrieval-Augmented Generation system built for syllabus-aligned question answering in the UGC NET exam domain.

---

## 📌 Project Overview

This project implements a hybrid **Graph RAG architecture** combining:

✔ Neo4j knowledge graph  
✔ Embedding-based retrieval  
✔ Language model for answer generation

The system transforms unstructured corpus text into structured concept graphs, enabling more accurate domain-aware question answering.

---

## 🧠 Architecture

The major components of the system are:

1. **Data Ingestion**  
   Converts syllabus texts and review articles into Neo4j graph format.

2. **Graph Engine**  
   Constructs entities, relations and bridges across syllabus units.

3. **Embeddings & Retrieval**  
   Uses FAISS and embedding models for semantic similarity.

4. **Answer Generation**  
   Combines retrieval results with an LLM (e.g., OpenAI) to produce answers.

---

## 📂 Repository Structure

