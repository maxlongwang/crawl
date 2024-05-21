from typing import Any
import scrapy
from fundinfo.items import FileDown
import re


class MovieDy2018(scrapy.Spider):
    name = 'moviedy2018'
    allowed_domains = ["dytt89.com"]
    start_urls = ["https://www.dytt89.com/"]
    custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 300},
                       }

    def start_requests(self):
        # 指定cookies
        cookies = {
            'guardok': 'u7BDgtDxvPAsRBUl6YIK9SvzVpqvzcAG4Pk8KmAqPGqwXascqtm99hwWw8CEo9SOq7VDflijXEsNWy1OayHhHw==',
            'Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4': '1715906919,1716164078,1716164107',
            'Hm_lvt_8e745928b4c636da693d2c43470f5413': '1715906919,1716164078,1716164107',
            'Hm_lvt_0113b461c3b631f7a568630be1134d3d': '1715906919,1716164078,1716164107',
            'Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4': '1716167422',
            'Hm_lpvt_0113b461c3b631f7a568630be1134d3d': '1716167422',
            'Hm_lpvt_8e745928b4c636da693d2c43470f5413': '1716167422'}

        for url in self.start_urls:
            yield scrapy.Request(url=url, cookies=cookies)

    def parse(self, response):
        url1_list = response.xpath('//div[@class="co_content222"]//li/a/@href').getall()
        # print('url1_list:-----', url1_list)
        for url in url1_list:
            goto_url = response.urljoin(url)
            # print(goto_url)
            yield scrapy.Request(url=goto_url, callback=self.parse_detail)
        
    # def parse(self, response):
    #     le=LinkExtractor(restrict_xpaths=('//div[@class="co_content222"]//li/a',))
    #     links=le.extract_links(response)
    #     for link in links:
    #         yield scrapy.Request(url=link.url,callback=self.parse_detail)

    def parse_detail(self, response):
        item = FileDown()
        # url_download = response.xpath('//div[@id="downlist"]//a/text()').get()
        text = response.text
        pattern = re.compile(r'(magnet:\?[^\'\"<>]+.(mp4|mkv))')
        urls = re.findall(pattern, text)
        for url, _ in urls:
            print(url)

            # item['file_urls'] = url
            # yield item
