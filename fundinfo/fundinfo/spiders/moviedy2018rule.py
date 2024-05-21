from typing import Any
import scrapy
from fundinfo.items import FileDown
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MovieDy2018(CrawlSpider):
    name = 'moviedy2018rule'
    allowed_domains = ["dytt89.com"]
    start_urls = ["https://www.dytt89.com/"]
    custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 300},
                       }

    rules = {
        # 详情页的链接地址
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="co_content222"]//li/a',)), callback='parse_detail', follow=False),
        #下一页提取链接地址
        # Rule(LinkExtractor(restrict_xpaths=('//div[@class="co_content222"]//li/a',)), callback='parse_detail', follow=True),
    }

    def start_requests(self):
        # 指定cookies
        cookies = {
            'guardok': 'swZhPTGZg4GJ0meuCSuwXt6PVRGoCC+33bqE85YHsClgXOqhB2/cox9EeJI58Fk/5mUB+nj4MjU+wqHcg6D/4Q==',
            'Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4': '1715906919,1716164078,1716164107,1716253852',
            'Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4': '1716253852',
            'Hm_lvt_0113b461c3b631f7a568630be1134d3d': '1715906919,1716164078,1716164107,1716253852',
            'Hm_lpvt_0113b461c3b631f7a568630be1134d3d': '1716253852',
            'Hm_lvt_8e745928b4c636da693d2c43470f5413': '1715906919,1716164078,1716164107,1716253852',
            'Hm_lpvt_8e745928b4c636da693d2c43470f5413': '1716253852'}

        for url in self.start_urls:
            yield scrapy.Request(url=url, cookies=cookies)
        
        # cookies_dic={}
        # for dic in cookies:
        #     key =dic['name']
        #     value=dic['value']
        #     cookies_dic[key]=value
        # or
        # cookies_dic ={dic['name']:dic['value'] for dic in cookies}
        # yield scrapy.Request(url,cookies=cookies_dic)

    def parse_detail(self, response):
        item = FileDown()
        text = response.text
        pattern = re.compile(r'(magnet:\?[^\'\"<>]+.(mp4|mkv))')
        urls = re.findall(pattern, text)
        for url, _ in urls:
            print(url)
