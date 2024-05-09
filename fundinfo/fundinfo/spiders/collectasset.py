import scrapy
import json

from fundinfo.items import CollectAssetItem


class CollectAssetSpider(scrapy.Spider):
    name = "collectasset"
    allowed_domains = ["gs.amac.org.cn"]
    base_url = "https://gs.amac.org.cn/amac-infodisc/api/fund/account?rand=0.012785816282853357&page={}&size=20"
    goto_url="https://gs.amac.org.cn/amac-infodisc/res/fund/account/{}.html"
    start_urls = ["https://gs.amac.org.cn/amac-infodisc/api/fund/account?rand=0.012785816282853357&page=0&size=20"]

    custom_settings = {'ITEM_PIPELINES': {'fundinfo.pipelines.CollectAssetPipeline': 300},
                       }

    # postdata = {"productName":,"mgrName":null,"productCode":null}
    postdata={}

    def start_requests(self):
        # for url in self.start_urls:
        #     yield scrapy.Request(url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'})
        for i in [1738]:
            url=self.base_url.format(i)
            yield scrapy.Request(url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'})

    def parse(self, response):
        jsonData = json.loads(response.body)
        totalPages = jsonData.get('totalPages')
        currentPage = jsonData.get('number')

        for data in jsonData['content']:
            item = CollectAssetItem()
            item['id'] = data.get('id')
            item['registerCode'] = data.get('registerCode')
            item['name'] = data.get('name')
            item['manager'] = data.get('manager')
            item['registerDate'] = data.get('registerDate')
            item['bailor'] = data.get('bailor')
            item['hasClassify'] = data.get('hasClassify')
            item['page'] = currentPage

            gotourl = self.goto_url.format(item['id'])
            yield scrapy.Request(url=gotourl, callback=self.gotourl_parse, cb_kwargs={'item': item})

        nextPage = currentPage + 1
        # if (nextPage < totalPages):
        #     next_page_url = self.base_url.format(nextPage)
        #     yield scrapy.Request(url=next_page_url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'}, callback=self.parse)


    def gotourl_parse(self, response, **kwargs):
        item = kwargs['item']
        sel = scrapy.Selector(response)
        item['mandatorName'] = sel.xpath('//td[contains(text(),"托管人名称")]/following-sibling::td/text()').extract_first()
        item['putOnRecordDate'] = sel.xpath('//td[contains(text(),"备案时间")]/following-sibling::td/text()').extract_first()
        item['dueDate'] = sel.xpath('//td[contains(text(),"到期日")]/following-sibling::td/text()').extract_first()
        item['tzlx'] = sel.xpath('//td[contains(text(),"投资类型")]/following-sibling::td/text()').extract_first()
        item['sfjgh'] = sel.xpath('//td[contains(text(),"是否分级")]/following-sibling::td/text()').extract_first()
        item['workingState'] = sel.xpath('//td[contains(text(),"运作状态")]/following-sibling::td/text()').extract_first()

        yield item
