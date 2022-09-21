'''
京喜拼拼小程序
https://api.m.jd.com/jxpp.picksite.queryOpenCityList?appid=jxpp_miniprogram&functionId=jxpp.picksite.queryOpenCityList&body=body={"longitude":116.397849,"latitude":39.903776,"time":1610101416468,"signStr":"89fea70ebbef1405a9703da9580c1b4a"}
加密：signStr
'''
import execjs

import time

# 通过compile命令转成一个js对象
docjs = execjs.compile(open(r"./jingxi_sign.js", "r", encoding="utf-8").read())


def jinxi_body(body):
    # 调用function方法
    signStr = docjs.call("jingxi_sign", body)
    print(signStr)


if __name__ == '__main__':
    now_t = int(time.time() * 1000)
    body = {
        "longitude": 116.397849,
        "latitude": 39.903776,
        "searchKey": "",
        "cityName": "",
        "queryType": 2,
        "pageSize": 10,
        "pageNo": 1,
        "time": now_t,
    }
    # // "signStr": "89fea70ebbef1405a9703da9580c1b4a"
    body = jinxi_body(body)
