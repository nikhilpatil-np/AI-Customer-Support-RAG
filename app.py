from document_loader import DocumentLoader
from preprocessing import TextPreprocessor
from utils import TextChunker

loader = DocumentLoader()
preprocessor = TextPreprocessor()
chunker = TextChunker(chunk_size=300, overlap=50)

# Load documents
documents = loader.load_documents("data/docs")

# Preprocess documents
cleaned_documents = preprocessor.preprocess_documents(documents)

# Create chunks
chunks = chunker.create_chunks(cleaned_documents)

print("=" * 60)
print("Documents Processed Successfully")
print("=" * 60)

print(f"\nTotal Documents : {len(cleaned_documents)}")
print(f"Total Chunks    : {len(chunks)}")

print("\nSample Chunks")
print("-" * 60)

for i, chunk in enumerate(chunks[:5], start=1):
    print(f"\nChunk {i}")
    print(f"File : {chunk['file_name']}")
    print(chunk["text"])
    print("-" * 60)