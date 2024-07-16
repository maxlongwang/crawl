import scrapy
# import scrapy.spiderloader
from fundinfo.items import FileDown
from fundinfo.items import PPT1File

'''
js 逆向来进行爬取数据,需要解决滑块的问题
20240650 发下过验证码取消了。原来是阿里的227验证码
20240621 403

'''


class Ppt1Js(scrapy.Spider):
    name = 'pp1js'
    allowed_domains = ["1ppt.com"]
    start_urls = ["https://www.1ppt.com/xiazai/"]
    
    custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 300},
                       'FILE_STORE':'./downfile',
                       
                       }
        
    url_list = []
    def parse(self, response):
        li_list = response.xpath("//ul[@class='tplist']/li")
        for li in li_list:
            item = PPT1File()
            url_detail = li.xpath('./a/@href').get()
            url_detail = response.urljoin(url_detail)
            item['name'] = li.xpath('./h2/a/text()').get()
            item['topic'] = li.xpath('./span/a/text()').get()
            aid = url_detail.split('/')[-1].split('.')[-2]
            url_level2 = f"https://www.1ppt.com/plus/download.php?open=0&aid={aid}&cid=3"
            # print(url_level2)
            yield scrapy.Request(url=url_level2, callback=self.detail_parse, cb_kwargs={'item': item})
        
        item2=FileDown()
        item2['file_urls'] = self.url_list
        yield item2
        
        

    def detail_parse(self, response, **kwargs):
        
        item = kwargs['item']
        down_url=response.xpath("//ul[@class='downloadlist']/li[@class='c1']/a/@href/text()").get()
        print(response.content.decode('utf-8'))
        # print(item,down_url)
        # self.url_list.append(down_url)
        # print (self.url_list)
        # yield item
        
