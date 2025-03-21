from typing import Any
import scrapy
from fundinfo.items_pandamusic import PandaMusicItem
import re
import json
import requests
from urllib.parse import urlencode
from scrapy.http import JsonRequest
import time
import random


class PandaMusic(scrapy.Spider):
    name = 'pandamusic'
    # allowed_domains = ["xmwav.com/"]
    start_urls = [f"https://www.xmwav.com/msclist/dy.html?classname=dy&page={i}" for i in range(1, 2) ]
    # start_urls=[]
    # for i in range(2, 3):
    #     url_page = f"{url}{i}"
    #     start_urls.append(url_page)

    # custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 300}, }
    custom_settings = {'ITEM_PIPELINES': {'fundinfo.pipelines_pm.PandaMusicPipeline': 300}, }

    params = {
        'pr': 'ucpro',
        'fr': 'pc',
        'uc_param_str': '',
        '__dt': '568',
        '__t': '1742454972456'}

    cookies = {
        'b-user-id': '9d6ab9c1-d341-b535-68bd-b551459d452b',
        '_UP_A4A_11_': 'wb9c5196c2374642bcdcd6c2ebad6595',
        '__sdid': 'AAQtHG7PA09Iw8ir4BP1ZluEN2RKBDfehCJALqXxVdaOfDCuTe9WXCkXnLYB+JbtyJ8=',
        '_UP_D_': 'pc',
        '_UP_30C_6A_': 'st9c762013azlv0bprwnf8r2fmzeue7n',
        '_UP_TS_': 'sg11db5c183a5f6c821169eaa0ef812abc1',
        '_UP_E37_B7_': 'sg11db5c183a5f6c821169eaa0ef812abc1',
        '_UP_TG_': 'st9c762013azlv0bprwnf8r2fmzeue7n',
        '_UP_335_2B_': '1',
        '__pus': 'e626bf4022e06ba1491cf4c2f1501443AASlVSEW/AgR1dOFT7v2ci3nqT95AM71/BQJMk63mxYo2pzDHv2VYu2wP6sXwyKxmRFe9mIQUUSmoWRZcnCt9/r8',
        '__kp': '65db4540-ff20-11ef-a188-3b83bfcf410b',
        '__kps': 'AARs6S/YJ9wh/9lAN2SAzsS5',
        '__ktd': 'jgKxlToza7NJnev+8RWDIg==',
        '__uid': 'AARs6S/YJ9wh/9lAN2SAzsS5',
        'xlly_s': '1',
        '__puus': '8d879bb888e36f025343854cd93a1408AAQIv81sMWIl8Xy1pT7m1dxL0AEe2ktCSZQXC1bkJcF2qrv6Y8q5hILnPhkq9Zp5H1rwNAq3yEDmVIQNI+g2Jrq8bkUZo4elwqnNpmNCN+6D67lKegsmjHBi87g5oTB55JypaOPfjdNbIMFptQScklzXykDk2yTtpeHCK+Z9BT1xBGL35FgBcjHLAX/iOXq+cdRZ52CjViJHaPBnN7JqKCPx',
        'tfstk': 'gvWxH0ZcQz4m7Tp3n-NoI2hGoRqutOIVyZSIIFYm1aQRbNdM1IxDBC_XrtAMhEb-Ph7hnxMX1A35SHGfhK_gBFsezxbggCDt0TQKIx44gGM9Ida3-J2h0nvwCyA7KTiwuhSW5uAXaWtCPda3-8coVIzDCZmP6XHRVU-9cmO153ZJ0UMXfxtsPuKwPdgjhCiWVHt6fF_6CuIWzh96cbR0WUiXSACIoqsNG28SCA6JDINlcUM64TKvMesfUAMs_ndvRiT88Umh1Qsw6OoZBCjfTN-Clqa97TI5h6_QrjYf9hIh6wZig3AO3LL1hJopPtIOeI5oljtpHEdChaiUxgd1wTpchPlFqgLX9LfuarAMHZCe8INzzNIJoN6vNqUkS6jlhQQQrYQw616DFta7pg81K9eIi2YpjjZ82flwG37q21pEuGP4A3L3DRhZ_Qry2eq82fGs5u-J-oEt_fRz4',
        'isg': 'BNzcaaQh1za4c6M63aRWhZD2rfqOVYB_VCJ4Fbbd6UeqAXyL3mSsD563YWn5j7jX',
    }

    def get_dt(self):
        return random.randint(10000, 1000000)

    def get_t(self):
        return int(time.time()*1000)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url)

    # 获取歌曲列表链接地址

    def parse(self, response):
        url_list = response.xpath('//div[@class="stream-list question-stream"]/a/@href').getall()
        for surl in url_list:
            url = response.urljoin(surl)
            pmitem = PandaMusicItem()
            pmitem['url_page'] = response.url
            pmitem['url'] = url
            yield scrapy.Request(url=url, callback=self.parse_gotourl, cb_kwargs={'item': pmitem})

    # 跳转到下载显示界面，获取跳转到夸克网盘的地址，会有重定向

    def parse_gotourl(self, response, **kwargs):
        pmitem = kwargs['item']
        url = response.xpath('//div[@class="info-zi mb15"]/a[2]/@href').get()
        url = response.urljoin(url)
        pmitem['url_goto'] = url
        yield scrapy.Request(url=url, callback=self.parse_redirect, cb_kwargs={'item': pmitem})

    def parse_redirect(self, response, **kwargs):
        pmitem = kwargs['item']
        script_tag = response.css('script:contains("window.location.href")::text').get()
        match = re.search(r"window.location.href='(.*?)';", script_tag)
        url = match.group(1)
        pwd_id = url.split('/')[-1]
        pmitem['pwd_id'] = pwd_id
        pmitem['url_redirect'] = url

        json_data = {
            'pwd_id': pmitem['pwd_id'],
            'passcode': '',
        }
        self.params['__t'] = self.get_t()
        self.params['__dt'] = self.get_dt()

        url = 'https://drive-h.quark.cn/1/clouddrive/share/sharepage/token?' + urlencode(self.params)

        yield scrapy.Request(url=url, method='POST', cookies=self.cookies, body=json.dumps(json_data),  callback=self.parse_stoken, cb_kwargs={'item': pmitem})

    def parse_stoken(self, response, **kwargs):
        pmitem = kwargs['item']
        jsonData = json.loads(response.body)
        stoken = jsonData['data']['stoken']
        pmitem['file_name'] = jsonData['data']['title']
        pmitem['stoken'] = stoken
        pwd_id = pmitem['pwd_id']
        t = self.get_t()
        dt = self.get_dt()

        params = {
            'pr': 'ucpro',
            'fr': 'pc',
            'uc_param_str': '',
            'pwd_id': pwd_id,
            'stoken': stoken,
            'pdir_fid': '0',
            'force': '0',
            '_page': '1',
            '_size': '50',
            '_fetch_banner': '1',
            '_fetch_share': '1',
            '_fetch_total': '1',
            '_sort': 'file_type:asc,file_name:asc',
            '__dt': dt,
            '__t': t

        }

        url = f"https://drive-h.quark.cn/1/clouddrive/share/sharepage/detail?" + urlencode(params)
        yield scrapy.Request(url=url, cookies=self.cookies, callback=self.parse_fid_token, cb_kwargs={'item': pmitem})

    def parse_fid_token(self, response, **kwargs):
        pmitem = kwargs['item']
        jsonData = json.loads(response.body)
        fid = jsonData["data"]["list"][0]["fid"]
        fid_token_list = jsonData["data"]["list"][0]["share_fid_token"]
        pmitem['fid'] = fid
        pmitem['fid_token_list'] = fid_token_list

        self.params['aver'] = 1
        self.params['__t'] = self.get_t()
        self.params['__dt'] = self.get_dt()
        url = 'https://drive-pc.quark.cn/1/clouddrive/share/sharepage/dir?'+urlencode(self.params)

        yield scrapy.Request(url=url, cookies=self.cookies, callback=self.parse_pdir_fid, cb_kwargs={'item': pmitem})

    def parse_pdir_fid(self, response, **kwargs):
        pmitem = kwargs['item']
        jsonData = json.loads(response.body)
        jsonData = response.json()
        to_pdir_fid = jsonData['data']['pdir_fid']
        pmitem['to_pdir_fid'] = to_pdir_fid
        fid = pmitem['fid']
        fid_token_list = pmitem['fid_token_list']
        pwd_id = pmitem['pwd_id']
        stoken = pmitem['stoken']

        url = 'https://drive-pc.quark.cn/1/clouddrive/share/sharepage/save'
        json_data = {
            'fid_list': [fid,],
            'fid_token_list': [fid_token_list,],
            'to_pdir_fid': to_pdir_fid,
            'pwd_id': pwd_id,
            'stoken': stoken,
            'pdir_fid': '0',
            'scene': 'link',
        }
        url = url + '?' + urlencode(self.params)
        yield scrapy.Request(url=url, method='POST', cookies=self.cookies, body=json.dumps(json_data),  callback=self.parse_taskid, cb_kwargs={'item': pmitem})

    def parse_taskid(self, response, **kwargs):
        pmitem = kwargs['item']
        jsonData = json.loads(response.body)
        task_id = jsonData['data']['task_id']
        pmitem['task_id'] = task_id

        self.params['task_id'] = task_id
        self.params['retry_index'] = 0
        n=random.randint(1,5)
        time.sleep(n)

        url = 'https://drive-pc.quark.cn/1/clouddrive/task'
        url = url + '?' + urlencode(self.params)
        # scrapy.Request(url=url, cookies=self.cookies, cb_kwargs={'item': pmitem})
        # self.params['retry_index'] = 1
        yield scrapy.Request(url=url, cookies=self.cookies, callback=self.parse_fid_entry, cb_kwargs={'item': pmitem})

    def parse_fid_entry(self, response, **kwargs):
        pmitem = kwargs['item']
        jsonData = json.loads(response.body)
        fid_encrypt = jsonData['data']['save_as']['save_as_top_fids'][0]
        pmitem['fid_encrypt'] = fid_encrypt
        task_id = pmitem['task_id']
        time.sleep(1)
        self.params['__t'] = self.get_t()
        self.params['__dt'] = self.get_dt()

        url = 'https://drive-pc.quark.cn/1/clouddrive/file/download'
        url = url+"?" + urlencode(self.params)

        json_data = {
            'fids': [
                fid_encrypt,
            ],
        }
        self.params.pop('aver',None)
        self.params.pop('task_id',None)
        self.params.pop('retry_index',None)
        
        yield scrapy.Request(url=url, method='POST', body=json.dumps(json_data), cookies=self.cookies, callback=self.parase_downloadurl, cb_kwargs={'item': pmitem})

    def parase_downloadurl(self, response, **kwargs):
        pmitem = kwargs['item']
        jsonData = json.loads(response.body)
        download_url = jsonData["data"][0]["download_url"]
        pmitem['download_url'] = download_url
        yield pmitem
