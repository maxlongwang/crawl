import xlwings as xw

# with xw.App(visible=True,add_book=False) as app:
#     book=app.books.add()
#     sht=book.sheets.add()
#     sht.range('A1').value='hello python'
#     book.save('./test.xlsx')

# Apps=xw.apps
# count=Apps.count
# print(count)

# keys=xw.apps.keys()
# print(keys)

 
app = xw.App(visible=True, add_book=False)  # 界面设置
# app.display_alerts = False  # 关闭提示信息
# app.screen_updating = False  # 关闭显示更新
 
wb = app.books.add()  # 创建新的工作簿
sht = wb.sheets['Sheet1']  # 实例化工作表
# sht.range('A1').value = 'Hello World!'
# sht.range('A1').value=[1,2,3]
# sht.range('A1').options(transpose=True).value=[4,5,6]

# sht.range('A1').value = [1, 2, 3, 4, 5]  #向 A1:E1 写入数据print(sheet.range('A1:E1').value)   

# print(sht.range('A1').value)  # 读取



# 选取第一列
rng=sht. range('A1').expand('down')
rng.value=['a1','a2','a3']
# 选取第一行
rng=sht.range('A1').expand('right')
#rng=['a1','b1']





# wb.close()
# app.kill()
