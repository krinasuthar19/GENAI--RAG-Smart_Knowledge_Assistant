# Smart RAG Knowledge Assistant

## Overview

Smart RAG Knowledge Assistant is a Generative AI application that enables users to upload PDF documents and interact with them through a conversational chatbot. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate context-aware responses.

## Features

* Upload PDF documents
* Automatically create a knowledge base from uploaded PDFs
* Intelligent document retrieval using ChromaDB
* Ask questions based on document content
* Interactive chatbot interface built with Streamlit
* Context-aware responses using Mistral AI
* Semantic search using embeddings

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Framework

* LangChain

### Language Model

* Mistral AI

### Embedding Model

* Mistral Embeddings

### Vector Database

* ChromaDB

### Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

## Project Structure

```text
RAG/
│
├── app.py
├── main.py
├── create_db.py
├── .env (API)
├── requirements.txt
│
├── chroma-db/
```

## Workflow

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the document into smaller chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in ChromaDB.
6. Retrieve relevant chunks based on user queries.
7. Generate responses using Mistral AI.

## Installation

### Create virtual environment

```bash
uv venv
```

### Activate environment

```bash
.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
uv pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

## Future Improvements

* Multiple PDF support
* User authentication
* Chat history export
* Database management
* PDF summaries
* Dark and light themes

## Author

Krina Suthar
