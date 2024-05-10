
import requests

pdf_url = 'https://yjs.gxmzu.edu.cn/__local/B/9A/98/4B18B8D6FFB67CF79D810F866CA_1B75817D_255E04.pdf'

response = requests.get(pdf_url, stream=True)

with open('large_file.pdf', 'wb') as pdf:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)
