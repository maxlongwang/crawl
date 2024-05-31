import ddddocr
'''
输入验证码ocr识别
'''

ocr= ddddocr.DdddOcr()
with open(r'test\ocr_img\image.png','rb') as f:
    img_bytes=f.read()

res=ocr.classification(img_bytes)
print(res)
