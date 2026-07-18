import re


class TextPreprocessor:

    def clean_text(self, text):

        text = text.lower()

        text = re.sub(r"\n+", " ", text)

        text = re.sub(r"\s+", " ", text)

        text = re.sub(r"[^a-zA-Z0-9.,?! ]", "", text)

        return text.strip()


    def preprocess_documents(self, documents):

        cleaned_documents = []

        for document in documents:

            cleaned_text = self.clean_text(document["content"])

            cleaned_documents.append(
                {
                    "file_name": document["file_name"],
                    "content": cleaned_text
                }
            )

        return cleaned_documents