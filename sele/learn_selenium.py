from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def init_chrome(headless=True, proxy=False, no_image=False):
    # conf = config()
    # chrome_remote_addr = conf.get('chrome', 'address')
    chrome_remote_addr = '127.0.0.1:9515'
    adsl = 'http://127.0.0.1:1909'
    options = webdriver.ChromeOptions()
    # 代理
    if proxy is True:
        # adsl = conf.get('proxy', 'adsl')
        options.add_argument(f"--proxy-server={adsl}")
    # Disable images
    if no_image:
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
    # 伪装参数
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36')
    # 无头参数
    if headless:
        options.add_argument("--headless")
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

    driver = webdriver.Remote(
        command_executor=chrome_remote_addr, desired_capabilities=options.to_capabilities())

    # 伪装selenium 的js代码
    script = '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        '''
    driver.set_page_load_timeout(20)
    driver.execute_script(script)
    WebDriverWait(driver, 20)
    return driver
