import frida
import time
import hashlib
import requests
from urllib.parse import urlencode, quote, unquote


def on_message(message, data):
    print("[%s] => %s" % (message, data))


def start_hook():
    device = frida.get_remote_device()
    print(device)

    # 应用包名
    app_package_name = "com.luojilab.player"  # dedao
    try:
        # pid = device.spawn([app_package_name])
        # device.resume(pid)
        # time.sleep(1)  # 2
        session = device.attach(app_package_name)
        # session = device.attach(target=16803)
        print("[*] start hook")
        print(session)

        # 加载脚本
        with open("test.js", "r", encoding="utf-8") as file:
            # with open("hook_dedao.js", "r", encoding="utf-8") as file:
            js_code = file.read()

        script = session.create_script(js_code)
        script.on('message', on_message)
        script.load()
        # sys.stdin.read()  # 等待程序触发,调试时打开
        # print('script', script)
        return script
    except frida.NotSupportedError:
        print("请检查包名的有效性.")


def get_header(args5, args6, args9, d, ns, token):
    '''
    该方法为firda hook，需要手机上的frida server一直跑着
    :param qidian_url:
    :param method: 一般为GET
    :return:
    '''
    args1 = "/label/navigation/content"
    args2 = "POST"
    args3 = ""
    args4 = "application/x-www-form-urlencoded"
    # args5 = "page_id=0&result_type=0&product_type=2&navigation_id=61&h=%7B%22u%22%3A%22267241698%22%2C%22thumb%22%3A%22xl%22%2C%22dt%22%3A%22phone%22%2C%22ov%22%3A%229%22%2C%22net%22%3A%22wifi%22%2C%22os%22%3A%22ANDROID%22%2C%22d%22%3A%2207eb81a017fe33d5%22%2C%22dv%22%3A%22MI%205%22%2C%22t%22%3A%22json%22%2C%22chil%22%3A%221%22%2C%22v%22%3A%222%22%2C%22av%22%3A%228.5.0%22%2C%22scr%22%3A%223.0%22%2C%22adv%22%3A%221%22%2C%22ts%22%3A%221600679506%22%2C%22s%22%3A%227fdcab3b5d99f1d8%22%2C%22seid%22%3A%2207eb81a017fe33d5%22%7D&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61"

    # args8 = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzI3MDQyNSwiaWF0IjoxNjAwNjc4NDI1LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNjc4NDI1LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.BlHdE91DxtsuUxjlDApbr9ArVB_Rb55vqZUCw5Nn7kFUpgEV1nKAEbkKWYu8Wzgucxvj6AVB-aGnkGsDH6j9PA"
    args8 = token
    # args9 = 267241698
    args = "android" + str(args9) + d + ns  # 纳秒
    # print(args)
    # args = "android26724169807eb81a017fe33d51600741335863898565"
    args7 = hashlib.md5(args.encode()).hexdigest()
    script = start_hook()
    signinfo = script.exports.myfunc(args1, args2, args3, args4, args5, str(args6), args7, args8, args9)
    # print(signinfo)
    # print("G-Auth-Ts", args6, "G-Auth-Nonce", args7, signinfo)

    header = {
        "Xi-App-Key": "android-8.5.0",
        "Xi-Uid": "267241698",
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
        "Xi-Scr": "3.0",
        "Xi-Adv": "1",
        "Xi-Seid": "07eb81a017fe33d5",
        "G-Auth-Sign": signinfo['G-Auth-Sign'],
        "G-Auth-Nonce": args7,
        "G-Auth-Ts": args6,
        "G-Auth-Appid": "463ceba202a9f6f9ac4cd98d0f2f2876204ea85c",
        "G-Auth-Token": args8,
        "Host": "entree-ali.igetget.com",
        "X-Parent-Id": "0",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "okhttp/3.12.1",
    }
    return header


# def get_header(args1, args2, args3, args4, args5, args6, args7, args8, args9:
#     '''
#     该方法为firda hook，需要手机上的frida server一直跑着
#     :param qidian_url:
#     :param method: 一般为GET
#     :return:
#     '''
#     args1 = "/label/navigation/content"
#     args2 = "POST"
#     args3 = ""
#     args4 = "application/x-www-form-urlencoded"
#     # args5 = "page_id=0&result_type=0&product_type=2&navigation_id=61&h=%7B%22u%22%3A%22267241698%22%2C%22thumb%22%3A%22xl%22%2C%22dt%22%3A%22phone%22%2C%22ov%22%3A%229%22%2C%22net%22%3A%22wifi%22%2C%22os%22%3A%22ANDROID%22%2C%22d%22%3A%2207eb81a017fe33d5%22%2C%22dv%22%3A%22MI%205%22%2C%22t%22%3A%22json%22%2C%22chil%22%3A%221%22%2C%22v%22%3A%222%22%2C%22av%22%3A%228.5.0%22%2C%22scr%22%3A%223.0%22%2C%22adv%22%3A%221%22%2C%22ts%22%3A%221600679506%22%2C%22s%22%3A%227fdcab3b5d99f1d8%22%2C%22seid%22%3A%2207eb81a017fe33d5%22%7D&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61"
#
#     args8 = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzI3MDQyNSwiaWF0IjoxNjAwNjc4NDI1LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNjc4NDI1LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.BlHdE91DxtsuUxjlDApbr9ArVB_Rb55vqZUCw5Nn7kFUpgEV1nKAEbkKWYu8Wzgucxvj6AVB-aGnkGsDH6j9PA"
#     # args9 = 267241698
#     args = "android" + str(args9) + d + ns  # 纳秒
#     print(args)
#     # args = "android26724169807eb81a017fe33d51600741335863898565"
#     args7 = hashlib.md5(args.encode()).hexdigest()
#     script = start_hook()
#     signinfo = script.exports.myfunc(args1, args2, args3, args4, args5, str(args6), args7, args8, args9)
#     print(signinfo)
#     # print("G-Auth-Ts", args6, "G-Auth-Nonce", args7, signinfo)
#
#     header = {
#         "Xi-App-Key": "android-8.5.0",
#         "Xi-Uid": "267241698",
#         "Xi-Thumb": "xl",
#         "Xi-Dt": "phone",
#         "Xi-Ov": "9",
#         "Xi-Net": "wifi",
#         "Xi-Os": "ANDROID",
#         "Xi-D": "07eb81a017fe33d5",
#         "Xi-Dv": "MI 5",
#         "Xi-T": "json",
#         "Xi-Chil": "1",
#         "Xi-V": "2",
#         "Xi-Av": "8.5.0",
#         "Xi-Scr": "3.0",
#         "Xi-Adv": "1",
#         "Xi-Seid": "07eb81a017fe33d5",
#         "G-Auth-Sign": signinfo['G-Auth-Sign'],
#         "G-Auth-Nonce": args7,
#         "G-Auth-Ts": args6,
#         "G-Auth-Appid": "463ceba202a9f6f9ac4cd98d0f2f2876204ea85c",
#         "G-Auth-Token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzI1OTkyMSwiaWF0IjoxNjAwNjY3OTIxLCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNjY3OTIxLCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.O3Waka6SOxqfRp0bMn5zx6HehgcHys3BkxWXQpLm3Di2mAPhcz_AN2adMDYrxdDjukrVHctUTQifgjLRz5JvvQ",
#         "Host": "entree-ali.igetget.com",
#         # "X-Span-Id": "6849849267206787385",
#         # "X-Trace-Id": "1801177121047302742",
#         "X-Parent-Id": "0",
#         "Content-Type": "application/x-www-form-urlencoded",
#         # "Content-Length": "583",
#         # "Connection": "Keep-Alive",
#         # "Accept-Encoding": "gzip",
#         "User-Agent": "okhttp/3.12.1",
#     }
#     # print(header)
#     return header

def token(Sign, Nonce, Ts):
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
        # "G-Auth-Sign": Sign,
        # "G-Auth-Nonce": Nonce,
        # "G-Auth-Ts": Ts,
        "Host": "entree.igetget.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "okhttp/3.12.1"
    }

    url = "https://entree.igetget.com/ddab/v1/init"
    res = requests.post(url=url, headers=header, verify=False, timeout=30)
    token = res.headers.get('G-Auth-Token')
    print(res.headers.get('G-Auth-Token'))
    # print(res.headers.get('G-Auth-Expire-At'))
    return token


def get_list(token):
    t = time.time()
    ns = str(round(t * 1000000000))  # 时间戳，纳秒
    args6 = str(int(t))  # 时间戳，毫秒
    args9 = 267241698  # 固定值
    d = str("07eb81a017fe33d5")  # 固定值
    values = '{"u":"%s","thumb":"xl","dt":"phone","ov":"9","net":"wifi","os":"ANDROID","d":"%s","dv":"MI 5","t":"json","chil":"1","v":"2","av":"8.5.0","scr":"3.0","adv":"1","ts":"%s","s":"7fdcab3b5d99f1d8","seid":"%s"}' % (
        args9, d, args6, d)

    args5 = "page_id=0&result_type=0&product_type=2&navigation_id=61&h=" + quote(
        values) + "&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61"

    url = "https://entree-ali.igetget.com/label/navigation/content"
    res = requests.post(url=url, data=args5, headers=get_header(args5, args6, args9, d, ns, token), verify=False,
                        timeout=30)
    book_info = res.text
    print(book_info)


if __name__ == '__main__':
    token = token(Sign='', Nonce='', Ts='')
    get_list(token)

# if __name__ == '__main__':
#     # qidian_url = "https://druidv6.if.qidian.com/argus/api/v1/bookstore/getbooks?pageIndex=1&pageSize=20&siteId=12&filters=&order=11"
#     # method = "GET"
#     # header = get_header(qidian_url, method)
#
#     # res = requests.get(qidian_url, headers=header, verify=False, timeout=30)
#     # book_info = res.json()
#     # print(book_info)
#
#     # //参数1 /label/navigation/content
#     # // 参数2 POST
#     # // 参数3
#     # // 参数4 application/x-www-form-urlencoded
#     # // 参数5 page_id=0&result_type=0&product_type=2&navigation_id=61&h=%7B%22u%22%3A%22267241698%22%2C%22thumb%22%3A%22xl%22%2C%22dt%22%3A%22phone%22%2C%22ov%22%3A%229%22%2C%22net%22%3A%22wifi%22%2C%22os%22%3A%22ANDROID%22%2C%22d%22%3A%2207eb81a017fe33d5%22%2C%22dv%22%3A%22MI%205%22%2C%22t%22%3A%22json%22%2C%22chil%22%3A%221%22%2C%22v%22%3A%222%22%2C%22av%22%3A%228.5.0%22%2C%22scr%22%3A%223.0%22%2C%22adv%22%3A%221%22%2C%22ts%22%3A%221600679506%22%2C%22s%22%3A%227fdcab3b5d99f1d8%22%2C%22seid%22%3A%2207eb81a017fe33d5%22%7D&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61
#     #
#     # // 参数6 1600679506 --G-Auth-Ts 时间戳 2020-09-21 17:11:46
#     # // 参数7 13a7105f62c650eaada4e9795a3c5c96  --G-Auth-Nonce
#     # // --  G-Auth-Token
#     # // 参数8 eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzI3MDQyNSwiaWF0IjoxNjAwNjc4NDI1LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNjc4NDI1LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.BlHdE91DxtsuUxjlDApbr9ArVB_Rb55vqZUCw5Nn7kFUpgEV1nKAEbkKWYu8Wzgucxvj6AVB-aGnkGsDH6j9PA
#     # // 参数9 267241698  --userid u 固定值
#     # // 结果 cf4338503bfa49e0902fa4ca7c6159b08c386749   --G-Auth-Sign
#     t = time.time()
#     args1 = "/label/navigation/content"
#     args2 = "POST"
#     args3 = ""
#     args4 = "application/x-www-form-urlencoded"
#     args5 = "page_id=0&result_type=0&product_type=2&navigation_id=61&h=%7B%22u%22%3A%22267241698%22%2C%22thumb%22%3A%22xl%22%2C%22dt%22%3A%22phone%22%2C%22ov%22%3A%229%22%2C%22net%22%3A%22wifi%22%2C%22os%22%3A%22ANDROID%22%2C%22d%22%3A%2207eb81a017fe33d5%22%2C%22dv%22%3A%22MI%205%22%2C%22t%22%3A%22json%22%2C%22chil%22%3A%221%22%2C%22v%22%3A%222%22%2C%22av%22%3A%228.5.0%22%2C%22scr%22%3A%223.0%22%2C%22adv%22%3A%221%22%2C%22ts%22%3A%221600679506%22%2C%22s%22%3A%227fdcab3b5d99f1d8%22%2C%22seid%22%3A%2207eb81a017fe33d5%22%7D&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61"
#     args6 = str(int(t))
#     args8 = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzI3MDQyNSwiaWF0IjoxNjAwNjc4NDI1LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNjc4NDI1LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.BlHdE91DxtsuUxjlDApbr9ArVB_Rb55vqZUCw5Nn7kFUpgEV1nKAEbkKWYu8Wzgucxvj6AVB-aGnkGsDH6j9PA"
#     args9 = 267241698
#     args = "android" + str(args9) + "07eb81a017fe33d5" + str(round(t * 1000000000))  # 纳秒
#     # print(args)
#     # args = "android26724169807eb81a017fe33d51600741335863898565"
#     args7 = hashlib.md5(args.encode()).hexdigest()
#     script = start_hook()
#     signinfo = script.exports.myfunc(args1, args2, args3, args4, args5, args6, args7, args8, args9)
#     print(signinfo)
#
#     # args1 = "/label/navigation/content"
#     # args2 = "POST"
#     # args3 = ""
#     # args4 = "application/x-www-form-urlencoded"
#     # args5 = "page_id=0&result_type=0&product_type=2&navigation_id=61&h=%7B%22u%22%3A%22267241698%22%2C%22thumb%22%3A%22xl%22%2C%22dt%22%3A%22phone%22%2C%22ov%22%3A%229%22%2C%22net%22%3A%22wifi%22%2C%22os%22%3A%22ANDROID%22%2C%22d%22%3A%2207eb81a017fe33d5%22%2C%22dv%22%3A%22MI%205%22%2C%22t%22%3A%22json%22%2C%22chil%22%3A%221%22%2C%22v%22%3A%222%22%2C%22av%22%3A%228.5.0%22%2C%22scr%22%3A%223.0%22%2C%22adv%22%3A%221%22%2C%22ts%22%3A%221600749444%22%2C%22s%22%3A%227fdcab3b5d99f1d8%22%2C%22seid%22%3A%2207eb81a017fe33d5%22%7D&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61"
#     # args6 = "1600749444"
#     # args8 = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzM0MTQxOSwiaWF0IjoxNjAwNzQ5NDE5LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNzQ5NDE5LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.O3Waka6SOxqfRp0bMn5zx6HehgcHys3BkxWXQpLm3Di2mAPhcz_AN2adMDYrxdDjukrVHctUTQifgjLRz5JvvQ"
#     # args9 = 267241698
#     # args7 = "58b59435cdac7d4738df8f5b7739424f"
