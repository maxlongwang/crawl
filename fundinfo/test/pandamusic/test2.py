import requests

cookies = {
    'b-user-id': 'b8a42176-40fd-5879-b419-a3d935be7373',
    '__sdid': 'AAQ5KOGTtXKBPSQyfGVieZ5QNL5m1w4ipbkylP+FZFySjv957P0rhPjuypDXZwtcmrM=',
    '_UP_D_': 'pc',
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
    '__puus': 'c6821f080280ab7d2121a928da4dffcdAAQIv81sMWIl8Xy1pT7m1dxLLBxVb/eM6FQwktTXwTdFfoL8zEenai8vrkq96Gs5kDaZn6cBnTmPACR/39ybyXpVsQy9cZas5UwnDhQP6d175n9glUxu+/fXq4l0c1xobRS6nysMGppOa6z4LF/mlSbUM3mGYCktIla2xD9jG8SlLacfwzONaHrEObe0pvOTNVBILnVIdSRv3fs96cp9FIYA',
    'tfstk': 'g0Vif0AXRRksITrJXkl1ei64h3XdfFGjAodxDjnVLDoIDNaYujR4Drht3GaYxmoUmI7fCZg08V3Z7muVjkb0XrOxbcFxixr-_xwtDcnmirZlJgCRwPasGYSR2_pBecHoNKR2QnHeTqhm7lB25u4sGjSpJIWRZPZyFM1agj7nTq0qujJwgwYEkDRZuCu2Yw0jYjRZbq8FTquS0FR40y7nlDoqgAk17IougWNFYNHtJZqNp5giI0zZbrUYTW--qPoHgIoISAYT7DA2gW2p1uDSbTTKcfn_5VqfNCGZn-PtT5SFgby7xSDrZtQsa5a4F-zBjZmaJlNo_7jM62HmjJPZKERqTXeZU-qGjdiaBkDS8v8cN2E-YPNaKZtU7uni_2kdaa4E3JFsF5Iesby7Wfe44Mptb80V4vveUq3kG27YTK9jQ2gn24p05C7uuJrh-wv5CAuIWgQh-K9jQ2gn2wbHFhMZRVIR.',
    'isg': 'BEZGJmMYXYZTYAlnIbCln9QhlzzIp4ph1wwmIjBvR2lEM-dNmDVTcdeFC2f_nYJ5',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'origin': 'https://pan.quark.cn',
    'priority': 'u=1, i',
    'referer': 'https://pan.quark.cn/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'b-user-id=b8a42176-40fd-5879-b419-a3d935be7373; __sdid=AAQ5KOGTtXKBPSQyfGVieZ5QNL5m1w4ipbkylP+FZFySjv957P0rhPjuypDXZwtcmrM=; _UP_D_=pc; _UP_A4A_11_=wb9c71a3a3504e4090f90f63bec53423; _UP_30C_6A_=st9c762011ahnlbw9wl7emctjt8ep97q; _UP_TS_=sg187851d9ee426f90755fe10ce41ada8c2; _UP_E37_B7_=sg187851d9ee426f90755fe10ce41ada8c2; _UP_TG_=st9c762011ahnlbw9wl7emctjt8ep97q; _UP_335_2B_=1; __pus=e8bb58570af87a08420e204e98d3f1f8AARaagBLQw92PjdcUQmHbUv37mB3g+GAj95G6aWBaJJREdN+W7JcgzVy+jVhssVCOeWnJNlVCzYM5OIIf2wiaDWu; __kp=178c31a0-ffb2-11ef-9f92-e3ac45c550f8; __kps=AARs6S/YJ9wh/9lAN2SAzsS5; __ktd=jgKxlToza7NJnev+8RWDIg==; __uid=AARs6S/YJ9wh/9lAN2SAzsS5; xlly_s=1; __puus=c6821f080280ab7d2121a928da4dffcdAAQIv81sMWIl8Xy1pT7m1dxLLBxVb/eM6FQwktTXwTdFfoL8zEenai8vrkq96Gs5kDaZn6cBnTmPACR/39ybyXpVsQy9cZas5UwnDhQP6d175n9glUxu+/fXq4l0c1xobRS6nysMGppOa6z4LF/mlSbUM3mGYCktIla2xD9jG8SlLacfwzONaHrEObe0pvOTNVBILnVIdSRv3fs96cp9FIYA; tfstk=g0Vif0AXRRksITrJXkl1ei64h3XdfFGjAodxDjnVLDoIDNaYujR4Drht3GaYxmoUmI7fCZg08V3Z7muVjkb0XrOxbcFxixr-_xwtDcnmirZlJgCRwPasGYSR2_pBecHoNKR2QnHeTqhm7lB25u4sGjSpJIWRZPZyFM1agj7nTq0qujJwgwYEkDRZuCu2Yw0jYjRZbq8FTquS0FR40y7nlDoqgAk17IougWNFYNHtJZqNp5giI0zZbrUYTW--qPoHgIoISAYT7DA2gW2p1uDSbTTKcfn_5VqfNCGZn-PtT5SFgby7xSDrZtQsa5a4F-zBjZmaJlNo_7jM62HmjJPZKERqTXeZU-qGjdiaBkDS8v8cN2E-YPNaKZtU7uni_2kdaa4E3JFsF5Iesby7Wfe44Mptb80V4vveUq3kG27YTK9jQ2gn24p05C7uuJrh-wv5CAuIWgQh-K9jQ2gn2wbHFhMZRVIR.; isg=BEZGJmMYXYZTYAlnIbCln9QhlzzIp4ph1wwmIjBvR2lEM-dNmDVTcdeFC2f_nYJ5',
}

params = {
    'pr': 'ucpro',
    'fr': 'pc',
    'uc_param_str': '',
    'task_id': 'bc59980ee5444ef686b373bddc1f5133',
    'retry_index': '0',
    '__dt': '114072',
    '__t': '1742200635841',
}

response = requests.get('https://drive-pc.quark.cn/1/clouddrive/task', params=params, cookies=cookies)
print(response.json())