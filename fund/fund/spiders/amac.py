import json
from typing import Iterable
import scrapy

from fund.items import FundNoItem


class AmacSpider(scrapy.Spider):
    name = "amac"
    allowed_domains = ["gs.amac.org.cn"]
    main_url = "https://gs.amac.org.cn/amac-infodisc/res/pof/fund/{}.html"
    base_url = "https://gs.amac.org.cn/amac-infodisc/api/pof/fund?&page={}&size=100"
    start_urls = ["https://gs.amac.org.cn/amac-infodisc/api/pof/fund?&page=0&size=100"]

    postdata = {}

    def start_requests(self):
        postdata = {}
        for url in self.start_urls:
            yield scrapy.Request(url, method='POST', body=json.dumps(postdata), headers={'Content-Type': 'application/json'})

    def parse(self, response):
        jsonData = json.loads(response.body)

        for data in jsonData['content']:
            fundnoitem = FundNoItem()
            fundnoitem['id'] = data.get('id')
            fundnoitem['fundNo'] = data.get('fundNo')
            fundnoitem['fundName'] = data.get('fundName')
            fundnoitem['managerId'] = data['managersInfo'][0].get('managerId')
            fundnoitem['managerName'] = data.get('managerName')
            fundnoitem['managerType'] = data.get('managerType')
            fundnoitem['managerUrl'] = data.get('managerUrl')
            fundnoitem['mandatorName'] = data.get('mandatorName')
            fundnoitem['establishDate'] = data.get('establishDate')
            fundnoitem['putOnRecordDate'] = data.get('putOnRecordDate')
            fundnoitem['isDeputeManage'] = data.get('isDeputeManage')
            fundnoitem['lastQuarterUpdate'] = data.get('lastQuarterUpdate')
            fundnoitem['url'] = data.get('url')
            fundnoitem['workingState'] = data.get('workingState')
            gotourl = self.main_url.format(fundnoitem['id'])
            yield scrapy.Request(url=gotourl, callback=self.gotourl_parse, cb_kwargs={'item': fundnoitem})

        totalPages = jsonData.get('totalPages')
        currentPage = jsonData.get('number')
        nextPage = currentPage + 1
        if (nextPage < totalPages):
            next_page_url = self.base_url.format(nextPage)
            yield scrapy.Request(url=next_page_url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'}, callback=self.parse)

    def gotourl_parse(self, response, **kwargs):
        fundnoitem = kwargs['item']
        sel = scrapy.Selector(response)
        fundnoitem['fundType'] = sel.xpath('//td[contains(text(),"基金类型")]/following-sibling::td/text()').extract_first()
        fundnoitem['moneyType'] = sel.xpath('//td[contains(text(),"币种")]/following-sibling::td/text()').extract_first()
        fundnoitem['lastUpDate'] = sel.xpath('//td[contains(text(),"基金信息最后更新时间")]/following-sibling::td/text()').extract_first()

        yield fundnoitem
