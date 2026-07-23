# Evaluation Report

## Objective

Evaluate the AI Customer Support Assistant for response quality and retrieval accuracy.

---

## Test Cases

| Question | Result |
|-----------|---------|
| How do I reset my password? | Correct |
| What are the shipping charges? | Correct |
| How can I contact support? | Correct |
| What is the leave policy? | Correct |
| Who is the CEO of Microsoft? | I don't know |

---

## Accuracy

The chatbot successfully retrieves relevant document chunks for company-related questions and generates accurate responses.

Unknown questions outside the knowledge base return:

> I don't know based on the available documents.

This reduces hallucination.

---

## Response Time

Average Response Time:

1–3 seconds

---

## Strengths

- Accurate retrieval
- Fast responses
- Easy to use
- Local LLM
- Semantic Search

---

## Limitations

- Small knowledge base
- DOCX documents only
- No conversation memory
- Local deployment only

---

## Future Improvements

- PDF Support
- Cloud Deployment
- User Authentication
- Chat History
- Multi-language Support