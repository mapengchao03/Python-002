from time import sleep
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options


# 手机号/邮箱，密码
params = {
    'mobileOrEmail': '请填写手机号码／邮箱',
    'password': '请填写密码'
}

get_url = 'https://shimo.im/login?from=home'

# 输出登陆结果
result = {}

chrome_options = Options()

# 设置无头浏览器
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 设置隐藏识别到selenium
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.set_page_load_timeout(30)

try:
    driver.get(get_url)

    sleep(2)

    # 获取对应元素
    mobile_element = driver.find_element_by_xpath('//div[@class="input"]//input[@name="mobileOrEmail"]')
    password_element = driver.find_element_by_xpath('//div[@class="input"]//input[@name="password"]')
    button_element = driver.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]')

    mobile_element.send_keys(params['mobileOrEmail'])
    password_element.send_keys(params['password'])

    sleep(2)

    button_element.click()

    sleep(2)

    # 若是登陆成功，会跳转到该网址
    if driver.current_url == 'https://shimo.im/dashboard/used':
        result['status'] = '登陆成功'
    else:
        result['status'] = '登陆失败, 可能原因为账号或密码不正确'

except exceptions.TimeoutException:

    result['status'] = '登陆超时'

except exceptions as e:

    result['status'] = '异常信息为：' + e

finally:

    print(result)

    # 关闭chrome
    driver.close()

