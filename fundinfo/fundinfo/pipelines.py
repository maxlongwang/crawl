# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import cx_Oracle
import datetime
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ImagsChianzPipeLine(ImagesPipeline):
    def get_media_request(self,item,info):
        yield scrapy.Request(item['src'])

    def file_path(self,request,respone=None,info=None, *, item=None):
        imgName=request.url.split('/')[-1]
        return imgName
    
    def item_completed(self, results, item, info):
        return item
    


class FundinfoPipeline:
    def process_item(self, item, spider):
        return item


def _getconnect():
    conn=cx_Oracle.connect('reader', 'reader', '192.168.144.66/eif')
    return conn

class SecuCollectAssetPipeline:
    def __init__(self):
        self.conn = _getconnect()
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        self.conn.commit()
        if len(self.data) > 0:
            self._write_to_db()

        self.conn.close()

    def process_item(self, item, spider):
        page_data = tuple(dict(item).values())
        self.data.append(page_data)

        if len(self.data) == 20:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_secucollectAssetno(id, cpbm, cpmc, gljg, slrq, barq, dqr, sffj, tgjg, tzlx, yzzt, page) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)', self.data)
        self.conn.commit()



class CollectAssetPipeline:
    def __init__(self):
        self.conn = _getconnect()
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        self.conn.commit()
        if len(self.data) > 0:
            self._write_to_db()

        self.conn.close()

    def process_item(self, item, spider):
        page_data = tuple(dict(item).values())
        self.data.append(page_data)

        if len(self.data) == 20:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_collectAssetno(id,registercode,name,manager,registerdate,bailor,hasclassify,page,mandatorname,putonrecorddate,duedate,tzlx,sfjgh,workingstate) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)', self.data)
        self.conn.commit()



class FuturesManagerPipeline:
    def __init__(self):
        self.conn = _getconnect()
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        self.conn.commit()
        if len(self.data) > 0:
            self._write_to_db()

        self.conn.close()

    def process_item(self, item, spider):
        page_data = tuple(dict(item).values())
        self.data.append(page_data)

        if len(self.data) == 20:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_Futuresmanager(usertenantid, managername, markstar, memberbehalf,membercode,memberdate, membertype, primaryinvesttype, page, managerenglishname, organcode, establishdate, registeraddress, officeaddress,registerasset, organtype, businesstype, employeenum, organwebaddress) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19)', self.data)
        self.conn.commit()


class FuturesPipeline:
    def __init__(self):
        self.conn = _getconnect()
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        self.conn.commit()
        if len(self.data) > 0:
            self._write_to_db()

        self.conn.close()

    def process_item(self, item, spider):
        page_data = tuple(dict(item).values())
        self.data.append(page_data)

        if len(self.data) == 20:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_Futuresno(id, aoiname, duedate, fundstatus, mpicreatedate, mpiname, mpiproductcode, mpitrustee, registereddate, sfjgh, tzlx, page) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)', self.data)
        self.conn.commit()

class FundProdPipeline:
    def __init__(self):
        # self.conn = cx_Oracle.connect('reader', 'reader', '192.168.144.66/eif')
        # self.cursor = self.conn.cursor()
        self.conn = _getconnect()
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        self.conn.commit()
        if len(self.data) > 0:
            self._write_to_db()

        self.conn.close()

    def process_item(self, item, spider):
        if item.get("establishDate") is not None:
            item["establishDate"] = datetime.datetime.fromtimestamp(item.get("establishDate")/1000).strftime('%Y-%m-%d')

        if item.get("putOnRecordDate") is not None:
            item["putOnRecordDate"] = datetime.datetime.fromtimestamp(item.get("putOnRecordDate")/1000).strftime('%Y-%m-%d')

        # one row insert
        # self.cursor.execute('insert into t_fundno(id,fundname,mamnagername,mandatorname,establishDate,putOnRecordDate) values (%s,%s,%s,%s,%s,%s)',(id,fundName,managerName,mandatorName,establishDate,putOnRecordDate))

        # batch insert

        # page_data = (item["id"], item["fundNo"], item["fundName"], item["managerId"], item["managerName"], item["managerType"],
        #              item["managerUrl"], item["mandatorName"], item["establishDate"], item["putOnRecordDate"], item["isDeputeManage"],
        #              item["lastQuarterUpdate"], item["url"], item["workingState"], item["page"], item["fundType"], item["moneyType"],
        #              item["lastUpDate"])
        page_data = tuple(dict(item).values())
        self.data.append(page_data)

        if len(self.data) == 20:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_fundnotest(id,fundno,fundname,managerid, managername, managertype, managerurl, mandatorname, establishdate, putonrecorddate,isdeputemanage,lastquarterupdate, url, workingstate,page, fundtype, money_type, lastupdate) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18)', self.data)
        self.conn.commit()


class FundManagerPipeline:
    def __init__(self):
        self.conn = cx_Oracle.connect('reader', 'reader', '192.168.144.66/eif')
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        self.conn.commit()
        if len(self.data) > 0:
            self._write_to_db()

        self.conn.close()

    def process_item(self, item, spider):
        id = item.get('id', '')
        artificialPersonName = item.get('artificialPersonName')
        fundCount = item.get('fundCount', '')
        fundTypeScaleMap = item.get('fundTypeScaleMap', '')
        hasCreditTips = item.get('hasCreditTips', '')
        hasSpecialTips = item.get('hasSpecialTips', '')
        managerHasProduct = item.get('managerHasProduct', '')
        managerName = item.get('managerName', '')
        managerEnglishName = item.get('managerEnglishName', '')
        establishDate = item.get('establishDate', '')
        establishDate = datetime.datetime.fromtimestamp(establishDate/1000).strftime('%Y-%m-%d')
        memberType = item.get('memberType', '')
        officeAddress = item.get('officeAddress', '')
        officeAdrAgg = item.get('officeAdrAgg', '')
        officeCity = item.get('officeCity', '')
        officeCoordinate = item.get('officeCoordinate')
        officeProvince = item.get('officeProvince')
        orgForm = item.get('orgForm')
        paidInCapital = item.get('paidInCapital')
        primaryInvestType = item.get('primaryInvestType')
        regAdrAgg = item.get('regAdrAgg')
        regCoordinate = item.get('regCoordinate')
        registerAddress = item.get('registerAddress')
        registerCity = item.get('registerCity')
        registerDate = item.get('registerDate')
        registerDate = datetime.datetime.fromtimestamp(registerDate/1000).strftime('%Y-%m-%d')
        registerNo = item.get('registerNo')
        registerProvince = item.get('registerProvince')
        url = item.get('url')
        organCode = item.get('organCode')
        registerAsset = item.get('registerAsset')
        payAsset = item.get('payAsset')
        registerAssetRto = item.get('registerAssetRto')
        enterpriceType = item.get('enterpriceType')
        businessType = item.get('businessType')
        employeeNum = item.get('employeeNum')
        practiceNum = item.get('practiceNum')
        isInvestAdvice = item.get('isInvestAdvice')
        manageScale = item.get('manageScale')
        lastUpDate = item.get('lastUpDate')
        subscribedCapital = item.get('subscribedCapital')
        page = item.get('page')

        # batch insert
        self.data.append((id,
                          artificialPersonName,
                          establishDate,
                          fundCount,
                          fundTypeScaleMap,
                          hasCreditTips,
                          hasSpecialTips,
                          managerHasProduct,
                          managerName,
                          managerEnglishName,
                          memberType,
                          officeAddress,
                          officeAdrAgg,
                          officeCity,
                          officeCoordinate,
                          officeProvince,
                          orgForm,
                          paidInCapital,
                          primaryInvestType,
                          regAdrAgg,
                          regCoordinate,
                          registerAddress,
                          registerCity,
                          registerDate,
                          registerNo,
                          registerProvince,
                          url,
                          organCode,
                          registerAsset,
                          payAsset,
                          registerAssetRto,
                          enterpriceType,
                          businessType,
                          employeeNum,
                          practiceNum,
                          isInvestAdvice,
                          manageScale,
                          lastUpDate,
                          subscribedCapital, page))

        if len(self.data) == 20:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_manager(id, artificialpersonname, establishdate, fundcount, fundtypescalemap, hascredittips, hasspecialtips, managerhasproduct, managername, managerenglishname, membertype, officeaddress, officeadragg, officecity, officecoordinate, officeprovince, orgform, paidincapital, primaryinvesttype, regadragg,regcoordinate, registeraddress, registercity,registerdate, registerno, registerprovince, url, organcode, registerasset, payasset, registerassetrto,enterpricetype, businesstype, employeenum, practicenum, isinvestadvice, managescale, lastupdate,subscribedcapital,page) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:30)', self.data)
        self.conn.commit()
