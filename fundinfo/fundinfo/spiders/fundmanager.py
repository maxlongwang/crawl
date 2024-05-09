import json
import re
import scrapy

from fundinfo.items import FundManagerItem


class FundManagerSpider(scrapy.Spider):
    name = "fundmanager"
    allowed_domains = ["gs.amac.org.cn"]
    goto_url = "https://gs.amac.org.cn/amac-infodisc/res/pof/manager/{}.html"
    base_url = "https://gs.amac.org.cn/amac-infodisc/api/pof/manager/query?&page={}&size=20"
    start_urls = ["https://gs.amac.org.cn/amac-infodisc/api/pof/manager/query?&page=0&size=20"]

    custom_settings = {'ITEM_PIPELINES': {'fundinfo.pipelines.FundManagerPipeline': 300},
                       }

    postdata = {"regiProvinceFsc": "province", "offiProvinceFsc": "province", "establishDate": {
        "from": "1900-01-01", "to": "9999-01-01"}, "registerDate": {"from": "1900-01-01", "to": "9999-01-01"}}

    def start_requests(self):
        # relist=[564]
        # for i in relist:
        #     url=self.base_url.format(i)
        #     yield scrapy.Request(url, method='POST', body=json.dumps(postdata), headers={'Content-Type': 'application/json'})
        for url in self.start_urls:
            yield scrapy.Request(url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'})

    def parse(self, response):
        jsonData = json.loads(response.body)
        totalPages = jsonData.get('totalPages')
        currentPage = jsonData.get('number')

        for data in jsonData['content']:
            manageritem = FundManagerItem()
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
            manageritem['page'] = currentPage

            gotourl = self.goto_url.format(manageritem['id'])
            yield scrapy.Request(url=gotourl, callback=self.gotourl_parse, cb_kwargs={'item': manageritem})

        nextPage = currentPage + 1
        # if (nextPage < totalPages):
        #     next_page_url = self.base_url.format(nextPage)
        #     yield scrapy.Request(url=next_page_url, method='POST', body=json.dumps(self.postdata), headers={'Content-Type': 'application/json'}, callback=self.parse)

    def gotourl_parse(self, response, **kwargs):
        manageritem = kwargs['item']
        sel = scrapy.Selector(response)
        manageritem['organCode'] = sel.xpath('//td[contains(text(),"组织机构代码")]/following-sibling::td/text()').extract_first()
        manageritem['managerEnglishName'] = sel.xpath('//td[contains(text(),"基金管理人全称(英文)")]/following-sibling::td/text()').extract_first()
        manageritem['registerAsset'] = sel.xpath('//td[contains(text(),"注册资本")]/following-sibling::td/text()').extract_first()
        manageritem['payAsset'] = sel.xpath('//td[contains(text(),"实缴资本")]/following-sibling::td/text()').extract_first()
        manageritem['registerAssetRto'] = sel.xpath('//td[contains(text(),"注册资本实缴比例")]/following-sibling::td/text()').extract_first().strip()
        manageritem['enterpriceType'] = sel.xpath('//td[contains(text(),"企业性质")]/following-sibling::td/text()').extract_first()
        manageritem['businessType'] = re.sub(
            ' +', ' ', sel.xpath('//td[contains(text(),"业务类型")]/following-sibling::td/text()').extract_first().strip().replace(u'\xa0\n', u''))
        manageritem['employeeNum'] = sel.xpath('//td/div[contains(text(),"全职员工人数")]/../following-sibling::td/text()').extract_first()
        manageritem['practiceNum'] = sel.xpath('//td/div[contains(text(),"取得基金从业人数")]/../following-sibling::td/text()').extract_first()
        manageritem['isInvestAdvice'] = sel.xpath('//td[contains(text(),"是否为符合提供投资建议条件的第三方机构")]/following-sibling::td/text()').extract_first()
        manageritem['manageScale'] = sel.xpath('//td[contains(text(),"管理规模区间")]/following-sibling::td/text()').extract_first().strip()
        manageritem['lastUpDate'] = sel.xpath('//td[contains(text(),"机构信息最后更新时间")]/following-sibling::td/text()').extract_first()

        yield manageritem
