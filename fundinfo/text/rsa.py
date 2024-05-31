import base64
from binascii import hexlify



def RSA(text):
    f="dsfdsafdsfdsafdsa"
    e="01001"
    text=text[::-1] #倒序
    # 返回二进制数据的16进制表示

    result = pow(int(hexlify(text.encode()),16),int(e,16),int(f,16))
    # 131 的压缩 进制的映射
    return format(result,'x').zfill(131)


import random
def RandomString(a):
    '''
    随机返回16位字符串,a(16)
    '''
    string='abcdefghijklmnopqrstuvwzyxABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    randomStr=random.sample(string, a)
    return "".join(randomStr)

def AESEncrypt(text,key):
    # 初识向量->字节
    iv=b'0102030405060708'
    # 填充AES 密钥16位 目的：保障密钥的长度符合 填充 删除
    # 16位数据 转变bytes pkcs7填充 固定方法
    pad=16-len(text)%16
    text = text +chr(2) * pad
    #创建AES对象 字符
    encryptor=AES.new(key.encode(),AES.MODE_CBC,iv)
    # AES 进行加密
    encryptor_str=encryptor.entrypt(text.encode())
    result=base64.b64encode(encryptor_str).decode()
    return result

def AES2(text,random_str):
    '''
    第二次AES加密
    '''
    first_aes=AESEncrypt(text,key='oCOJUm6qym8W8jud')
    # 第二次加密 把第一次加密内容+密钥为i(随机16个字符串)
    second_aes=AESEncrypt(first_aes,random_str)
    return second_aes 

