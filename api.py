from fastapi import FastAPI
from pydantic import BaseModel
from logger import log_chat
from document_loader import DocumentLoader
from preprocessing import TextPreprocessor
from utils import TextChunker
from embeddings import EmbeddingGenerator
from rag_chatbot import VectorStore
from llm import LLMModel

app = FastAPI(title="AI Customer Support RAG API")


class Question(BaseModel):
    question: str


print("Loading RAG pipeline...")

loader = DocumentLoader()
preprocessor = TextPreprocessor()
chunker = TextChunker(chunk_size=300, overlap=50)
embedding_generator = EmbeddingGenerator()
vector_store = VectorStore()
llm = LLMModel()

documents = loader.load_documents("data/docs")
cleaned_documents = preprocessor.preprocess_documents(documents)
chunks = chunker.create_chunks(cleaned_documents)

embeddings = embedding_generator.generate_embeddings(chunks)

vector_store.create_index(embeddings)

print("API Ready!")


@app.get("/")
def home():
    return {"message": "AI Customer Support RAG API is running."}


@app.post("/chat")
def chat(request: Question):

    query_embedding = embedding_generator.model.encode(
        [request.question],
        convert_to_numpy=True
    )

    distances, indices = vector_store.search(query_embedding, top_k=3)

    context = ""

    for index in indices[0]:
        context += chunks[index]["text"] + "\n"

    if context.strip() == "":
        return {
            "answer": "I don't know based on the available documents."
        }

    prompt = f"""
Answer only from the context below.

Context:
{context}

Question:
{request.question}

Answer:
"""

    answer = llm.generate_answer(prompt)
    log_chat(request.question, answer)

    return {
        "question": request.question,
        "answer": answer
    }