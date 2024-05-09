import scrapy
import json

class CollectAssetSpider(scrapy.Spider):
    name = "pdftest1"
    allowed_domains = ["https://yjs.gxmzu.edu.cn/"]
    # base_url = "https://gs.amac.org.cn/amac-infodisc/api/fund/account?rand=0.012785816282853357&page={}&size=20"
    # goto_url="https://gs.amac.org.cn/amac-infodisc/res/fund/account/{}.html"
    start_urls = ["https://yjs.gxmzu.edu.cn/system/resource/pdfjs/viewer.html?file=%2F__local%2FB%2F9A%2F98%2F4B18B8D6FFB67CF79D810F866CA_1B75817D_255E04.pdf"]

    custom_settings = {'ITEM_PIPELINES': {'fundinfo.pipelines.CollectAssetPipeline': 300},
                       }
    def parse(self, response):
        sel = scrapy.Selector(response)
        item_list=sel.xpath('//div[@data-page-number="1"]//span/text()').getall
        for col in item_list:
            for i in range(12):
                print(col)

