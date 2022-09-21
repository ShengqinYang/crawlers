import random
import frida
import sys
import time
import json

import requests


def on_message(message, data):
    print("[%s] => %s" % (message, data))


def start_hook():
    device = frida.get_remote_device()
    print(device)

    # 应用包名
    app_package_name = "com.qidian_app.QDReader"  # 起点
    try:
        # pid = device.spawn([app_package_name])
        # device.resume(pid)
        # time.sleep(1)  # 2
        session = device.attach(app_package_name)
        # session = device.attach(target=16803)
        print("[*] start hook")
        print(session)

        # 加载脚本
        with open("hook_qidian.js", "r", encoding="utf-8") as file:
            js_code = file.read()

        script = session.create_script(js_code)
        script.on('message', on_message)
        script.load()
        sys.stdin.read()  # 等待程序触发,调试时打开
        # return script
    except frida.NotSupportedError:
        print("请检查包名的有效性.")


def get_header(qidian_url, method):
    '''
    该方法为firda hook，需要手机上的frida server一直跑着
    :param qidian_url:
    :param method: 一般为GET
    :return:
    '''
    script = start_hook()
    signinfo = script.exports.myfunc(qidian_url, method, None)

    header = {
        "Cache-Control": "no-cache, max-stale=0",
        "User-Agent": signinfo.get('User-Agent'),
        "Cookie": signinfo.get('Cookie'),
        "QDInfo": signinfo.get('QDInfo'),
        "QDSign": signinfo.get('QDSign'),
        'AegisSign': signinfo.get('AegisSign'),
        "Accept-Encoding": "gzip",
    }
    return header


if __name__ == '__main__':
    qidian_url = "https://druidv6.if.qidian.com/argus/api/v1/bookstore/getbooks?pageIndex=1&pageSize=20&siteId=12&filters=&order=11"
    method = "GET"
    header = get_header(qidian_url, method)

    # res = requests.get(qidian_url, headers=header, verify=False, timeout=30)
    # book_info = res.json()
    # print(book_info)
