\# VDO-02 — RAG \& Vector Databases



This folder contains practical implementations covering \*\*document loading, text splitting, embeddings, vector databases, retrieval, MMR, and Retrieval-Augmented Generation (RAG)\*\*.



\---



\## 🎯 What I Learned



\- How to load documents using LangChain document loaders

\- How to work with PDF, text, and web documents

\- How to split large documents into smaller chunks

\- How `RecursiveCharacterTextSplitter` works

\- Why chunk size and chunk overlap matter

\- What embeddings are and how text is converted into vectors

\- How to generate embeddings using Hugging Face

\- How vector databases store and search embeddings

\- How to use Chroma as a vector database

\- How to retrieve relevant documents from a vector store

\- How Maximum Marginal Relevance (MMR) improves retrieval diversity

\- How to build a basic RAG pipeline

\- How to create a PDF question-answering application using Streamlit



\---



\## 🧠 Concepts Covered



\### 1. Document Loaders



Document loaders convert different types of data into LangChain `Document` objects.



Practicals include working with:



\- Text files

\- PDF files

\- Web pages



Basic flow:



```text

Source Document

&#x20;     ↓

Document Loader

&#x20;     ↓

LangChain Documents

