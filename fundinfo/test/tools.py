import datetime

def rq_cn(busi_date):
    year=busi_date[:4]
    month=busi_date[4:6]
    day=busi_date[6:]
    rq=f'{year}年{month}月{day}日'
    return rq


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
