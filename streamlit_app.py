import streamlit as st
import requests
from feedback import save_feedback

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Customer Support Assistant")
st.write("Ask questions from the company knowledge base.")

# Store question and answer
if "question" not in st.session_state:
    st.session_state.question = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question.strip():

        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"question": question}
            )

            st.session_state.question = question
            st.session_state.answer = response.json()["answer"]

        except Exception:
            st.error("Unable to connect to the API.")

# Display answer
if st.session_state.answer:

    st.success(st.session_state.answer)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Helpful"):
            save_feedback(
                st.session_state.question,
                st.session_state.answer,
                "Helpful"
            )
            st.success("Thank you for your feedback!")

    with col2:
        if st.button("👎 Not Helpful"):
            save_feedback(
                st.session_state.question,
                st.session_state.answer,
                "Not Helpful"
            )
            st.success("Thank you for your feedback!")