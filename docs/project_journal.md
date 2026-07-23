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

### Date
20 July 2026

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

**Date:** 21 July 2026

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

# Day 4 Project Journal

## Date

22 July 2026

---

## Work Completed

- Developed the FastAPI backend for the AI Customer Support RAG Chatbot.
- Created REST API endpoints to process user questions and return AI-generated responses.
- Integrated the existing RAG pipeline with the FastAPI backend.
- Developed a Streamlit-based user interface for the chatbot.
- Connected the Streamlit frontend with the FastAPI API using HTTP requests.
- Tested the complete chatbot workflow from user input to AI-generated response.
- Verified that the chatbot correctly answered questions from the knowledge base and returned "I don't know based on the available documents." for unrelated queries.

---

## Challenges Faced

- Faced API connection issues between Streamlit and FastAPI.
- Fixed request handling and endpoint communication.
- Verified that both services were running simultaneously for successful communication.

---

## Solutions

- Corrected the API endpoint configuration.
- Successfully connected the Streamlit frontend with the FastAPI backend.
- Tested multiple customer support questions to verify accurate responses.

---

## Outcome

Successfully completed the FastAPI backend and Streamlit frontend integration. The AI Customer Support RAG Chatbot is now capable of accepting user questions through a web interface, retrieving relevant information from the knowledge base, and generating accurate responses using the integrated RAG pipeline.

# Day 5 Project Journal

## Date

23 July 2026

---

## Work Completed

- Developed FastAPI backend API.
- Connected Streamlit frontend with FastAPI.
- Added conversation logging.
- Implemented user feedback system (Helpful / Not Helpful).
- Improved chatbot response handling.
- Updated project documentation.
- Performed final testing and bug fixing.
- Prepared project for GitHub submission.

---

## Challenges Faced

- API connection issues.
- Ollama integration.
- Streamlit feedback state handling.

---

## Solutions

- Fixed FastAPI endpoint.
- Corrected Ollama response handling.
- Used Streamlit session state for feedback.

---

## Outcome

Successfully completed the AI Customer Support RAG Chatbot with FastAPI backend, Streamlit frontend, FAISS vector search, Ollama integration, conversation logging, and user feedback mechanism.