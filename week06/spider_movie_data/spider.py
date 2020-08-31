from time import sleep
from week06.spider_movie_data.db.movie_mysql import ConnDB
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options


def driver():

    chrome_options = Options()

    # 设置无头浏览器
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 设置隐藏识别到selenium
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 其他设置
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.set_page_load_timeout(30)

    return driver


def run():

    basic_url = 'https://movie.douban.com/subject/26754233/reviews?start='
    spider_page = 4
    all_start = {
        '力荐': 5,
        '推荐': 4,
        '还行': 3,
        '较差': 2,
        '很差': 1
    }

    data = []

    try:

        for i in range(spider_page):

            driver.get(basic_url + str(i))
            sleep(2)
            comments = driver.find_elements_by_css_selector('.article .review-list   .review-item')
            for comment in comments:
                try:
                    star = all_start[comment.find_element_by_css_selector('.main-title-rating').get_attribute('title')]
                except Exception:
                    star = 0
                comment_time = comment.find_element_by_css_selector('.main-meta').text
                short_comment = comment.find_element_by_css_selector('.short-content').text
                data.append((short_comment, comment_time, star))

    except Exception as e:

        print('抓取异常，异常信息为：', e)

    finally:

        driver.close()
        if len(data) != 0:
            ConnDB.run(data)
            print('数据写入已完成')


if __name__ == '__main__':

    ConnDB = ConnDB()
    driver = driver()
    run()
