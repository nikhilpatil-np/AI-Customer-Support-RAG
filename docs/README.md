# AI Customer Support Assistant (RAG Chatbot)

## Project Overview

The AI Customer Support Assistant is a Retrieval-Augmented Generation (RAG) chatbot that answers customer and employee queries using information stored in company documents.

Instead of generating answers from general knowledge, the chatbot retrieves the most relevant document chunks from a FAISS vector database and then uses a Large Language Model (LLM) running locally through Ollama to generate accurate responses.

---

## Features

- Document Loading (.docx)
- Text Preprocessing
- Text Chunking
- SentenceTransformer Embeddings
- FAISS Vector Search
- Retrieval-Augmented Generation (RAG)
- Ollama Llama 3.2 Integration
- FastAPI Backend API
- Streamlit Chat Interface
- Conversation Logging
- User Feedback (Helpful / Not Helpful)
- "I don't know" guardrail for unknown questions

---

## Technologies Used

- Python
- FastAPI
- Streamlit
- FAISS
- Sentence Transformers
- LangChain
- Ollama
- Llama 3.2
- NumPy

---

## Project Structure

```
AI-Customer-Support-RAG
│
├── api.py
├── app.py
├── streamlit_app.py
├── rag_chatbot.py
├── llm.py
├── logger.py
├── feedback.py
├── document_loader.py
├── embeddings.py
├── preprocessing.py
├── utils.py
├── requirements.txt
├── README.md
├── project_journal.md
├── data/
├── models/
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download Ollama Model

```bash
ollama pull llama3.2:3b
```

---

## Run FastAPI

```bash
uvicorn api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

## Sample Questions

- How do I reset my password?
- What are the shipping charges?
- How can I contact support?
- What is the leave policy?
- Who is the CEO of Microsoft?

---

## Future Improvements

- PDF Support
- Website Crawling
- Better Prompt Engineering
- Conversation Memory
- User Authentication
- Cloud Deployment

---

## Author

Nikhil Patil

AI/ML Engineering Intern