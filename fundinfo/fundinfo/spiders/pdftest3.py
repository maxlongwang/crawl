import scrapy
import json

"""
发现下载不下来，待处理
"""

class PdfTest1(scrapy.Spider):
    name = "pdftest3"
    allowed_domains = ["yjs.gxmzu.edu.cn/"]
    file_urls=['https://yjs.gxmzu.edu.cn/__local/B/9A/98/4B18B8D6FFB67CF79D810F866CA_1B75817D_255E04.pdf']

    custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 300},
                    }

    # def file_parse(self, response):
    #     with open('tmp3.pdf','wb') as pdf:
    #         pdf.write(response.body)
