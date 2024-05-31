from typing import Any
import scrapy
from fundinfo.items import FileDown
import re

'''
使用文件下载测试
采用selenium

'''

class Music163(scrapy.Spider):
    name = 'ppt1'
    # allowed_domains = ["1ppt.com"]
    start_urls = ["https://www.1ppt.com/xiazai/"]
    custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 300},
                       }
    
    def parse(self, response):
        pass
