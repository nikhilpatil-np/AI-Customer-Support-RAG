from docx import Document

doc = Document("data/docs/company_faq.docx")

print("Document opened successfully!")
print(len(doc.paragraphs))