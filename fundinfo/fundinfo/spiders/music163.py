from typing import Any
import scrapy
from fundinfo.items import FileDown
import re


class Music163(scrapy.Spider):
    name = 'music163'
    # allowed_domains = ["music.163.com"]
    start_urls = ["https://m801.music.126.net/20240523150900/105b8795dafc6b03a366e348a2de38b6/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/36145021310/4f58/47c3/4fe5/7b70c6659e872d3dd183187f37f881d2.m4a"]
    # custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 300},
    #                    }
    
    def parse(self, response):
        # sel = scrapy.Selector(response)
        # print('-----respones----',response.body)
        with open('test.mp3','wb') as pdf:
            pdf.write(response.body)




