import requests
import re
import pandas as pd
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as Bs


# 正则
def re_text(html_text):

    pattern = r"</span>\s+(?P<text>\S+)\s+</div>"
    result = re.search(pattern, html_text)
    text = result.group("text")
    return text


# 代理
def http_proxy():

    res = requests.get('https://ip.jiangxianli.com/api/proxy_ip')
    ip = res.json()['data']['ip']
    proxies = {
        'http': 'http://' + ip,
        'https': 'https://' + ip,
    }
    return proxies


# 随机user-agent, 禁止从ssl获取，目的提升访问效率
ua = UserAgent(verify_ssl=False)

# 电影名称，类型，上映时间，定义一个list
movie_list = []

url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers={'User-Agent': ua.random})

bs_info = Bs(response.text, 'html.parser')

try:

    movies_info_element = bs_info.select('.movies-list dd .movie-item .movie-item-hover a')[:10]

    if len(movies_info_element) == 0:

        raise Exception

    # 遍历每个电影的详情信息
    for movies_detail_list in movies_info_element:

        # 电影名称
        movie_name = movies_detail_list.find_all('div', class_="movie-hover-title")[0].contents[1].string

        # 电影类型
        movie_type = movies_detail_list.find_all('div', class_="movie-hover-title")[1].contents[2].string.strip()

        # 电影上映时间
        movie_time = movies_detail_list.find_all('div', class_="movie-hover-title")[3].contents[2].string.strip()

        movie_list.append([movie_name, movie_type, movie_time])

    movie = pd.DataFrame(data=movie_list)

    # 转存csv
    movie.to_csv('./movie.csv', encoding='utf8', index=False, header=False)

    print('数据抓取完整，详情数据查阅 movie.csv文件')

except Exception:

    print('可能被猫眼识别，没有获取到数据，请重新执行程序!')
