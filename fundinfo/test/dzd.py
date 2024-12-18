from OracleDBPool import OracleDBPool
import cx_Oracle
import xlwings as xw
import shutil
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import tools


def pare_date(busi_date):
    year = busi_date[:4]
    month = busi_date[4:6]
    day = busi_date[6:]
    rq = f'{year}年{month}月{day}日'
    return f'起止日期：{rq}--{rq}'

# 资金情况


def fundinfo(busi_date, client_id, fund_account, product_name, op_dept_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_1_0_1', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    fundinfo = []
    for row in v_cursor:
        fundinfo.append(row)

    cursor.close()
    conn.close()
    return fundinfo

# 对账单


def dzdinfo(busi_date, client_id, fund_account, product_name, op_dept_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_1_0_2', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist

# 当日持仓清单


def stockholder(busi_date, client_id, fund_account, product_name, op_dept_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_1_0_3', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist

# 新股配号


def newstock(busi_date, client_id, fund_account, product_name, op_dept_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_1_0_4', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist

# 基金份额


def secumholder(busi_date, client_id, fund_account, product_name, op_dept_name):
    conn = OracleDBPool(dsn='192.168.144.49/uf', user='common', password='oracle').get_conn()
    cursor = conn.cursor()
    out_ref = cursor.var(cx_Oracle.CURSOR)
    data = cursor.callfunc('FN_EXCEL_1_0_5', cx_Oracle.NUMBER, (client_id, fund_account, busi_date, busi_date, out_ref))
    v_cursor = out_ref.getvalue()
    datalist = []
    for row in v_cursor:
        datalist.append(row)

    cursor.close()
    conn.close()
    return datalist


def create_user(op_dept_name):
    dt = datetime.now()
    year = dt.strftime('%Y')
    month = dt.strftime('%m')
    day = dt.strftime('%d')
    hour = dt.strftime('%H')
    minute = dt.strftime('%M')
    second = dt.strftime('%S')
    rq = f'制表日期：{year}年{month}月{day}日 {hour}:{minute}:{second}       操作员：{op_dept_name}'
    return rq


def openfile(busi_date, client_id, fund_account, product_name, op_dept_name, op_user_name):
    shutil.copy("./test/template/(客户号)-(产品名称)-账户对账单(创建时间).xls", f"./test/dzdfiles/{client_id}-{product_name}-账户对账单{busi_date}.xls")
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(f'./test/dzdfiles/{client_id}-{product_name}-账户对账单{busi_date}.xls')
    sht = wb.sheets['账户对账单']
    # headinfo
    sht.range('a3').value = f'客户姓名：{product_name}'
    sht.range('d3').value = f'制表：{op_dept_name}'
    sht.range('a4').value = pare_date(busi_date)

    funddata = fundinfo(busi_date, client_id, fund_account, product_name, op_dept_name)
    for row in funddata:
        sht.range('A8').value = row[0]
        sht.range('B8').value = row[1]
        sht.range('C8').value = row[2]
        sht.range('D8').value = row[5]
        sht.range('E8').value = row[3]
        sht.range('F8').value = row[4]
        sht.range('O12').value = row[6]

    dzd_list = dzdinfo(busi_date, client_id, fund_account, product_name, op_dept_name)
    dzd_list_rows = len(dzd_list)
    stock_holder_list = stockholder(busi_date, client_id, fund_account, product_name, op_dept_name)
    stock_holder_list_rows = len(stock_holder_list)
    new_stock_list = newstock(busi_date, client_id, fund_account, product_name, op_dept_name)
    new_stock_list_rows = len(new_stock_list)
    secum_holder_list = secumholder(busi_date, client_id, fund_account, product_name, op_dept_name)
    secum_holder_list_rows = len(secum_holder_list)
    
    stock_holder_pos=0
    if stock_holder_list_rows >1 :
        stock_holder_pos=stock_holder_list_rows -1
    new_stock_pos=0
    if new_stock_list_rows>1:
        new_stock_pos=new_stock_list_rows-1
    secum_holder_pos=0
    if secum_holder_list_rows>1:
        secum_holder_pos=secum_holder_list_rows-1

    if dzd_list_rows > 0:
        spos = 13
        begin = spos
        endpos = spos+dzd_list_rows-1
        sht.range(f"{spos}:{endpos}").api.Insert()
        for row in dzd_list:
            sht.range(f'A{spos}').value = row
            spos = spos+1
        epos = spos-1
        sht.range(f'F{spos}').formula = f'=sum(f{begin}:f{epos})'
        sht.range(f'J{spos}').formula = f'=sum(j{begin}:j{epos})'
        sht.range(f'K{spos}').formula = f'=sum(k{begin}:k{epos})'
        sht.range(f'L{spos}').formula = f'=sum(l{begin}:l{epos})'
        sht.range(f'M{spos}').formula = f'=sum(m{begin}:m{epos})'
        sht.range(f'N{spos}').formula = f'=sum(n{begin}:n{epos})'

    if stock_holder_list_rows > 0:
        spos = 17+dzd_list_rows
        begin = spos
        endpos = spos + stock_holder_list_rows-1
        if stock_holder_list_rows > 1:
            sht.range(f"{spos+1}:{endpos}").api.Insert()
        for row in stock_holder_list:
            sht.range(f'A{spos}').value = row[1:12]
            spos = spos+1
        epos = spos-1
        sht.range(f'D{spos}').formula = f'=sum(d{begin}:d{epos})'
        sht.range(f'H{spos}').formula = f'=sum(h{begin}:h{epos})'
        sht.range(f'K{spos}').formula = f'=sum(k{begin}:k{epos})'
        sht.range(f'J{spos}').formula = f'=sum(j{begin}:j{epos})'

    if new_stock_list_rows > 0:
        spos = 22 + stock_holder_pos + dzd_list_rows
        begin = spos
        endpos = spos + new_stock_list_rows
        if new_stock_list_rows > 1:
            sht.range(f"{spos+1}:{endpos}").api.Insert()
        for row in new_stock_list:
            sht.range(f'A{spos}').value = row
            spos = spos+1

    if secum_holder_list_rows > 0:
        spos = 26+stock_holder_pos + dzd_list_rows + new_stock_pos
        begin = spos
        endpos = spos + secum_holder_list_rows
        if secum_holder_list_rows > 1:
            sht.range(f"{spos+1}:{endpos}").api.Insert()
        for row in secum_holder_list:
            sht.range(f'A{spos}').value = row
            spos = spos+1
        epos = spos-1
        sht.range(f'F{spos}').formula = f'=sum(F{begin}:F{epos})'
        sht.range(f'L{spos}').formula = f'=sum(L{begin}:L{epos})'
        sht.range(f'K{spos}').formula = f'=sum(k{begin}:k{epos})'
        sht.range(f'J{spos}').formula = f'=sum(j{begin}:j{epos})'
    

    
    spos = 29 + stock_holder_pos + new_stock_pos +secum_holder_pos + dzd_list_rows
    user = create_user(op_user_name)
    sht.range(f'A{spos}').value = user

    wb.save()
    wb.close()
    app.quit()


if __name__ == "__main__":
    conn = OracleDBPool(dsn='192.168.144.66/eif', user='excelmanage', password='oracle').get_conn()
    cursor = conn.cursor()
    cursor.execute("select client_id,fund_account,product_name,op_dept_name,op_user_name from excelmanage.t_excel_target where product_status=1  ")
    result = cursor.fetchall()
    busi_date = '20241213'
    futures = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for row in result:
            client_id = row[0]
            fund_account = row[1]
            product_name = row[2]
            op_dept_name = row[3]
            op_user_name = row[4]
            futures.append(executor.submit(openfile, busi_date, client_id, fund_account, product_name, op_dept_name, op_user_name))
            # openfile(busi_date, client_id, fund_account, product_name, op_dept_name, op_user_name)
    
        # for future in futures:
        #     try:
        #         future.result() # 获取结果，若有异常会抛出
        #         print(f"Batch imported successfully.{tools.now()}")
        #     except Exception as e:
        #         print(f"Error occurred: {e}")

    cursor.close()
    conn.close()
