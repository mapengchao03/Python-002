import scrapy
import re
import os.path
import random
from scrapy.selector import Selector
from week01.task_two.task_two.items import MaoYanSpiderItem


class MaoYanSpider(scrapy.Spider):

    # 用于区别Spider
    name = "MaoYanSpider"

    # 允许访问的域
    allowed_domains = ['maoyan.com']

    # 爬取的初始地址
    start_urls = ['https://maoyan.com/films?showType=3']

    # 电影名称，类型，上映时间，定义一个list
    movie_list = []

    # 定义抓取数量
    movie_count = 10

    init_count = 0

    # 定义随机user-agent
    def headers(self):

        USER_AGENT_LIST = [
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
            'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
            'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.3 Mobile/14E277 Safari/603.1.30',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        ]

        USER_AGENT = random.choice(USER_AGENT_LIST)

        return {
            'User-Agent': USER_AGENT,
        }

    # 根据url进行抓取
    def start_requests(self):
        for start_url in self.start_urls:
            response = scrapy.Request(start_url, headers=self.headers(), callback=self.parse_info)
            yield response

    # 获取抓取详情信息
    def parse_info(self, response):

        item = MaoYanSpiderItem()

        movie_element = response.css('.movies-list dd .movie-item .movie-item-hover a .movie-hover-info ').extract()

        if len(movie_element) == 0:

            print('可能被猫眼识别，没有获取到数据，请重新执行程序!')

        else:

            # 判断是否存在scMovie.csv文件，若存在，清空内容
            if os.path.exists('./scMovie.csv'):

                with open('./scMovie.csv', "r+") as f:

                    f.seek(0)

                    # 清空文件
                    f.truncate()

            for movie_element_list in movie_element:

                # 只取前10个
                if self.init_count < self.movie_count:

                    # 电影名字
                    movie_name = Selector(text=movie_element_list).css('.name::text').extract_first()

                    # 准换成字符串，然后进行拆分，替换
                    # 电影类型
                    movie_type_element = Selector(text=movie_element_list).css('.movie-hover-title').extract()[1]
                    movie_type = str(movie_type_element).split('</span>')[1].replace('</div>', '').strip()

                    # 准换成字符串，然后进行拆分，替换
                    # 电影上映时间
                    movie_time_element = Selector(text=movie_element_list).css('.movie-hover-title').extract()[3]
                    movie_time = str(movie_time_element).split('</span>')[1].replace('</div>', '').strip()

                    self.init_count += 1

                    item['movie_name'] = movie_name
                    item['movie_type'] = movie_type
                    item['movie_time'] = movie_time

                    yield item

                else:
                    break

            print('数据抓取完整，详情数据查阅 scMovie.csv文件')






