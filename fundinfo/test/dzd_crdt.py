
from OracleDBPool import OracleDBPool
import cx_Oracle
import xlwings as xw
import shutil
from datetime import datetime
import tools


def head_info(busi_date):
    rq=tools.rq_cn(busi_date)
    return f'账单日期：{rq}--{rq}'
    

def basic_info(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_5_0_1', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist
    
    

def asset_info(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_5_0_2', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist

def secu_info(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_5_0_3', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist

def debit_info(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_5_0_4', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist

def crdt_detail(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_5_0_5', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist

def business_flow(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_5_0_6', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist

def openfile(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name):
    shutil.copy("./test/template/(客户号)-(产品名称)-融资融券对账单(创建时间).xls", f"./test/dzdfiles/{client_id}-{product_name}-融资融券对账单{busi_date}.xls")
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(f'./test/dzdfiles/{client_id}-{product_name}-融资融券对账单{busi_date}.xls')
    sht = wb.sheets['sheet1']
    head=head_info(busi_date)
    sht.range('a2').value = head
    
    sht.range('b4').value=product_name
    sht.range('e4').value=fund_account
    dataList=basic_info(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name)
    for row in dataList:
        sht.range('b5').value=row[0]
        sht.range('e5').value=row[1]
        sht.range('b6').value=row[2]
        sht.range('e6').value=row[3]
        sht.range('b7').value=row[4]
        sht.range('e7').value=row[5]
        sht.range('b8').value=row[6]
        sht.range('e8').value=row[7]
        sht.range('b9').value=row[8]
        sht.range('e9').value=row[9]
        sht.range('b10').value=row[10]
        sht.range('e10').value=row[11]
        sht.range('b11').value=row[12]
        
    dataList=asset_info(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name)
    spos=18
    for  row in dataList:
        sht.range('a{spos}').value=row
    
    dataList=secu_info(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name)
    spos=spos +4
    begin=spos
    if len(dataList) >0:
        for row in dataList:
            sht.range('a{spos}').value=row
            spos=spos +1
            sht.range(f"{spos}:{spos}").api.Insert()
        epos=spos-1
        sht.range(f'F{spos}').formula = f'=sum(f{begin}:f{epos})'
        sht.range(f'g{spos}').formula = f'=sum(g{begin}:g{epos})'
        
    spos=spos+5
    dataList=debit_info(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name)
    for row in dataList:
        sht.range('a{spos}').value=row
    
    spos=spos+5
    begin=spos
    dataList=crdt_detail(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name)
    if len(dataList)>0:
        for row in dataList:
            sht.range(f'a{spos}').value=row
            spos=spos +1
            sht.range(f"{spos}:{spos}").api.Insert()
        epos=spos-1
        sht.range(f'F{spos}').formula = f'=sum(f{begin}:f{epos})'
        sht.range(f'g{spos}').formula = f'=sum(g{begin}:g{epos})'
        sht.range(f'h{spos}').formula = f'=sum(h{begin}:h{epos})'
        sht.range(f'i{spos}').formula = f'=sum(i{begin}:i{epos})'
        sht.range(f'i{spos}').formula = f'=sum(i{begin}:i{epos})'
        sht.range(f'j{spos}').formula = f'=sum(j{begin}:j{epos})'
        sht.range(f'm{spos}').formula = f'=sum(m{begin}:m{epos})'
        
    spos=spos+5
    begin=spos
    dataList=business_flow(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name)
    if len(dataList)>0:
        for row in dataList:
            sht.range(f'a{spos}').value=row
            spos=spos +1
            sht.range(f"{spos}:{spos}").api.Insert()
        epos=spos-1

        sht.range(f'h{spos}').formula = f'=sum(h{begin}:h{epos})'
        sht.range(f'l{spos}').formula = f'=sum(l{begin}:l{epos})'
        sht.range(f'k{spos}').formula = f'=sum(k{begin}:k{epos})'
        sht.range(f'j{spos}').formula = f'=sum(j{begin}:j{epos})'
        sht.range(f'm{spos}').formula = f'=sum(m{begin}:m{epos})'
            
        
    wb.save()
    # wb.close()
    # app.quit()

        
    
    
if __name__ == "__main__":
    conn = OracleDBPool(dsn='192.168.144.66/eif', user='excelmanage', password='oracle').get_conn()
    cursor = conn.cursor()
    cursor.execute("select client_id,fund_account,product_name,op_dept_name,op_user_name from excelmanage.t_excel_target where client_id='6030001913'")
    result = cursor.fetchall()
    busi_date = '20241213'
    for row in result:
        client_id = row[0]
        fund_account = row[1]
        product_name = row[2]
        op_dept_name = row[3]
        op_user_name=row[4]
        openfile(busi_date, client_id, fund_account, product_name, op_dept_name,op_user_name)
    cursor.close()
    conn.close()
    