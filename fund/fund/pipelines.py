# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
from itemadapter import ItemAdapter

import pymysql
import cx_Oracle


# mysql pipeline
class FundPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.144.89', port=3306,
                                    user='cif', password='12345678', database='cif', charset='utf8mb4')
        self.cursor = self.conn.cursor()
        self.data = []

    def close_spider(self, spider):
        self.conn.commit()
        if len(self.data) > 0:
            self._write_to_db()

        self.conn.close()

    def process_item(self, item, spider):
        # title=item.get('title','')
        # rank=item.get('rank',0)
        # subject=item.get('subject','')

        # self.cursor.execute('insert into t_fundinfo(title,rating,subject) values (%s,%s,%s)',(title,rank,subject))

        id = item.get('id', '')
        fundName = item.get('fundName', '')
        managerName = item.get('managerName', '')
        mandatorName = item.get('mandatorName', '')
        establishDate = item.get('establishDate', '')
        establishDate = datetime.datetime.fromtimestamp(
            establishDate/1000).strftime('%Y-%m-%d')
        putOnRecordDate = item.get('putOnRecordDate', '')
        putOnRecordDate = datetime.datetime.fromtimestamp(
            putOnRecordDate/1000).strftime('%Y-%m-%d')

        # one row insert
        # self.cursor.execute('insert into t_fundinfo(id,fundname,mamnagername,mandatorname,establishDate,putOnRecordDate) values (%s,%s,%s,%s,%s,%s)',(id,fundName,managerName,mandatorName,establishDate,putOnRecordDate))

        # batch insert
        self.data.append((id, fundName, managerName,
                         mandatorName, establishDate, putOnRecordDate))

        if len(self.data) == 100:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_fundinfo(id,fundname,mamnagername,mandatorname,establishDate,putOnRecordDate) values (%s,%s,%s,%s,%s,%s)', self.data)
        self.conn.commit()


# oracle save data

class FundPipeline_Oracle:
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
        fundNo = item.get('fundNo')
        fundName = item.get('fundName', '')
        managerId = item.get('managerId', '')
        managerName = item.get('managerName', '')
        managerType = item.get('managerType', '')
        managerUrl = item.get('managerUrl', '')

        mandatorName = item.get('mandatorName', '')
        establishDate = item.get('establishDate', '')
        establishDate = datetime.datetime.fromtimestamp(establishDate/1000).strftime('%Y-%m-%d')
        putOnRecordDate = item.get('putOnRecordDate', '')
        putOnRecordDate = datetime.datetime.fromtimestamp(putOnRecordDate/1000).strftime('%Y-%m-%d')
        isDeputeManage = item.get('isDeputeManage', '')
        lastQuarterUpdate = item.get('lastQuarterUpdate', '')
        url = item.get('url', '')
        workingState = item.get('workingState', '')
        fundType = item.get('fundType')
        moneyType = item.get('moneyType')
        lastUpDate = item.get('lastUpDate')
        # one row insert
        # self.cursor.execute('insert into t_fundno(id,fundname,mamnagername,mandatorname,establishDate,putOnRecordDate) values (%s,%s,%s,%s,%s,%s)',(id,fundName,managerName,mandatorName,establishDate,putOnRecordDate))

        # batch insert
        self.data.append((id, fundNo, fundName, managerId, managerName, managerType, managerUrl, mandatorName, establishDate,
                         putOnRecordDate, isDeputeManage, lastQuarterUpdate, url, workingState, fundType, moneyType, lastUpDate))

        if len(self.data) == 20:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_fundno(id,fundno,fundname,managerid, managername, managertype, managerurl, mandatorname, establishdate, putonrecorddate,isdeputemanage,lastquarterupdate, url, workingstate, fundtype, money_type, lastupdate) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17)', self.data)
        self.conn.commit()


class ManagerPipeline_Oracle:
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
                          lastUpDate))

        if len(self.data) == 20:
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into t_manager(id, artificialpersonname, establishdate, fundcount, fundtypescalemap, hascredittips, hasspecialtips, managerhasproduct, managername, managerenglishname, membertype, officeaddress, officeadragg, officecity, officecoordinate, officeprovince, orgform, paidincapital, primaryinvesttype, regadragg,regcoordinate, registeraddress, registercity,registerdate, registerno, registerprovince, url, organcode, registerasset, payasset, registerassetrto,enterpricetype, businesstype, employeenum, practicenum, isinvestadvice, managescale, lastupdate) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38)', self.data)
        self.conn.commit()
