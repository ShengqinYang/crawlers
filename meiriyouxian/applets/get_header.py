import sys

sys.path.append('.')
import execjs

# 通过compile命令转成一个js对象
docjs = execjs.compile(open(r"./models/meiriyouxian/getmfsig.js", "r", encoding="utf-8").read())


def get_headers(body, url):
    # 调用function方法
    mfsig = docjs.call("getmfsig", body, url)
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "content-type": "application/json",
        "mfsig": "mfsw" + mfsig,
        "platform": "weixin_app",
        "Accept-Encoding": 'gzip',
    }
    return headers
