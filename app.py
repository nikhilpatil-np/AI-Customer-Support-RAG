from document_loader import DocumentLoader
from preprocessing import TextPreprocessor
from utils import TextChunker
from embeddings import EmbeddingGenerator
from rag_chatbot import VectorStore
from llm import LLMModel

# -------------------------------
# Initialize Components
# -------------------------------
loader = DocumentLoader()
preprocessor = TextPreprocessor()
chunker = TextChunker(chunk_size=300, overlap=50)
embedding_generator = EmbeddingGenerator()
vector_store = VectorStore()
llm = LLMModel()

print("\nLoading documents...")

# -------------------------------
# Load Documents
# -------------------------------
documents = loader.load_documents("data/docs")

# -------------------------------
# Preprocess Documents
# -------------------------------
cleaned_documents = preprocessor.preprocess_documents(documents)

# -------------------------------
# Create Text Chunks
# -------------------------------
chunks = chunker.create_chunks(cleaned_documents)

print(f"Total Chunks Created: {len(chunks)}")

# -------------------------------
# Generate Embeddings
# -------------------------------
embeddings = embedding_generator.generate_embeddings(chunks)

print("Embeddings Generated Successfully.")

# -------------------------------
# Create FAISS Vector Database
# -------------------------------
vector_store.create_index(embeddings)

# Save FAISS Index
vector_store.save_index("models/faiss_index.bin")

print("FAISS Index Saved Successfully.")

print("\n===================================")
print(" AI Customer Support RAG Chatbot ")
print("===================================")

# -------------------------------
# Chat Loop
# -------------------------------
while True:

    question = input("\nAsk a Question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    # Generate embedding for user query
    query_embedding = embedding_generator.model.encode(
        [question],
        convert_to_numpy=True
    )

    # Retrieve Top 3 Similar Chunks
    distances, indices = vector_store.search(
        query_embedding,
        top_k=3
    )

    # Guardrail
    if distances[0][0] > 1.0:
        print("\nI don't know based on the available documents.")
        continue

    context = ""

    print("\nRetrieved Context:\n")

    for i, index in enumerate(indices[0]):

        print(f"Chunk {i+1}:")
        print(chunks[index]["text"])
        print("-" * 50)

        context += chunks[index]["text"] + "\n"

    prompt = f"""
You are an AI Customer Support Assistant.

Answer ONLY from the given context.

If the answer is not available in the context,
reply exactly:

I don't know based on the available documents.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = llm.generate_answer(prompt)

    print("\nAI Answer:\n")
    print(answer)