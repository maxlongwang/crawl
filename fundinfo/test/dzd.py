import OracleDBPool
import cx_Oracle
import xlwings as xw
import os
import shutil

def get_conn():
    dsn = "192.168.144.49/uf"
    user = "common"
    password = "oracle"
    pool = OracleDBPool.OracleDBPool(dsn=dsn, user=user, password=password)
    conn = pool.get_conn()
    return conn

#资金情况
def fundinfo():
    conn=get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data=cursor.callfunc('FN_EXCEL_1_0_1', cx_Oracle.NUMBER, ('6035000599', '6035000599', '20241213', '20241213', out_ref))
    v_cursor = out_ref.getvalue()
    fundinfo=[]
    for row in v_cursor:
        fundinfo.append(row)
        
    cursor.close()
    conn.close()  
    return fundinfo

#对账单
def dzdinfo():
    conn=get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data=cursor.callfunc('FN_EXCEL_1_0_2', cx_Oracle.NUMBER, ('11006318', '11006318', '20241213', '20241213', out_ref))
    v_cursor = out_ref.getvalue()
    datalist=[]
    for row in v_cursor:
        datalist.append(row)
        
    cursor.close()
    conn.close()  
    return datalist

    
    pass
#当日持仓清单
def stockholder():
    pass
#新股配号
def newstock():
    pass
#基金份额
def secumholder():
    pass



def openfile():
    shutil.copy("./test/template/(客户号)-(产品名称)-账户对账单(创建时间).xls","./test/dzdfiles/6035000599-运舟跨越2号私募证券投资基金-账户对账单20241213.xls")
    app = xw.App(visible=True, add_book=False) 
    wb = app.books.open('./test/dzdfiles/6035000599-运舟跨越2号私募证券投资基金-账户对账单20241213.xls')  
    sht = wb.sheets['账户对账单']
    funddata=fundinfo()
    for row in funddata:
        sht.range('A8').value=row[0]
        sht.range('B8').value=row[1]
        sht.range('C8').value=row[2]
        sht.range('D8').value=row[5]
        sht.range('E8').value=row[3]
        sht.range('F8').value=row[4]
        sht.range('O12').value=row[6]
        print(row)
    
    datalist=dzdinfo()
    spos=13
    rows=len(datalist)
    epos=spos + rows -1
    print('epos',epos)
    sht.range(f"13:{epos}").api.Insert()
    for row in datalist:
        sht.range(f'A{spos}').value=row
        spos=spos+1
    print('spos',spos)
    sht.range(f'F{spos}').formula=f'=sum(f13:f{epos})'
    sht.range(f'J{spos}').formula=f'=sum(j13:j{epos})'
    sht.range(f'K{spos}').formula=f'=sum(k13:k{epos})'
    sht.range(f'L{spos}').formula=f'=sum(l13:l{epos})'
    sht.range(f'M{spos}').formula=f'=sum(m13:m{epos})'
    sht.range(f'N{spos}').formula=f'=sum(n13:n{epos})'
    
    wb.save()
    wb.close()
    app.quit()   



if __name__ == "__main__":
    openfile()