# GeminiLLM_DocChat

## Overview
**GeminiLLM_DocChat** is an AI-powered document chat system that extracts text from PDFs, generates vector embeddings, stores them in a vector database, and allows users to query information using natural language. It leverages **LangChain, FAIS and google's  embeddings** to provide an efficient document retrieval and question-answering system.

## Features
- 📄 Extracts text from PDFs, PPTs etc
- 🔍 Stores embeddings in a vector database (FAISS)
- 🤖 Uses AI embeddings for semantic search
- 💬 Allows users to ask natural language questions about the document
- 🚀 Fast and scalable retrieval-augmented generation (RAG)

## Tech Stack
- **Python** (Core language)
- **LangChain** (Document processing and retrieval)
- **FAISS** (Vector database)
- **google/models/text-embedding-004** (Embeddings model)
- **Docling** (PDF text extraction)
- **Streamlit** (API or UI for interaction)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SPYLoveC2/GeminiLLM_DocChat.git
   cd GeminiLLM_DocChat
   ```
2. Create a virtual environment and install dependencies:
```sh
conda env create -f environment.yml
```

## Usage
1. Start the chatbot interface:
   ```bash
   streamlit run app.py  # If using Streamlit UI
   ```
3. Ask questions about the document in the UI or API.

## Configuration
- Set your API keys (if using OpenAI embeddings) in an `.env` file:
  ```
GOOGLE_API_KEY=your_api_key
GROQ=your_api_key
  ```

## Roadmap
- ✅ Basic PDF processing & embedding storage
- ✅ Q&A system with retrieval
- 🔜 Multi-document support
- 🔜 Fine-tuned LLM integration

## Contributing
Feel free to submit issues or pull requests to improve the project.


