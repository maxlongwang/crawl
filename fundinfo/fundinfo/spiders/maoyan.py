from DataRecorder import Recorder
from DrissionPage import ChromiumPage
__date__ = '2024/10/31 17:27'
'''
猫眼的数据抓取，直接就启动浏览器进行抓取了
'''


page = ChromiumPage()
recorder = Recorder('data.csv')
page.get('https://www.maoyan.com/board/4')

while True:
    for mov in page.eles('tag:dd'):
        num = mov('t:i').text
        score = mov('.score').text
        title = mov('@data-act=boarditem-click').attr('title')
        star = mov('.star').text
        time = mov('.releasetime').text
        recorder.add_data((num, title, star, time, score))

    btn = page('下一页', timeout=2)
    if btn:
        btn.click()
        page.wait.load_start()
    else:
        break

recorder.record()
