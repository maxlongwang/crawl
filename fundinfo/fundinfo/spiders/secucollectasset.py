import scrapy
import json

from fundinfo.items import SecuCollectAssetItem


class SecuCollectAssetSpider(scrapy.Spider):
    name = "secucollectasset"
    allowed_domains = ["gs.amac.org.cn"]
    base_url = "https://gs.amac.org.cn/amac-infodisc/api/pof/securities?rand=0.9394901403643676&page={}&size=20"
    # goto_url="https://gs.amac.org.cn/amac-infodisc/res/fund/account/{}.html"
    start_urls = ["https://gs.amac.org.cn/amac-infodisc/api/pof/securities?rand=0.9394901403643676&page=1&size=20"]

    custom_settings = {'ITEM_PIPELINES': {'fundinfo.pipelines.SecuCollectAssetPipeline': 300},
                       }

    # postdata = {"productName":,"mgrName":null,"productCode":null}
    postdata={}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'})
        # for i in [1738]:
        #     url=self.base_url.format(i)
        #     yield scrapy.Request(url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'})

    def parse(self, response):
        jsonData = json.loads(response.body)
        totalPages = jsonData.get('totalPages')
        currentPage = jsonData.get('number')

        for data in jsonData['content']:
            item = SecuCollectAssetItem()
            item['id'] = data.get('id')
            item['cpbm'] = data.get('cpbm')
            item['cpmc'] = data.get('cpmc')
            item['gljg'] = data.get('gljg')
            item['slrq'] = data.get('slrq')
            item['barq'] = data.get('barq')
            item['dqr'] = data.get('dqr')
            item['sffj'] = data.get('sffj')
            item['tgjg'] = data.get('tgjg')
            item['tzlx'] = data.get('tzlx')
            item['yzzt'] = data.get('yzzt')
            item['page'] = currentPage
            yield item
        
        nextPage = currentPage + 1
        if (nextPage < totalPages):
            next_page_url = self.base_url.format(nextPage)
            yield scrapy.Request(url=next_page_url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'}, callback=self.parse)






       
