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
        session = device.attach(app_package_name)
        print("[*] start hook")
        print(session)

        # 加载脚本
        with open("hook_dedao.js", "r", encoding="utf-8") as file:
            js_code = file.read()

        script = session.create_script(js_code)
        script.on('message', on_message)
        script.load()
        # sys.stdin.read()  # 等待程序触发,调试时打开

        return script
    except frida.NotSupportedError:
        print("请检查包名的有效性.")


def get_header(args1, args2, args3, args5, args6, args9, d, ns, token):
    '''

    :param args1: "/label/navigation/content" url
    :param args2: "POST"
    :param args3: ""
    :param args5:
    :param args6:
    :param args9:
    :param d:
    :param ns:
    :param token:
    :return:
    '''
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
    args8 = token
    args = "android" + str(args9) + d + ns  # 纳秒
    args7 = hashlib.md5(args.encode()).hexdigest()
    script = start_hook()
    signinfo = script.exports.myfunc(args1, args2, args3, args4, args5, str(args6), args7, args8, args9)
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


def token():
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
        "Host": "entree.igetget.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "okhttp/3.12.1"
    }

    url = "https://entree.igetget.com/ddab/v1/init"
    res = requests.post(url=url, headers=header, verify=False, timeout=30)
    token = res.headers.get('G-Auth-Token')
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
