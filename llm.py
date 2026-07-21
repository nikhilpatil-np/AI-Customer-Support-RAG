from langchain_ollama import ChatOllama


class LLMModel:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3.2:3b",
            temperature=0.3
        )

    def generate_answer(self, prompt):

        response = self.llm.invoke(prompt)

        return response.content