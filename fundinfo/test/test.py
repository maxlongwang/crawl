import requests

cookies = {
    'bdshare_ty': '0x18',
    'Hm_lvt_0d970a9fc90ae6afd489296b16fa5a10': '1741830136',
    'HMACCOUNT': '13962BE667AE1583',
    'Hm_lpvt_0d970a9fc90ae6afd489296b16fa5a10': '1742190479',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://www.xmwav.com/mscdetail/149319.html',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'bdshare_ty=0x18; Hm_lvt_0d970a9fc90ae6afd489296b16fa5a10=1741830136; HMACCOUNT=13962BE667AE1583; Hm_lpvt_0d970a9fc90ae6afd489296b16fa5a10=1742190479',
}

response = requests.get('https://www.xmwav.com/download/rmk14931919327.html', cookies=cookies, headers=headers)
print(response.text)