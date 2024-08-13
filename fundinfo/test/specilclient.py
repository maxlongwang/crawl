import re
with open("./test/20240812.sql", "r") as f:
    content=f.read()

lines=content.split('\n')
# data={}
for line in lines:
    if ',' in line:
        data=line.split(',')[1].split('=')[-1].strip("'")
        print(data)



