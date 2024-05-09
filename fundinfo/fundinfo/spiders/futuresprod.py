import scrapy
import json

from fundinfo.items import FuturesItem


class FuturesprodSpider(scrapy.Spider):
    name = "futuresprod"
    allowed_domains = ["gs.amac.org.cn"]
    base_url = "https://gs.amac.org.cn/amac-infodisc/api/pof/futures?rand=0.9075592085544137&page={}&size=20"
    start_urls = ["https://gs.amac.org.cn/amac-infodisc/api/pof/futures?rand=0.9075592085544130&page=0&size=20"]

    custom_settings = {'ITEM_PIPELINES': {'fundinfo.pipelines.FuturesPipeline': 300},
                       }

    # postdata = {"productName": "null", "mgrName": "null", "productCode": "null", "foundDateFrom": "null", "foundDateTo": "null"}
    postdata={}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'})

    def parse(self, response):
        jsonData = json.loads(response.body)
        totalPages = jsonData.get('totalPages')
        currentPage = jsonData.get('number')

        for data in jsonData['content']:
            item = FuturesItem()
            item['id'] = data.get('id')
            item['aoiName'] = data.get('aoiName')
            item['dueDate'] = data.get('dueDate')
            item['fundStatus'] = data.get('fundStatus')
            item['mpiCreateDate'] = data.get('mpiCreateDate')
            item['mpiName'] = data.get('mpiName')
            item['mpiProductCode'] = data.get('mpiProductCode')
            item['mpiTrustee'] = data.get('mpiTrustee')
            item['registeredDate'] = data.get('registeredDate')
            item['sfjgh'] = data.get('sfjgh')
            item['tzlx'] = data.get('tzlx')
            item['page'] = currentPage

            yield item

        nextPage = currentPage + 1
        if (nextPage < totalPages):
            next_page_url = self.base_url.format(nextPage)
            yield scrapy.Request(url=next_page_url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'}, callback=self.parse)
