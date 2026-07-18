class TextChunker:

    def __init__(self, chunk_size=300, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def create_chunks(self, documents):

        chunks = []

        for document in documents:

            text = document["content"]

            start = 0

            while start < len(text):

                end = start + self.chunk_size

                chunk = text[start:end]

                chunks.append({
                    "file_name": document["file_name"],
                    "text": chunk
                })

                start += self.chunk_size - self.overlap

        return chunks