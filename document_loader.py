import os
from pypdf import PdfReader
from docx import Document


class DocumentLoader:

    def load_pdf(self, file_path):
        text = ""
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text


    def load_docx(self, file_path):
        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text


    def load_txt(self, file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()


    def load_documents(self, folder_path):

        documents = []

        for file_name in os.listdir(folder_path):

            file_path = os.path.join(folder_path, file_name)

            if file_name.endswith(".pdf"):
                content = self.load_pdf(file_path)

            elif file_name.endswith(".docx"):
                content = self.load_docx(file_path)

            elif file_name.endswith(".txt"):
                content = self.load_txt(file_path)

            else:
                continue

            documents.append(
                {
                    "file_name": file_name,
                    "content": content
                }
            )

        return documents