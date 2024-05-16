# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FundinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FundProdItem(scrapy.Item):
    id = scrapy.Field()
    fundNo = scrapy.Field()  # 基金代码
    fundName = scrapy.Field()  # 基金名称
    managerId = scrapy.Field()  # 基金管理人id
    managerName = scrapy.Field()  # 基金管理人名称
    managerType = scrapy.Field()  # 管理类型
    managerUrl = scrapy.Field()  # 跳转管理url
    mandatorName = scrapy.Field()  # 托管人名称
    establishDate = scrapy.Field()  # 成立时间
    putOnRecordDate = scrapy.Field()  # 备案时间
    isDeputeManage = scrapy.Field()
    lastQuarterUpdate = scrapy.Field()
    url = scrapy.Field()  # 基金跳转url
    workingState = scrapy.Field()  # 运作状态
    fundType = scrapy.Field()  # 基金类型
    moneyType = scrapy.Field()  # 币种类型
    lastUpDate = scrapy.Field()  # 基金信息最后更新时间
    page = scrapy.Field()


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
    subscribedCapital = scrapy.Field()
    page = scrapy.Field()  # 当前页


class FuturesItem(scrapy.Item):
    id = scrapy.Field()
    aoiName = scrapy.Field()  # 管理人名称
    dueDate = scrapy.Field()  # 到期日
    fundStatus = scrapy.Field()  # 运作状态
    mpiCreateDate = scrapy.Field()  # 成立日期
    mpiName = scrapy.Field()  # 产品名称
    mpiProductCode = scrapy.Field()  # 产品编码
    mpiTrustee = scrapy.Field()  # 托管人名称
    registeredDate = scrapy.Field()  # 备案日期
    sfjgh = scrapy.Field()  # 是否分级
    tzlx = scrapy.Field()  # 投资类型
    page = scrapy.Field()


class FuturesManagerItem(scrapy.Item):
    userTenantId = scrapy.Field()
    managerName = scrapy.Field()  # 机构（会员）名称
    markStar = scrapy.Field()  # 是否标星
    memberBehalf = scrapy.Field()  # 会员代表
    memberCode = scrapy.Field()  # 会员编号
    memberDate = scrapy.Field()  # 入会时间
    memberType = scrapy.Field()  # 会员类型
    primaryInvestType = scrapy.Field()  # 机构类型
    page = scrapy.Field()

    managerEnglishName = scrapy.Field()  # 机构（会员）名称 英文
    organCode = scrapy.Field()  # 组织机构代码
    establishDate = scrapy.Field()  # 成立时间
    registerAddress = scrapy.Field()  # 注册地址
    officeAddress = scrapy.Field()  # 办公地址
    registerAsset = scrapy.Field()  # 注册资本(万元)(人民币)
    organType = scrapy.Field()  # 机构性质
    businessType = scrapy.Field()  # 业务类型
    employeeNum = scrapy.Field()  # 企业人数
    organWebAddress = scrapy.Field()  # 机构网址


class CollectAssetItem(scrapy.Item):
    id = scrapy.Field()
    registerCode = scrapy.Field()  # 产品编码
    name = scrapy.Field()  # 产品名称
    manager = scrapy.Field()  # 管理人名称
    registerDate = scrapy.Field()  # 成立日期
    bailor = scrapy.Field()
    hasClassify = scrapy.Field()
    page = scrapy.Field()
    mandatorName = scrapy.Field()  # 托管人名称
    putOnRecordDate = scrapy.Field()  # 备案时间
    dueDate = scrapy.Field()  # 到期日
    tzlx = scrapy.Field()  # 投资类型
    sfjgh = scrapy.Field()  # 是否分级
    workingState = scrapy.Field()  # 运作状态


class SecuCollectAssetItem(scrapy.Item):
    id = scrapy.Field()
    cpbm = scrapy.Field() #产品编码	
    cpmc = scrapy.Field() #产品名称	
    gljg = scrapy.Field() # 管理人名称	
    slrq = scrapy.Field() # 成立日期
    barq = scrapy.Field() #备案日期	
    dqr = scrapy.Field() # 到期日	
    sffj = scrapy.Field() #是否分级	
    tgjg = scrapy.Field() #托管人名称	
    tzlx = scrapy.Field() #投资类型	
    yzzt = scrapy.Field() #运作状态	
    page=scrapy.Field()


class ImageChinazItem(scrapy.Item):
    image_urls=scrapy.Field()
    images=scrapy.Field()