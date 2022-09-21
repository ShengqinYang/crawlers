import frida
import sys
import time
import json
import gzip
import requests
from Crypto.Cipher import AES
import base64


# def on_message(message, data):
#     print("[%s] => %s" % (message, data))
#
#
# def start_hook():
#     device = frida.get_remote_device()
#     app_package_name = "com.dianping.v1"
#     session = device.attach(app_package_name)
#     with open("dp_Capture.js", "r", encoding="utf-8") as file:
#         js_code = file.read()
#     script = session.create_script(js_code)
#     script.on('message', on_message)
#     script.load()
#     return script


key = bytes([68, 55, 67, 54, 70, 55, 49, 65, 49, 50, 49, 53, 51, 69, 69, 53])
iv = bytes([53, 53, 67, 57, 51, 48, 68, 56, 50, 55, 66, 68, 65, 66, 70, 68])


# script = start_hook()

def decrypt_aes(key, iv, content):
    generator = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    # padded = pad_bytes(content)
    decrypt = generator.decrypt(content)
    return decrypt


def decode_aes(content, model):
    aes_data = decrypt_aes(key=key, iv=iv, content=content)
    ungzip_data = gzip.decompress(aes_data)
    bytes_list = list()
    # for b in ungzip_data:
    #     bytes_list.append(int(b))
    # res = script.exports.decode(model,bytes_list)

    res = decode_for_android(model, ungzip_data)
    return res


def decode_for_android(model, bytes_list):
    url = 'http://10.100.22.130:10086/d_p_decode'
    params = {
        'model': model,
        'byte_64': str(base64.b64encode(bytes_list), encoding='utf-8')
    }
    res = requests.post(url, data=params)
    return res.json()


if __name__ == "__main__":
    # url = 'https://apimeishi.meituan.com/meishi/selectlist/meishifilterlist.bin'
    url = 'https://mapi.dianping.com/mapi/searchshop.api'
    headers = {
        'pragma-os': 'MApi 1.4 (com.dianping.v1 10.38.13 om_sd_sgsztc17 MI_5; Android 9)',
        'User-Agent': 'MApi 1.4 (com.dianping.v1 10.38.13 om_sd_sgsztc17 MI_5; Android 9)',
        'pragma-dpid': 'c2388c0a879e439aa433071560edf303a160866520179041367'
        # 'c2388c0a879e439aa433071560edf303a160866520179041367'
    }
    # params = {
    #     'lastshopids': '',
    #     'parentcategoryid': '0',
    #     'categoryid': '10',
    #     'sortid': '1',
    #     'mylat': '0.0',
    #     'mylng': '0.0',
    #     'maptype': '0',
    #     'cityid': '1',
    #     'nettype': 'wifi',
    #     'phoneresolution': '1920_1080',
    #     'phonecarrier': 'unknown',
    #     'selectlocal': 'false',
    #     'start': '0',
    #     'smarttagslength': '19',
    #     'userid': '0',
    #     'phonemodel': 'xiaomi_mi 5',
    #     'lastshopuuids': '',
    #     'pageType': 'list',
    #     'connectwifiname': '<unknown ssid>',
    #     'scanwifiname': '<unknown ssid>',
    # }
    # params = {"start": "40",
    #           "keyword": "星巴克",
    #           "myLng": "0.0",
    #           "mylat": "0.0",
    #           "sortid": "0",
    #           "regionid": "0",
    #           "cityid": "1",
    #           "regiontype": "0",
    #           # "parentregionid": "-10000",
    #           "attributes": "",
    #           "disablerewrite": "0",
    #           "ganextindex": "40",
    #           # "requestuuid": "c5cb0225-2b63-43b2-ad04-e64bc9548231",
    #           "requestuuid": "027e31dc-e400-4238-b151-d9ef4e2a464c",
    #           # "requestuuid": "2ff01fd0-41e3-4f86-a762-42fe6c7e5920",
    #           "devicelat": "0.0",
    #           "devicelng": "0.0",
    #           "keepcategory": "1",
    #           # "tabid": "-1",
    #           "charactercount": "18",
    #           "isresearch": "0",
    #           "istravelsearch": "0",
    #           "noprofile": "0",
    #           "inputtext": "星巴克"
    #           }
    params = {"start": "0",
              "keyword": "好利来",
              "myLng": "0.0",
              "mylat": "0.0",
              "categoryid": "117",
              "regionid": "0",
              "cityid": "2",
              "regiontype": "0",
              "parentregionid": "-10000",
              "parentcategoryid": "10",
              "attributes": "",
              "disablerewrite": "0",
              "ganextindex": "0",
              "requestuuid": "0c6f186a-2ba0-4015-87f0-50aee96b7b81",
              "devicelat": "0.0",
              "devicelng": "0.0",
              "keepcategory": "1",
              "tabid": "-1",
              "charactercount": "18",
              "isresearch": "0",
              "istravelsearch": "0",
              "noprofile": "0"}

    r = requests.get(url, params=params, headers=headers, verify=False, timeout=10.0)
    # print(r.content)
    # result = decode_aes(r.content, 'com.dianping.model.MeishiPoiListResult')
    result = decode_aes(r.content, 'com.dianping.model.SearchShopApiResult')
    print(result, type(result))