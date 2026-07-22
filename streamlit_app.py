import streamlit as st
import requests

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Customer Support Assistant")

st.write("Ask questions from the company knowledge base.")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question.strip():

        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"question": question}
            )

            answer = response.json()["answer"]

            st.success(answer)

        except Exception:
            st.error("Unable to connect to the API.")