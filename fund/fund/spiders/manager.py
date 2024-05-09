import json
import scrapy

from fund.items import ManagerItem


class ManagerSpider(scrapy.Spider):
    name = "manager"
    allowed_domains = ["gs.amac.org.cn"]
    goto_url = "https://gs.amac.org.cn/amac-infodisc/api/pof/manager/{}.html"
    base_url = "https://gs.amac.org.cn/amac-infodisc/api/pof/fund?&page={}&size=100"
    start_urls = ["https://gs.amac.org.cn/amac-infodisc/api/pof/manager/query?&page=0&size=20"]

    postdata = {}

    def start_requests(self):
        postdata = {}
        for url in self.start_urls:
            yield scrapy.Request(url, method='POST', body=json.dumps(postdata), headers={'Content-Type': 'application/json'})

    def parse(self, response):
        jsonData = json.loads(response.body)

        for data in jsonData['content']:
            manageritem = ManagerItem()
            manageritem['id'] = data.get('id')
            manageritem['managerName'] = data.get('managerName')
            manageritem['artificialPersonName'] = data.get('artificialPersonName')
            manageritem['registerNo'] = data.get('registerNo')
            manageritem['establishDate'] = data.get('establishDate')
            manageritem['managerHasProduct'] = data.get('managerHasProduct')
            manageritem['url'] = data.get('url')
            manageritem['registerDate'] = data.get('registerDate')
            manageritem['registerAddress'] = data.get('registerAddress')
            manageritem['registerProvince'] = data.get('registerProvince')
            manageritem['registerCity'] = data.get('registerCity')
            manageritem['regAdrAgg'] = data.get('regAdrAgg')
            manageritem['officeAdrAgg'] = data.get('officeAdrAgg')
            manageritem['fundCount'] = data.get('fundCount')
            manageritem['paidInCapital'] = data.get('paidInCapital')
            manageritem['subscribedCapital'] = data.get('subscribedCapital')
            manageritem['hasSpecialTips'] = data.get('hasSpecialTips')
            manageritem['hasCreditTips'] = data.get('hasCreditTips')
            manageritem['regCoordinate'] = data.get('regCoordinate')
            manageritem['officeCoordinate'] = data.get('officeCoordinate')
            manageritem['officeAddress'] = data.get('officeAddress')
            manageritem['officeProvince'] = data.get('officeProvince')
            manageritem['officeCity'] = data.get('officeCity')
            manageritem['primaryInvestType'] = data.get('primaryInvestType')
            manageritem['fundTypeScaleMap'] = data.get('fundTypeScaleMap')
            manageritem['memberType'] = data.get('memberType')
            manageritem['orgForm'] = data.get('orgForm')

            gotourl = self.goto_url.format(manageritem['id'])
            yield scrapy.Request(url=gotourl, callback=self.gotourl_parse, cb_kwargs={'item': manageritem})

        totalPages = jsonData.get('totalPages')
        currentPage = jsonData.get('number')
        nextPage = currentPage + 1
        # if (nextPage < totalPages):
        #     next_page_url = self.base_url.format(nextPage)
        #     yield scrapy.Request(url=next_page_url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'}, callback=self.parse)

    def gotourl_parse(self, response, **kwargs):
        manageritem = kwargs['item']
        sel = scrapy.Selector(response)
        manageritem['organCode'] = sel.xpath('//td[contains(text(),"组织机构代码	")]/following-sibling::td/text()').extract_first()
        manageritem['managerEnglishName'] = sel.xpath('//td[contains(text(),"基金管理人全称(英文)")]/following-sibling::td/text()').extract_first()
        manageritem['registerAsset'] = sel.xpath('//td[contains(text(),"注册资本")]/following-sibling::td/text()').extract_first()
        manageritem['payAsset'] = sel.xpath('//td[contains(text(),"实缴资本")]/following-sibling::td/text()').extract_first()
        manageritem['registerAssetRto'] = sel.xpath('//td[contains(text(),"注册资本实缴比例")]/following-sibling::td/text()').extract_first()
        manageritem['enterpriceType'] = sel.xpath('//td[contains(text(),"企业性质")]/following-sibling::td/text()').extract_first()
        manageritem['businessType'] = sel.xpath('//td[contains(text(),"业务类型")]/following-sibling::td/text()').extract_first()
        manageritem['employeeNum'] = sel.xpath('//td[contains(text(),"全职员工人数")]/following-sibling::td/text()').extract_first()
        manageritem['practiceNum'] = sel.xpath('//td[contains(text(),"取得基金从业人数")]/following-sibling::td/text()').extract_first()
        manageritem['isInvestAdvice'] = sel.xpath('//td[contains(text(),"是否为符合提供投资建议条件的第三方机构")]/following-sibling::td/text()').extract_first()
        manageritem['manageScale'] = sel.xpath('//td[contains(text(),"管理规模区间")]/following-sibling::td/text()').extract_first()
        manageritem['lastUpDate'] = sel.xpath('//td[contains(text(),"机构信息最后更新时间")]/following-sibling::td/text()').extract_first()

        yield manageritem

