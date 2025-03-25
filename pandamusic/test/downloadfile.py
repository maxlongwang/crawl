import cx_Oracle
import requests
import asyncio
import aiohttp
import datetime

BATCHSIZE = 10
DOWNLOAD_FOLDER = 'd:/my/music'

cookies = {
    'b-user-id': 'b8a42176-40fd-5879-b419-a3d935be7373',
    '__sdid': 'AAQ5KOGTtXKBPSQyfGVieZ5QNL5m1w4ipbkylP+FZFySjv957P0rhPjuypDXZwtcmrM=',
    '_UP_A4A_11_': 'wb9c71a3a3504e4090f90f63bec53423',
    '_UP_30C_6A_': 'st9c762011ahnlbw9wl7emctjt8ep97q',
    '_UP_TS_': 'sg187851d9ee426f90755fe10ce41ada8c2',
    '_UP_E37_B7_': 'sg187851d9ee426f90755fe10ce41ada8c2',
    '_UP_TG_': 'st9c762011ahnlbw9wl7emctjt8ep97q',
    '_UP_335_2B_': '1',
    '__pus': 'e8bb58570af87a08420e204e98d3f1f8AARaagBLQw92PjdcUQmHbUv37mB3g+GAj95G6aWBaJJREdN+W7JcgzVy+jVhssVCOeWnJNlVCzYM5OIIf2wiaDWu',
    '__kp': '178c31a0-ffb2-11ef-9f92-e3ac45c550f8',
    '__kps': 'AARs6S/YJ9wh/9lAN2SAzsS5',
    '__ktd': 'jgKxlToza7NJnev+8RWDIg==',
    '__uid': 'AARs6S/YJ9wh/9lAN2SAzsS5',
    'xlly_s': '1',
    '__puus': 'a42cdfa1744f6c8966b716a9e3dfe8b3AAQIv81sMWIl8Xy1pT7m1dxL4A5YosiBUBuMiAamLLKL/zdrdalEHZNmZthKAQ54voj+zAss848OFvCa4Ppsc6AHd7vuBfAyBkPoXOqAP8Pme4ODNNspKASst4y9udR+rOPqKi12WTgr5fFSrQ/GLSl847JqjLnyIMqwhYLo3s3Wzr0lULaMGAmK54tiAxbjIQJYyOw1celXXl8afrfwt/2B',
    'tfstk': 'gRnoE_sCh4z5W2lOwjrWWGiDyiYvNTZQGXIL9kFeuSPb9LMKLkSE9vE88QMKiWP4dTJQYyPV08G9FWSyZjvnwvsLa7nLxylT4yg897F3xvGMHCK9XYM7APR96hCLESnzfwSUU6UV0RZ3U3wLzoH7AkRAHM89jYGNtb56KkJ00J2UUk7PYKf4QSSzLgyFgK2Qgk7UzkSV0J2uTkrETxJ0dSyrCssUsDoj0I7v1lv-zPn0EzVZnEshYaeP65DziMSUJ84lBYPcYMomkgGg5781HWZ8NYwoOhs74y0E2ooygHrZ5jm37lYpFloSLVgEh_v3axhSjuoMZgeY-70q4rXFYorxzPunZQb7a4h05-zVKhwx6SkS4qvCgYlTZuy4khJi3yuxVPiJggqZ5YE-8fRAy7ugLgRluNyLIMw2pm7CRzybn5eO-YsyIvuqiKvc5Uazh8d9nKbCR1sFjCpDnN17z-wJ6',
    'isg': 'BBsbJWv5-EM-7ASEvOcgjIGeqn-F8C_youNrQQ1YYJox7DrOlMI6QscmhkTid4fq',
}

download_urls = []
conn = cx_Oracle.connect('system', 'oracle', '192.168.144.66/eif')
cursor = conn.cursor()


# downloadfile=f'{DOWNLOAD_FOLDER}/{file_name}'

def get_downurl():
    global download_urls

    sql = "select file_name,download_url from scott.t_pandamusic where status=0 and create_date >=to_date('2025/3/24 18:04:22','yyyy/mm/dd hh24:mi:ss')  "
    cursor.execute(sql)
    download_urls = cursor.fetchall()


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
                file_name = filename.split('/')[-1]
                cursor.execute(f"update scott.t_pandamusic set status=1,update_date=sysdate where file_name='{file_name}'")
                conn.commit()
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
    while True:
        get_downurl()
        # download_all(download_urls)
        asyncio.run(download_all(download_urls))
    # download_file()

    cursor.close()
    conn.close()


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
