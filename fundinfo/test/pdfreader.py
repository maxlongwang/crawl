from PyPDF2 import PdfReader


filepath = r'd:\tmp\1122.pdf'
reader = PdfReader(filepath)
pages = len(reader.pages)

for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text()
    print(text)
