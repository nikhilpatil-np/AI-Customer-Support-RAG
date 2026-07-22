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


# Project Journal

## Day 3 – RAG Pipeline Integration with Ollama

**Date:** 22 July 2026

### Objective
Integrate the Retrieval-Augmented Generation (RAG) pipeline with a local LLM and enable question answering using the knowledge base.

### Work Completed
- Integrated Ollama (Llama 3.2) as the local Large Language Model.
- Connected the FAISS vector database with the RAG pipeline.
- Generated embeddings for all document chunks using Sentence Transformers.
- Retrieved the most relevant document chunks using semantic search.
- Created prompts by combining the retrieved context with the user's question.
- Implemented guardrails to return **"I don't know based on the available documents."** when no relevant information was found.
- Tested the chatbot with multiple questions from the knowledge base.
- Saved the FAISS index for future use.
- Created the `day-3-rag-pipeline` Git branch, committed the completed work, pushed it to GitHub, and merged it into the `main` branch.

### Files Worked On
- app.py
- llm.py
- rag_chatbot.py

### Testing Performed
- Verified password reset queries.
- Verified shipping-related queries.
- Tested unknown questions to confirm guardrail behavior.
- Confirmed the chatbot retrieved relevant document chunks before generating answers.

### Challenges Faced
- Encountered issues while integrating the Gemini API because of API quota and model availability restrictions.
- GitHub push was initially blocked because the `.env` file containing an API key had been committed.

### Resolution
- Switched from the Gemini API to Ollama with the Llama 3.2 local model.
- Removed the `.env` file from Git tracking and updated the repository before pushing.
- Successfully pushed the Day 3 branch and merged it into the `main` branch.

### Outcome
Successfully completed the RAG pipeline with local LLM integration. The chatbot now retrieves relevant information from the knowledge base and generates context-aware responses while avoiding unsupported answers.