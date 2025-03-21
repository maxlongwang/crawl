from zipfile import ZipFile
import os
import itertools as its


def passwd(path, pwd):
    type_ = os.path.splitext(path)[-1][1:]
    if type_ == 'zip':
        with ZipFile(path, 'r') as zip:
            try:
                zip.extractall('./tmp', pwd=str(pwd).encode('utf-8'))
                return True
            except Exception as e:
                pass


def create_pwd(length):
    words = '0123456789abcdefghijk'
    for i in range(1, length):
        base = its.product(words, repeat=i)
        for i in base:
            yield ''.join(i)


if __name__ == "__main__":
    for p in create_pwd(5):
        flag = passwd('./aa.zip', p)
        if flag:
            break
