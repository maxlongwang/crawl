from DataRecorder import Recorder
from DrissionPage import ChromiumPage
import time
import random
from DrissionPage.errors import *
from DrissionPage import SessionPage

'''
使用文件下载测试
采用drissionpage 
过滑块验证码

'''
page = ChromiumPage()
# recorder = Recorder('data.csv')
save_path = r'C:\Users\lwp54\Downloads'
page.get('https://www.1ppt.com/xiazai/')
while True:
    for item in page.ele('.tplist').children('t:li'):
        url = item('t:a').attr('href')
        page_detail = page.new_tab(url)  # 点击跳转新tab 打开详细页网页
        page_detail.set.load_mode.normal()
        down_url = page_detail.ele('.downurllist')('t:a').attr('href')
        page_detail.get(down_url)  # 打开下载地址

        for i in range(10):
            try:
                page_detail.actions.click('#nc_1__scale_text')
            except ElementNotFoundError:
                page_detail.refresh()
            # 划动验证码处理 滑块48*48,长度300，距离左边的距离是252，滑块需要划动252个像素
            page_detail.actions.hold('x://*[@id="nc_1_n1z"]')
            page_detail.actions.move(offset_x=252, offset_y=0, duration=random.uniform(0, 0.4))
            # page_detail.actions.release('x://*[@id="nc_1_n1z"]')  # 释放鼠标左键

            page_detail.set.load_mode.normal()
            try:
                down_url2 = page_detail.ele('.c1')('t:a').attr('href')
                if down_url2:
                    break
            except ElementNotFoundError:
                continue

        # 跳转到真正的下载链接页面
        # down_url2 = page_detail.ele('.c1')('t:a').attr('href')
        print(url, down_url2)

        page_down = SessionPage()
        res = page_down.download(down_url2, save_path)
        print(res)
        page_detail.close()

    btn = page('下一页', timeout=2)
    page.set.load_mode.normal()
    if btn:
        btn.click()
        page.wait.load_start()
    else:
        break

# page.close
