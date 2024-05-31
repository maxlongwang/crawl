'''
把pdf转换成csv文件，需要使用tabula包
 pip install tabula-py
'''

import tabula
df = tabula.read_pdf("tmp.pdf", pages='all')[0]
tabula.convert_into("tmp.pdf", "trav.csv", output_format="csv", pages='all')
print(df)
