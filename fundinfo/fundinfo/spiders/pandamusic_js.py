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
    name = 'pandamusicjs'
    # allowed_domains = ["xmwav.com/"]
    start_urls = ["https://www.xmwav.com/msctdlist/rcmsc.html#"]
    # custom_settings = {'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 300}, }
    custom_settings = {'ITEM_PIPELINES': {'fundinfo.pipelines_pm.PandaMusicPipeline': 300},}

    params = {
        'pr': 'ucpro',
        'fr': 'pc',
        'uc_param_str': '',
        '__dt': '546',
        '__t': '1742177515276'}

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

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url)

    # 获取歌曲列表链接地址

    def parse(self, response):
        url_list = response.xpath('//div[@class="stream-list question-stream"]/a/@href').getall()
        for surl in url_list:
            url = response.urljoin(surl)
            pmitem = PandaMusicItem()
            pmitem['url'] = url
            yield scrapy.Request(url=url, callback=self.parse_gotourl, cb_kwargs={'item': pmitem})

    # 跳转到下载显示界面，获取跳转到夸克网盘的地址，会有重定向
    def parse_gotourl(self, response, **kwargs):
        pmitem = kwargs['item']
        url = response.xpath('//div[@class="info-zi mb15"]/a[2]/@href').get()
        url = response.urljoin(url)
        pmitem['url_goto'] = url
        # yield scrapy.Request(url=full_url,  meta={'handle_httpstatus_list': [301, 302]}, callback=self.after_redirect)
        yield scrapy.Request(url=url, callback=self.parse_redirect, cb_kwargs={'item': pmitem})

    def parse_redirect(self, response, **kwargs):
        pmitem = kwargs['item']
        script_tag = response.css('script:contains("window.location.href")::text').get()
        match = re.search(r"window.location.href='(.*?)';", script_tag)
        url = match.group(1)
        pwd_id = url.split('/')[-1]
        pmitem['pwd_id'] = pwd_id
        pmitem['url_redirect'] = url
        yield scrapy.Request(url=url, callback=self.parse_stoken, cb_kwargs={'item': pmitem})
        
    
    def parse_stoken(self,response,**kwargs):
        pmitem = kwargs['item']
        json_data = {
            'pwd_id': pmitem['pwd_id'],
            'passcode': '',
        }

        params = {
            'pr': 'ucpro',
            'fr': 'pc',
            'uc_param_str': '',
            '__dt': '596',
            '__t': '1742200522365',
        }

        response = requests.post(
            'https://drive-h.quark.cn/1/clouddrive/share/sharepage/token',
            params=params,
            cookies=self.cookies,
            # headers=headers,
            json=json_data,
        )
        jsonData = response.json()
        stoken = jsonData['data']['stoken']
        pmitem['file_name']=jsonData['data']['title']
        pmitem['stoken'] = stoken
        pwd_id = pmitem['pwd_id']
        time.sleep(0.5)
        dt=random.randint(10000,1000000)
        t=int(time.time()*1000)
    
        url = f"https://drive-h.quark.cn/1/clouddrive/share/sharepage/detail?pr=ucpro&fr=pc&uc_param_str=&pwd_id={pwd_id}&stoken={stoken}&pdir_fid=0&force=0&_page=1&_size=50&_fetch_banner=1&_fetch_share=1&_fetch_total=1&_sort=file_type:asc,file_name:asc&__dt={dt}&__t={t}"
        response=requests.get(url=url,cookies=self.cookies)
        jsonData=response.json()
        fid = jsonData["data"]["list"][0]["fid"]
        fid_token_list = jsonData["data"]["list"][0]["share_fid_token"]
        pmitem['fid'] = fid
        pmitem['fid_token_list'] = fid_token_list
        
        params = {
            'pr': 'ucpro',
            'fr': 'pc',
            'uc_param_str': '',
            'aver': '1',
            '__dt': '16129',
            '__t': '1742200537898',
        }
        url = 'https://drive-pc.quark.cn/1/clouddrive/share/sharepage/dir'
        response = requests.get(
            url=url,
            params=params,
            cookies=self.cookies,
            # headers=headers,
        )
        jsonData = response.json()
        to_pdir_fid = jsonData['data']['pdir_fid']
        pmitem['to_pdir_fid'] = to_pdir_fid
        fid = pmitem['fid']
        fid_token_list = pmitem['fid_token_list']
        pwd_id = pmitem['pwd_id']
        stoken = pmitem['stoken']
        url = 'https://drive-pc.quark.cn/1/clouddrive/share/sharepage/save'
        json_data = {
            'fid_list': [
                fid,
            ],
            'fid_token_list': [
                fid_token_list,
            ],
            'to_pdir_fid': to_pdir_fid,
            'pwd_id': pwd_id,
            'stoken': stoken,
            'pdir_fid': '0',
            'scene': 'link',
        }
        response = requests.post(
            url=url,
            params=params,
            cookies=self.cookies,
            json=json_data
            # headers=headers,
        )
        jsonData = response.json()

        task_id = jsonData['data']['task_id']
        pmitem['task_id'] = task_id

        url = 'https://drive-pc.quark.cn/1/clouddrive/task'
        dt=random.randint(10000,1000000)
        t=int(time.time()*1000)

        params = {
            'pr': 'ucpro',
            'fr': 'pc',
            'uc_param_str': '',
            'task_id': task_id,
            'retry_index': '0',
            '__dt': dt,
            '__t': t,
        }

        response = requests.get(url=url, params=params, cookies=self.cookies)
        time.sleep(0.5)
        dt=random.randint(10000,1000000)
        t=int(time.time()*1000)
        
        params = {
            'pr': 'ucpro',
            'fr': 'pc',
            'uc_param_str': '',
            'task_id': task_id,
            'retry_index': '1',
            '__dt': dt,
            '__t': t,
        }
        response = requests.get(url=url, params=params, cookies=self.cookies)
        jsonData = response.json()
        fid_encrypt = jsonData['data']['save_as']['save_as_top_fids'][0]
        pmitem['fid_encrypt'] = fid_encrypt

        url = 'https://drive-pc.quark.cn/1/clouddrive/file/download'
        params = {
            'pr': 'ucpro',
            'fr': 'pc',
            'uc_param_str': '',
            '__dt': '114686',
            '__t': '1742200636455',
        }

        json_data = {
            'fids': [
                fid_encrypt,
            ],
        }
        response = requests.post(url=url, params=params, json=json_data ,cookies=self.cookies)

        jsonData = response.json()
        download_url = jsonData["data"][0]["download_url"]
        pmitem['download_url'] = download_url
        print(pmitem)
        yield pmitem
