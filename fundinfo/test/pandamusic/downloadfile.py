import cx_Oracle
import requests
import asyncio
import aiohttp
import datetime

BATCHSIZE = 10
DOWNLOAD_FOLDER = 'd:/my/music'

cookies = {
    'b-user-id': '9d6ab9c1-d341-b535-68bd-b551459d452b',
    '_UP_A4A_11_': 'wb9c5196c2374642bcdcd6c2ebad6595',
    '__sdid': 'AAQtHG7PA09Iw8ir4BP1ZluEN2RKBDfehCJALqXxVdaOfDCuTe9WXCkXnLYB+JbtyJ8=',
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
    '__puus': '5ff1237dea213c6d616fe5e76f00ca69AAQIv81sMWIl8Xy1pT7m1dxLBroePGqF3OhHAWa53cJTbbr5yXElMZ1QbSYxyEYflCe1T6/yizxptfLTULELn4nd6vvrfNNZidxFHjlx+ZWRmPo+5Gditn8A3IR7bZh01dTMsj8pC64WiffgGpJ0Q8qOnbyn8kPYjKFJFtFeV7e55ZurLGavebHArvzWgVyp5OTPAWZxuabYb31yBqglHS4m',
    'isg': 'BGZm2V7YPSpz0-ncOxZMy15Et9zoR6oBKlAyM1APGwlk0wbtuNGdEUygL8_f_qIZ',
    'tfstk': 'g5uIFfmsE9XIm4Witpda1oH4UfzSFYT4J_N-ibQFwyUKwzM_QWSexuJSfYHapwzpxOE7iW689zIpWaNzEJUrYJP-CbHpt7RnPcbSib0etzR3-X4uyKJ2u8GntzV-BSADQfd8ZzNpkZ5ySX4uyd5Nyn8jtxIHIY38yCaTaW_8yMeJ1OF8BwFRJ7B9172Ty7QL2fhTNSP8eWH-6CNuB8U8ybSCG7tQKXOKadsZkLDt9R_Ry2LuA-NG4aQ8RWZIlXesADg_OkwYjKh342HZw2u3jhjarfojF0HvQMyKcSM_0D9fRxM3wAaEkQx3ju3SP5mMFgwj2Xom2lOpJfaQdxgiB_IQR0HnPkmCZIcTJAm0nkKMI5gEuuw0fOpK_fwLc0MeIaeEcfH_0VWNurnmC4ZYkg-Pu-TZig1_maN_3CO1qg0NHgGJGoixBkFgOlR619nuv5V_34R1x0qLsWww1C6Kq',
}
download_urls = []


# downloadfile=f'{DOWNLOAD_FOLDER}/{file_name}'

def get_downurl():
    global download_urls
    conn = cx_Oracle.connect('system', 'oracle', '192.168.144.66/eif')
    cursor = conn.cursor()
    sql = "select file_name,download_url from scott.t_pandamusic where create_date >=to_date('2025/3/21 15:30:06','yyyy/mm/dd hh24:mi:ss') "
    cursor.execute(sql)
    download_urls = cursor.fetchall()
    cursor.close()
    conn.close()


async def download_file(session, url, filename):
    async with session.get(url=url, cookies=cookies) as response:
        if response.status == 200:
            with open(filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
                print(f'{filename} download success.{datetime.datetime.now()}')
        else:
            print(f'{filename} download failure. {response.status}')


async def download_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for row in urls:
            file_name = row[0]
            download_url = row[1]
            filename = f'{DOWNLOAD_FOLDER}/{file_name}'
            task = asyncio.create_task(download_file(session, download_url, filename))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    get_downurl()
    # download_all(download_urls)
    asyncio.run(download_all(download_urls))
    # download_file()


# try:
#     response=requests.get(url=url,cookies=cookies, stream=True)
#     response.raise_for_status()
#     with  open(file_name,'wb') as f:
#         for chunk in response.iter_content(chunk_size=8192):
#             if chunk:
#                 f.write(chunk)
#     print(f'{file_name} download success.')
# except Exception as e:
#     print(f'{file_name} download error.{e}')
