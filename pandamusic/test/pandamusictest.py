import execjs

with open('./test/pandamusic/pandamusic.js','r',encoding='utf-8') as f:
    js_code=f.read()


e = ["1bb86dafd55144a6adc1c442187b759e"]
r = ["d4868ca65e5538cfd3fffc791ac59464"]
n = { 'isCanDirectDownload': True }
    
result=execjs.compile(js_code).call('download',e,r,n)
print(result)