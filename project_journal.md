# Project Journal

## Day 1

### Date
18 July 2026

### Work Completed
- Created the project repository.
- Organized the project folder structure.
- Set up the Python virtual environment.
- Added sample customer support documents.
- Implemented document loading for Word documents.
- Implemented text preprocessing.
- Implemented document chunking.
- Tested the document processing pipeline successfully.

### Issues Faced
- Initially, the Word documents were not in a valid .docx format, causing errors while loading.
- Temporary Word files (~$) were also being read by the program.

### Solution
- Recreated all documents using Microsoft Word and saved them in the correct .docx format.
- Removed temporary Word files from the documents folder.
- Successfully tested document loading after fixing the files.

### Next Plan
- Generate embeddings using Sentence Transformers.
- Create a FAISS vector database.


## Day 2

### Work Completed
- Installed Sentence Transformers and FAISS.
- Generated embeddings for document chunks.
- Created a FAISS vector database.
- Implemented semantic similarity search.
- Tested document retrieval with sample queries.
- Saved the FAISS index for future use.
- Committed and pushed the changes to GitHub.

### Issues Faced
- No major issues during embedding generation and vector indexing.

### Solution
- Verified embedding dimensions and successfully tested semantic search.

### Next Plan
- Integrate LangChain with the vector database.
- Connect an LLM to build the complete RAG pipeline.