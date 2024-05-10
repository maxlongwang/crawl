from requests import HTTPError
import scrapy
import json
import re

from fundinfo.items import FuturesManagerItem


class FuturesprodSpider(scrapy.Spider):
    name = "futuresmanager"
    allowed_domains = ["gs.amac.org.cn"]
    goto_url = "https://gs.amac.org.cn/amac-infodisc/res/pof/member/{}.html"
    base_url = "https://gs.amac.org.cn/amac-infodisc/api/pof/pofMember?rand=0.6132896288284786&page={}&size=20"
    start_urls = ["https://gs.amac.org.cn/amac-infodisc/api/pof/pofMember?rand=0.6132896288284786&page=0&size=20"]

    custom_settings = {'ITEM_PIPELINES': {'fundinfo.pipelines.FuturesManagerPipeline': 300},
                       }

    # postdata = {"productName": "null", "mgrName": "null", "productCode": "null", "foundDateFrom": "null", "foundDateTo": "null"}
    postdata = {}

    def start_requests(self):
        # for url in self.start_urls:
        #     yield scrapy.Request(url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'})
        for i in [161,107,52,109,78,99,185,44,41,155,56,21,90,49,213,46,112,153,139,181,83,67,69,150,123,39]:
            url=self.base_url.format(i)
            yield scrapy.Request(url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'})

    def parse(self, response):
        jsonData = json.loads(response.body)
        totalPages = jsonData.get('totalPages')
        currentPage = jsonData.get('number')

        for data in jsonData['content']:
            item = FuturesManagerItem()
            item['userTenantId'] = data.get('userTenantId')
            item['managerName'] = data.get('managerName')
            item['markStar'] = data.get('markStar')
            item['memberBehalf'] = data.get('memberBehalf')
            item['memberCode'] = data.get('memberCode')
            item['memberDate'] = data.get('memberDate')
            item['memberType'] = data.get('memberType')
            item['primaryInvestType'] = data.get('primaryInvestType')
            item['page'] = currentPage

            gotourl = self.goto_url.format(item['userTenantId'])

            yield scrapy.Request(url=gotourl, callback=self.gotourl_parse, cb_kwargs={'item': item})

        nextPage = currentPage + 1
        # if (nextPage < totalPages):
        #     next_page_url = self.base_url.format(nextPage)
        #     yield scrapy.Request(url=next_page_url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'}, callback=self.parse)

    def gotourl_parse(self, response, **kwargs):
        item = kwargs['item']
        sel = scrapy.Selector(response)
        item['managerEnglishName'] = sel.xpath('//td[contains(text(),"会员机构全称(英文)")]/following-sibling::td/text()').extract_first()
        item['organCode'] = sel.xpath('//td[contains(text(),"组织机构代码")]/following-sibling::td/text()').extract_first()
        item['establishDate'] = sel.xpath('//td[contains(text(),"成立时间")]/following-sibling::td/text()').extract_first()
        item['registerAddress'] = sel.xpath('//td[contains(text(),"注册地址")]/following-sibling::td/text()').extract_first()
        item['officeAddress'] = sel.xpath('//td[contains(text(),"办公地址")]/following-sibling::td/text()').extract_first()
        item['registerAsset'] = sel.xpath('//td[contains(text(),"注册资本")]/following-sibling::td/text()').extract_first()
        item['organType'] = sel.xpath('//td[contains(text(),"机构性质")]/following-sibling::td/text()').extract_first()
        item['businessType'] = sel.xpath('//td[contains(text(),"业务类型")]/following-sibling::td/text()').extract_first()
        if item['businessType'] is not None:
            item['businessType'] = re.sub(' +', ' ', item['businessType']).strip().replace(u'\xa0\n', u'').replace(u'\n', u'').strip()

        item['employeeNum'] = sel.xpath('//td[contains(text(),"员工人数")]/following-sibling::td/text()').extract_first()
        item['organWebAddress'] = sel.xpath('//td[contains(text(),"机构网址")]/following-sibling::td/text()').extract_first()
        if item['organWebAddress'] is not None:
            item['organWebAddress'] = item['organWebAddress'].replace(u'\n', u'').strip()

        yield item
