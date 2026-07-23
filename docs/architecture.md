# AI Customer Support Assistant Architecture

## Architecture Flow

```text
              User
                │
                ▼
        Streamlit Web UI
                │
                ▼
          FastAPI Backend
                │
                ▼
        User Question
                │
                ▼
      Sentence Transformer
        (Embedding Model)
                │
                ▼
        FAISS Vector Search
                │
                ▼
     Top Relevant Chunks
                │
                ▼
     Ollama (Llama 3.2)
                │
                ▼
      Generated Response
                │
                ▼
          Streamlit UI
```

## Components

### Document Loader

Loads company documents.

### Preprocessing

Cleans text and removes unnecessary characters.

### Chunking

Splits long documents into smaller chunks.

### Embedding Generator

Converts text into vectors.

### FAISS

Stores embeddings and performs similarity search.

### Ollama

Generates responses using retrieved context.

### FastAPI

Provides REST API.

### Streamlit

Provides user-friendly chat interface.

### Logger

Stores conversations.

### Feedback

Stores user feedback.