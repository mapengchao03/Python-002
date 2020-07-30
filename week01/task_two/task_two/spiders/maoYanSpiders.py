import scrapy
import re
import os.path
from fake_useragent import UserAgent
from scrapy.selector import Selector
from week01.task_two.task_two.items import MaoYanSpiderItem


class MaoYanSpider(scrapy.Spider):

    # 用于区别Spider
    name = "MaoYanSpider"

    # 允许访问的域
    allowed_domains = ['maoyan.com']

    # 爬取的初始地址
    start_urls = ['https://maoyan.com/films?showType=3']

    # 随机user-agent, 禁止从ssl获取，目的提升访问效率
    ua = UserAgent(verify_ssl=False)

    # 正则
    def re_text(self, html_text):

        pattern = r"</span>\s+(?P<text>\S+)\s+</div>"
        result = re.search(pattern, html_text)
        text = result.group("text")
        return text

    # 根据url进行抓取
    def start_requests(self):
        for start_url in self.start_urls:
            response = scrapy.Request(start_url, headers={'User-Agent': self.ua.random}, callback=self.parse_info)
            yield response

    # 获取抓取详情信息
    def parse_info(self, response):

        item = MaoYanSpiderItem()

        try:

            movie_element = response.css('.movies-list dd .movie-item .movie-item-hover a .movie-hover-info').extract()[:10]

            if len(movie_element) == 0:

                raise Exception

            # 判断是否存在scMovie.csv文件，若存在，清空内容
            if os.path.exists('./scMovie.csv'):

                with open('./scMovie.csv', "r+") as f:

                    f.seek(0)

                    # 清空文件
                    f.truncate()

            for movie_element_list in movie_element:

                # 电影名字
                movie_name = Selector(text=movie_element_list).css('.name::text').extract_first()

                # 电影类型
                movie_type_element = Selector(text=movie_element_list).css('.movie-hover-title').extract()[1]
                movie_type = self.re_text(str(movie_type_element))

                # 电影上映时间
                movie_time_element = Selector(text=movie_element_list).css('.movie-hover-title').extract()[3]
                movie_time = self.re_text(str(movie_time_element))

                item['movie_name'] = movie_name
                item['movie_type'] = movie_type
                item['movie_time'] = movie_time

                yield item

            print('数据抓取完整，详情数据查阅 scMovie.csv文件')

        except Exception:

            print('可能被猫眼识别，没有获取到数据，请重新执行程序!')






