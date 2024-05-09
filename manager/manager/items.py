# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.item


class FundManagerItem(scrapy.Item):
    id = scrapy.Field()
    artificialPersonName = scrapy.Field()  # 实际控制人姓名
    establishDate = scrapy.Field()  # 成立时间
    fundCount = scrapy.Field()  # 在管基金数量
    fundTypeScaleMap = scrapy.Field()
    hasCreditTips = scrapy.Field()  # 是否有诚信信息
    hasSpecialTips = scrapy.Field()  # 是否有提示信息
    managerHasProduct = scrapy.Field()
    managerName = scrapy.Field()  # 基金管理人名称
    managerEnglishName = scrapy.Field()  # 基金管理人英文名称
    memberType = scrapy.Field()  # 会员类型
    officeAddress = scrapy.Field()  # 办公地址
    officeAdrAgg = scrapy.Field()
    officeCity = scrapy.Field()
    officeCoordinate = scrapy.Field()
    officeProvince = scrapy.Field()
    orgForm = scrapy.Field()
    paidInCapital = scrapy.Field()
    primaryInvestType = scrapy.Field()  # 机构类型
    regAdrAgg = scrapy.Field()
    regCoordinate = scrapy.Field()
    registerAddress = scrapy.Field()  # 注册地址
    registerCity = scrapy.Field()  # 登记城市
    registerDate = scrapy.Field()  # 登记日期
    registerNo = scrapy.Field()  # 登记编号
    registerProvince = scrapy.Field()  # 登记省
    url = scrapy.Field()
    organCode = scrapy.Field()  # 组织机构代码
    registerAsset = scrapy.Field()  # 注册资本
    payAsset = scrapy.Field()  # 实缴资本
    registerAssetRto = scrapy.Field()  # 注册资本比例
    enterpriceType = scrapy.Field()  # 企业性质
    businessType = scrapy.Field()  # 业务类型
    employeeNum = scrapy.Field()  # 企业人数
    practiceNum = scrapy.Field()  # 从业人数
    isInvestAdvice = scrapy.Field()  # 是否为符合提供投资建议条件的第三方机构
    manageScale = scrapy.Field()  # 管理规模区间
    lastUpDate = scrapy.Field()  # 机构信息最后更新时间
    subscribedCapital=scrapy.Field() 
    page=scrapy.Field() # 当前页
