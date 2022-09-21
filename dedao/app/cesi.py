from urllib.parse import quote

import requests
import time

header = {
    "Xi-App-Key": "android-8.5.0",
    "Xi-Uid": "0",
    "Xi-Thumb": "xl",
    "Xi-Dt": "phone",
    "Xi-Ov": "9",
    "Xi-Net": "wifi",
    "Xi-Os": "ANDROID",
    "Xi-D": "07eb81a017fe33d5",
    "Xi-Dv": "MI 5",
    "Xi-T": "json",
    "Xi-Chil": "1",
    "Xi-V": "2",
    "Xi-Av": "8.5.0",
    "Xi-Scr": "0",
    "Xi-Adv": "1",
    "Xi-Seid": "07eb81a017fe33d5",
    # "G-Auth-Sign": "56490fa7fd45a9a5be166ca23e911814a72cab71",
    # "G-Auth-Nonce": "fad188e35b8267707b95f1a01f8b23e3",
    # "G-Auth-Ts": "1600759297",
    "Host": "entree.igetget.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "okhttp/3.12.1", }

# headers = get_header(args5, args6, args9, d, ns)
now_t = time.time()
# ts = str(int(now_t))  # 时间戳，毫秒
ts = str("1600759297")
url = "https://entree.igetget.com/ddab/v1/init"
# args5 = "h=" + "%7B%22u%22%3A%220%22%2C%22thumb%22%3A%22xl%22%2C%22dt%22%3A%22phone%22%2C%22ov%22%3A%229%22%2C%22net%22%3A%22wifi%22%2C%22os%22%3A%22ANDROID%22%2C%22d%22%3A%2207eb81a017fe33d5%22%2C%22dv%22%3A%22MI%205%22%2C%22t%22%3A%22json%22%2C%22chil%22%3A%221%22%2C%22v%22%3A%222%22%2C%22av%22%3A%228.5.0%22%2C%22scr%22%3A%220%22%2C%22adv%22%3A%221%22%2C%22ts%22%3A%221600759297%22%2C%22s%22%3A%2221a6273d2dc033e8%22%2C%22seid%22%3A%2207eb81a017fe33d5%22%7D"

# ARGS5 = '{"u":"0","thumb":"xl","dt":"phone","ov":"9","net":"wifi","os":"ANDROID","d":"07eb81a017fe33d5","dv":"MI 5","t":"json","chil":"1","v":"2","av":"8.5.0","scr":"0","adv":"1","ts":"%s","s":"21a6273d2dc033e8","seid":"07eb81a017fe33d5"}' % ts
# args5 = "h=" + quote(ARGS5)
# print(args5)
# header = get_header()


res = requests.post(url=url, headers=header, verify=False, timeout=30)
print(res.headers.get('G-Auth-Token'))
print(res.headers.get('G-Auth-Expire-At'))
print(int(time.time()))

# {'Date': 'Tue, 22 Sep 2020 07:48:26 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '367', 'Connection': 'keep-alive', 'Set-Cookie': 'aliyungf_tc=AQAAANUWfDtPIwoA4gp+fKP5pawiGsbk; Path=/; HttpOnly, acw_tc=2f624a3316007609066655889e7e3778bb4d1b5ccd5d377b6b65fb8d8f754a;path=/;HttpOnly;Max-Age=1800, ISID=ae4309c22cb0580bbcbcdfb79eb7f855; Path=/; Domain=igetget.com; Max-Age=31536000; HttpOnly', 'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': '*', 'Access-Control-Allow-Origin': '*', 'G-Auth-Expire-At': '1603352906', 'G-Auth-Token': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzM1MjkwNiwiaWF0IjoxNjAwNzYwOTA2LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNzYwOTA2LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.iOkexj6wn8dKt_A1Yi2yfCFgC8FRMxx3R3aKHrG6glimzeuFPZzVe00UL4_DOkuRBrLW9D5y3CydwRyTEfJzIw', 'G-Client-Ip': '124.126.10.226', 'G-Powered-By': 'ddgw/1.11.5', 'G-Timestamp': '1600760906', 'Vary': 'Accept-Encoding', 'X-Uid': '267241698', 'Xi-Uid': '267241698'}
# 'G-Auth-Token': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzM1MjkwNiwiaWF0IjoxNjAwNzYwOTA2LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNzYwOTA2LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.iOkexj6wn8dKt_A1Yi2yfCFgC8FRMxx3R3aKHrG6glimzeuFPZzVe00UL4_DOkuRBrLW9D5y3CydwRyTEfJzIw'
