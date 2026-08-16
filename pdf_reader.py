import fitz

pdf_path = "resume.pdf"

document = fitz.open(pdf_path)

resume_text = ""

for page in document:
    resume_text += page.get_text()

document.close()
