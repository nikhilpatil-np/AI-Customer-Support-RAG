from document_loader import DocumentLoader
from preprocessing import TextPreprocessor
from utils import TextChunker
from embeddings import EmbeddingGenerator
from rag_chatbot import VectorStore

# Initialize
loader = DocumentLoader()
preprocessor = TextPreprocessor()
chunker = TextChunker(chunk_size=300, overlap=50)
embedding_generator = EmbeddingGenerator()
vector_store = VectorStore()

# Load documents
documents = loader.load_documents("data/docs")

# Preprocess
cleaned_documents = preprocessor.preprocess_documents(documents)

# Create chunks
chunks = chunker.create_chunks(cleaned_documents)

# Generate embeddings
embeddings = embedding_generator.generate_embeddings(chunks)

# Create FAISS index
vector_store.create_index(embeddings)

# Save index
vector_store.save_index("models/faiss_index.bin")

# Load index
vector_store.load_index("models/faiss_index.bin")

print("\n")
print("=" * 60)
print("Semantic Search Test")
print("=" * 60)

query = input("Enter your question: ")

query_embedding = embedding_generator.model.encode(
    [query],
    convert_to_numpy=True
)

distances, indices = vector_store.search(query_embedding, top_k=3)

print("\nTop Matching Chunks")
print("-" * 60)

for rank, index in enumerate(indices[0], start=1):

    print(f"\nResult {rank}")
    print(f"File : {chunks[index]['file_name']}")
    print(chunks[index]["text"])
    print("-" * 60)