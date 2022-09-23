# 使用opencv进行知乎的滑动验证识别并模拟登录
import base64
import datetime
import json
import logging
import math
import os
import random
import time
from io import BytesIO

import cv2
import numpy as np
import requests
import undetected_chromedriver as uc
from PIL import Image
from matplotlib import pyplot as plt
from retrying import retry
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait


from mysqlservice import MySQLConnection

"""
pip 安装 undetected_chromedriver包，可绕过知乎对chromedriver识别的问题，
在undetected-chromedriver的过程中会自动下载chromerdriver且为最新版本，放在运行目录下，下次运行不会重复下载，
大家不用去主动下载chromedriver了，但要注意浏览器与 chromerdriver 版本匹配
"""


class SliderCode(object):
    """滑动验证识别"""

    def __init__(self, slider_ele=None, background_ele=None, count=1, save_image=False):
        '''
        :param slider_ele: 滑块元素
        :param background_ele: 背景图元素
        :param count:  验证重试次数
        :param save_image:  是否保存验证中产生的图片， 默认 不保存
        '''
        self.count = count
        self.save_images = save_image
        self.slider_ele = slider_ele
        self.background_ele = background_ele

    def get_slide_locus(self, distance):
        # 计算出一个滑动轨迹防止被识别出是机器行为
        distance += 8
        v = 0
        t = 0.3
        # 保存0.3内的位移
        tracks = []  # 存放每段移动的位移
        current = 0
        mid = distance * 4 / 5
        while current <= distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            s = v0 * t + 0.5 * a * (t ** 2)
            current += s
            tracks.append(round(s))
            v = v0 + a * t
        # 由于计算机计算的误差，导致模拟人类行为时，会出现分布移动总和大于真实距离，这里就把这个差添加到tracks中，也就是最后进行一步左移。
        # tracks.append(-(sum(tracks) - distance * 0.5))
        # tracks.append(10)
        return tracks

    def slide_verification(self, driver, slide_element, distance):
        '''
        :param driver: driver对象
        :param slide_element: 滑块元素
        :type   webelement
        :param distance: 滑动距离
        :return:+
        '''
        print('滑动距离是: ', distance)
        # 根据滑动的距离生成滑动轨迹
        locus = self.get_slide_locus(distance)
        print('生成的滑动轨迹为:{},轨迹的距离之和为{}'.format(locus, distance))
        # 按下鼠标左键
        ActionChains(driver).click_and_hold(slide_element).perform()
        time.sleep(0.5)
        # 遍历轨迹进行滑动
        for loc in locus:
            time.sleep(0.01)
            # 此处记得修改selenium的源码 selenium\webdriver\common\actions\pointer_input.py中将DEFAULT_MOVE_DURATION改为50，否则滑动很慢
            ActionChains(driver).move_by_offset(loc, random.randint(-5, 5)).perform()
            ActionChains(driver).context_click(slide_element)
        # 释放鼠标
        ActionChains(driver).release(on_element=slide_element).perform()

    def onload_save_img(self, url, filename="image.png"):
        '''
        下载图片并保存
        :param url: 图片网址
        :param filename: 图片名称
        :return:
        '''
        try:
            print(url)
            response = requests.get(url, verify=False)
            print(response)
        except Exception as e:
            print('图片下载失败')
            raise e
        else:
            with open(filename, 'wb') as f:
                f.write(response.content)

    def get_element_slide_distance(self, background_url, slider_url, correct=0):
        '''
        根据传入滑块， 和背景的节点， 计算滑块的距离
        :param background_url: 背景图的url
        :param slider_url: 滑块url
        :param correct:
        :return:
        '''
        # 下载验证码链接
        slider = 'slider.jpg'
        background = 'background.jpg'
        self.onload_save_img(slider_url, slider)
        self.onload_save_img(background_url, background)

        # 进行色度图片, 转化为numpy 中的数组类型数据
        slider_pic = cv2.imread(slider, 0)
        background_pic = cv2.imread(background, 0)

        # 获取缺口数组的形状
        width, height = slider_pic.shape[::-1]

        # 将处理之后的图片另存
        slider01 = 'slider01.jpg'
        slider02 = 'slider02.jpg'
        background01 = 'background01.jpg'

        cv2.imwrite(slider01, slider_pic)
        cv2.imwrite(background01, background_pic)

        # 读取另存的滑块
        slider_pic = cv2.imread(slider01)

        # 进行色彩转化
        slider_pic = cv2.cvtColor(slider_pic, cv2.COLOR_BGR2GRAY)

        # 获取色差的绝对值
        slider_pic = abs(255 - slider_pic)
        # 保存图片
        cv2.imwrite(slider02, slider_pic)
        # 读取滑块
        slider_pic = cv2.imread(slider02)

        # 读取背景图
        background_pic = cv2.imread(background01)
        time.sleep(3)

        # 比较两张图的重叠部分
        result = cv2.matchTemplate(slider_pic, background_pic, cv2.TM_CCOEFF_NORMED)

        # 通过数组运算，获取图片缺口位置
        top, left = np.unravel_index(result.argmax(), result.shape)

        # 背景图缺口坐标
        print('当前滑块缺口位置', (left, top, left + width, top + height))

        # 判读是否需求保存识别过程中的截图文件
        if self.save_images:
            loc = [(left + correct, top + correct), (left + width - correct, top + height - correct)]
            self.image_crop(background, loc)

        else:
            # 删除临时文件
            os.remove(slider01)
            os.remove(slider02)
            os.remove(background01)
            os.remove(background)
            os.remove(slider)
            print("临时图片文件已删除")

        # 返回需要移动的位置距离
        return left

    def image_crop(self, image, loc):
        cv2.rectangle(image, loc[0], loc[1], (7, 249, 151), 2)
        cv2.imshow('Show', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class ClickCode(object):
    # def __init__(self, yidun_bg_img=None):
    #     self.yidun_bg_img = yidun_bg_img

    def save_img(self, yidun_bg_img, driver, clip_img_name):
        locate = yidun_bg_img.location
        size = yidun_bg_img.size

        screenshot = driver.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        top, bottom, left, right = locate['y'], locate['y'] + size['height'], locate['x'], locate['x'] + size['width']
        img = screenshot.crop((left, top, right, bottom))
        img.save(clip_img_name)

    def click_locxy(self, dr, points, locate=None):
        '''
        dr:浏览器
        points: [[900.0, 360.0], [970.5, 355.75], [1022.0, 353.0]] 坐标点
        locate: 验证码元素对象
        '''
        action_chains = ActionChains(dr)
        action_chains.pause(2)
        for index, p in enumerate(points):
            action_chains.move_to_element_with_offset(locate, p[0], p[1]).pause(random.random())
            print(p[0], p[1], 'move_to_element_with_offset')
        action_chains.pause(random.random()).click().perform()

    @retry(stop_max_attempt_number=3)
    def base64_api(self, uname, pwd, img, typeid):
        '''
        对接图鉴打码平台
        :param uname: 平台用户名
        :param pwd: 平台密码
        :param img: 图片路径
        :param typeid: 打码类型id
        :return: [['135', '45'], ['218', '109'], ['81', '85']]
        '''
        with open(img, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            b64 = base64_data.decode()
        data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
        if result['success']:
            pic_str = result["data"]["result"].split('|')
            pic_str = [i.split(',') for i in pic_str]
            return pic_str
        else:
            raise Exception("获取图鉴打码平台坐标失败：", result["message"])


class GenerateCurve():
    '''根据两点坐标确定一条被瑟尔曲线'''

    def __init__(self, point0, point1, control_point=[], point_nums=random.randint(5, 15), debug=False):
        '''
        :param point0: 起点
        :param point1: 终点
        :param control_point: 控制点
        :param point_nums: 生成曲线坐标点的数量.数量越多图越凹凸不平，越少越平滑
        '''
        self.point0 = point0
        self.point1 = point1
        self.control_point = control_point
        self.point_nums = point_nums
        self.debug = debug

    def getBezierPoints(self):
        '''
        :return:
        '''
        if not self.point_nums:
            self.point_nums = random.randint(1, 6)
        pointList = []
        x1, y1 = int(self.point0[0]), int(self.point0[1])
        x2, y2 = int(self.point1[0]), int(self.point1[1])
        cx, cy = int(self.control_point[0]), int(self.control_point[1])
        for i in range(self.point_nums + 1):
            t = i / self.point_nums
            x = math.pow(1 - t, 2) * x1 + 2 * t * (1 - t) * cx + math.pow(t, 2) * x2
            y = math.pow(1 - t, 2) * y1 + 2 * t * (1 - t) * cy + math.pow(t, 2) * y2
            pointList.append([int(x), int(y)])
        return pointList

    def getControlPoint(self):
        '''
        :return: 控制点
        '''
        if self.control_point:
            return self.control_point

        x0, y0 = int(self.point0[0]), int(self.point0[1])
        x1, y1 = int(self.point1[0]), int(self.point1[1])

        abs_x = abs(x0 - x1) / 2  # 两点横坐标相减绝对值/2
        abs_y = abs(y0 - y1) / 2  # 两点横坐标相减绝对值/2
        # print(abs_y)
        ran_x = random.randint(0, int(abs_x))  # x取随机差值
        ran_y = random.randint(0, int(abs_y))  # y取随机差值

        # print(ran_x, ran_y)
        self.control_point.append((x0 + x1) / 2 + random.choice([-ran_x, +ran_x]))
        self.control_point.append((y0 + y1) / 2 + random.choice([-ran_y, +ran_y]))

    def showRoute(self, pointList):
        '''
        展示曲线走势
        :return:
        '''
        _xx = []
        _yy = []
        for p in pointList:
            _xx.append(p[0])
            _yy.append(p[1])
        plt.plot(_xx, _yy, color='gold', markerfacecolor='cyan', marker='o')  # 绘图
        for a, b in zip(_xx, _xx):  # 添加这个循环显示坐标
            plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)
        plt.show()
        plt.close()

    def main(self):
        self.getControlPoint()
        print(self.control_point)
        pointList = self.getBezierPoints()
        if self.debug == True:
            self.showRoute(pointList)
        return pointList


class Login(object):
    def __init__(self, user, password, account_id, account_type, retry=2):
        # path = "C:\Program Files\Google\Chrome\Application\driver\chromedriver.exe" # 线下测试改为自己的路径
        # uc.TARGET_VERSION = 103
        path = "/usr/bin/chromedriver"  # 指定线上路径,线上的chromedriver是87版本，浏览器也是87版本
        options = uc.ChromeOptions()
        options.add_argument('no-sandbox')
        options.headless = True
        uc.TARGET_VERSION = 87
        self.driver = uc.Chrome(options=options, executable_path=path)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.url = "https://www.zhihu.com/signin?next=https%3A%2F%2Faduser.zhihu.com%2Fchoose%2F%3Fnext%3Dhttps%253A%252F%252Fxg.zhihu.com%252Fhome"
        self.sli = SliderCode()
        self.cli = ClickCode()
        self.user = user
        self.password = password
        self.account_id = account_id
        self.account_type = account_type
        self.retry = retry  # 重试次数
        self.clip_img_name = "clip_img_name.png"
        self.tujian_name = "•••"  # 图鉴会员名
        self.tujian_pwd = "•••"  # 图鉴密码

    def slider_verification_code(self, yidun_bg_img_src, yidun_jigsaw_src):
        '''
        :param yidun_bg_img_src: 背景图的url
        :param yidun_jigsaw_src: 滑块url
        :return:
        '''
        # 获取验证码滑动距离
        distance = self.sli.get_element_slide_distance(yidun_bg_img_src, yidun_jigsaw_src)
        print('滑动距离是', distance)
        # 滑块对象
        element = self.driver.find_element_by_css_selector('.yidun_slider')
        # 滑动函数
        self.sli.slide_verification(self.driver, element, distance)

    @retry(stop_max_attempt_number=3, wait_random_min=100, wait_random_max=450)
    def login(self):
        '''
        登录主体
        :return: 登录后的cookies，登陆后的用户跳转页url（用于提取用户id）
        '''
        try:
            self.driver.get(self.url)  # 请求登录页面网址
            time.sleep(2)
            # 选择密码登录
            self.wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR, "div[class='SignFlow-tab']"))).click()
            # 输入账号
            username = self.wait.until(Ec.element_to_be_clickable((By.NAME, "username")))
            username.send_keys(self.user)
            time.sleep(random.random())
            # 输入密码
            password = self.wait.until(Ec.element_to_be_clickable((By.NAME, 'password')))
            password.send_keys(self.password)
            time.sleep(random.random())
            count = 1
            while count < self.retry:
                # 登录框
                submit = self.wait.until(Ec.element_to_be_clickable((By.CLASS_NAME, 'SignFlow-submitButton')))
                submit.click()  # 点击登录
                time.sleep(3)
                # 1.获取验证码背景大图
                yidun_bg_img = self.wait.until(
                    Ec.presence_of_element_located((By.CSS_SELECTOR, '.yidun_bgimg .yidun_bg-img')))
                yidun_bg_img_src = yidun_bg_img.get_attribute('src')

                # 2.获取验证码滑块
                yidun_jigsaw = self.wait.until(
                    Ec.presence_of_element_located((By.CSS_SELECTOR, '.yidun_bgimg .yidun_jigsaw')))
                yidun_jigsaw_src = yidun_jigsaw.get_attribute('src')

                if yidun_jigsaw_src:  # 如果滑块url存在就走滑动验证码方式
                    logging.info(f"知乎走滑块验证码，{datetime.datetime.now()}")
                    self.slider_verification_code(yidun_bg_img_src, yidun_jigsaw_src)  # 滑动验证码
                else:
                    # 3.获取验证码对象
                    placeholder = self.wait.until(
                        Ec.presence_of_element_located((By.CSS_SELECTOR, '.yidun_panel-placeholder')))
                    logging.info(f"知乎走点选验证码，{datetime.datetime.now()}")
                    self.click_verification_code(yidun_bg_img, placeholder)

                # 滑动之后的url链接
                time.sleep(random.randint(5, 10))
                # 检查是否登录成功
                try:
                    if "https://xg.zhihu.com" in self.driver.current_url:  # 登录成功
                        print("get_cookies")
                        return self.get_cookies()
                    else:
                        raise Exception("login failure~")
                except:
                    count += 1
                    logging.error(f"login retrying：{count}！！")
                    print(f"开始重试：{count}！！")
            return None
        except Exception as e:
            logging.error("login failure~，获取cookie失败~")
            return None

    def click_verification_code(self, yidun_bg_img, placeholder):
        '''点选验证码'''

        self.cli.save_img(yidun_bg_img, self.driver, clip_img_name=self.clip_img_name)
        pic_str = self.cli.base64_api(uname=self.tujian_name, pwd=self.tujian_pwd, img=self.clip_img_name, typeid=20)
        print(pic_str, "result")
        # 添加鼠标起始点 x=0~350, y=180~245
        start_point = [random.randint(0, 350), random.randint(180, 245)]
        pic_str.insert(0, start_point)
        for i in range(len(pic_str) - 1):
            p0, p1 = pic_str[i], pic_str[i + 1]  # 起点, 终点 = p0, p1
            print(p0, p1, 'p0, p1')
            gc = GenerateCurve(p0, p1)
            points = gc.main()
            print(points, 'points')
            self.cli.click_locxy(self.driver, points, placeholder)
        # 删除临时文件
        os.remove(self.clip_img_name)

    def get_cookies(self):
        '''
        登录成功后 保存账号的cookies
        :return:
        '''
        cookies = self.driver.get_cookies()
        cookies = [item["name"] + "=" + item["value"] for item in cookies]
        cookies = ';'.join(item for item in cookies)
        print(cookies, 'cookies')
        return cookies

    def __del__(self):
        self.driver.close()

    def main(self):
        cookie = self.login()
        if check_cookie(cookie, self.account_id, self.account_type):
            save_cookie(cookie, self.account_id)
            logging.info(f"{self.account_id}，cookie有效、保存成功~")
        else:
            logging.error(f"{self.account_id}，cookie无效、保存失败~")


def check_cookie(cookie, account_id, account_type, retry=3):
    '''检查cookie是否有效'''
    k = 1
    headers = {
        "host": 'xg.zhihu.com',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
        "Cookie": cookie
    }
    proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
    date_str = datetime.datetime.today().strftime("%Y-%m-%d")

    if account_type == '1':  # BM账户
        url = f"https://xg.zhihu.com/api/v1/agent/user?authority=advertiser,ka_advertiser&agentedBy={account_id}&perPage=10&page=1"
    else:
        url = f"https://xg.zhihu.com/api/v1/stat/overview?userId={account_id}&dataType=USER&groupUnit=BY_HOUR&&&stTms={date_str}&endTms={date_str}"
    print(account_id, account_type, type(account_type))
    while k < retry:
        try:
            res = requests.get(url=url, headers=headers, verify=False)
            res_json = res.json()
            return True
        except Exception as e:
            print(e)
            k += 1
    return False


def save_cookie(cookie, account_id):
    '''保存cookie'''
    with MySQLConnection(db_host='85') as conn:
        cur = conn.cursor()
        cookie_update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(
            f"UPDATE `zhihu`.`account_info` SET `cookie` = '{cookie}',`cookie_update_time`='{cookie_update_time}' WHERE `account_id`='{account_id}';")


if __name__ == "__main__":
    # 知乎实验账号
    # 账号：•••
    # 密码：•••
    # 网址：https://xg.zhihu.com/agent
    login = Login("username", "password", 523695, 1)
    login.main()
    print("sd")


    # c = """ll_b=t0Um9TX7vlX0fVd/E9zkGuX1h0j6BRom59k/adp9fwU=;KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1655106972|1655106969;z_c0=2|1:0|10:1655106968|4:z_c0|92:Mi4xckNUV053QUFBQUFBQUJJSmVSY1hGU1lBQUFCZ0FsVk5tRHVVWXdGTURYMmdoTDlyT2xCeEhnV2lxR2oybzY1Yml3|6ea46a6b902fc2269833a9085cb19f7667f74e4c05541b093bb5887aa743301d;captcha_session_v2=2|1:0|10:1655106913|18:captcha_session_v2|88:c3oyaGdnS1d1SWNRM3lCN2tJdk1kTDNIaEhaakg1R3BsZjZkdzI1VWFpZkQybFM1aVpoTGhXVjJPV2FnTnk2OQ==|3760a2a4532e2ea337fb1d0a0d52c683cbf2a65871f078a5eac3f9c9b53fe4b4;Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1655106911;d_c0="AAASCXkXFxWPTn6BBHkuGxNlGZeaz3d3Lgo=|1655106909";captcha_ticket_v2=2|1:0|10:1655106968|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfdUxCT1JmWWlqVmNqdjROeHFDQWx1N19jbjdhUGRZMTlkSHE2S2hDQkhwOGVqcXJDaFVTWGNrQlVVMHVPWC5DTWltNDFSc3U0RmpQV29OcENaZW11QmZ2QVF3T3puR2tJbzRXdTQxOHlkLks2YlBMekxiR3JNaUFDUkZ5VGZfajROT0FRUVlRZHRjVUxBOWRPWU1VMXI3Lkk3R0I0VlRGa0FUTjhET1B2WXVhS0l2MkNyaU80cWMxSktidmtONVl3TjRHX2pTeUl3S2cyTVB1S2JabUt2WGhvRzJEMW5VNTJhVFpXX1FJTmtWYlhYdVp1N3hnaS1acGo0TVFsZHNILkRXR0k0ZzQwYlpYcm5GYmZwbU14dDlCMm9aSXlselFEVms2SG9lTVRDeElvdzRUR3BqSTQ1Lk5OR1FOOC5LWEVqRFUtQUFOd09nRFlSQ09FTldxcWt3Q25URWZkajJnX2JQZEh3dWJJZ1U3WlpKbFJNVzZtd1F1bUZkb21rU2hoNGRsYVk4dHFwNEMtZVZ3QXd6dWtsNEpSaU1keG8tX1FudzFxQ3FrN2ZTNXQwbEhpT05YUG9jQWo3MlZrMGlVRUZXQTdOUnBIMUh1X2JSLjlBcGM1ekx6N0FocDhMRktTZlJLd3k5NzluaHFBTDF4UXBQb3JHTGMySVNpMyJ9|4c9d028c429be385a79e8bf99bf6222b192fdf47d4a88acbbe8034444d1407f0;Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1655106911;_xsrf=0c5a3289-aadf-4b67-be81-0502c1bc8b75;_zap=345147c2-f680-4373-9e48-8a12d2ad02cd"""
    # print(login.check_cookie(c))
    # print(login.generate_tracks(25))
