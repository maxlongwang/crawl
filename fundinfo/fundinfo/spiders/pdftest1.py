import scrapy
import json

class PdfTest1(scrapy.Spider):
    name = "pdftest1"
    allowed_domains = ["yjs.gxmzu.edu.cn/"]
    # base_url = "https://gs.amac.org.cn/amac-infodisc/api/fund/account?rand=0.012785816282853357&page={}&size=20"
    # goto_url="https://gs.amac.org.cn/amac-infodisc/res/fund/account/{}.html"
    start_urls = [r"https://yjs.gxmzu.edu.cn/__local/B/9A/98/4B18B8D6FFB67CF79D810F866CA_1B75817D_255E04.pdf"]

    def parse(self, response):
        # sel = scrapy.Selector(response)
        # print('-----respones----',response.body)
        with open('tmp.pdf','wb') as pdf:
            pdf.write(response.body)
