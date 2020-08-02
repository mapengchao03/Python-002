import scrapy
import re
import os.path
from fake_useragent import UserAgent
from scrapy.selector import Selector
from week02.task_one.task_one.items import TaskOneItem


class MaoYanSpider(scrapy.Spider):

    # 用于区别Spider
    name = "MaoYanSpider"

    # 允许访问的域
    allowed_domains = ['maoyan.com']

    # 爬取的初始地址
    start_urls = ['https://maoyan.com/films?showType=3']

    # 随机user-agent, 禁止从ssl获取，目的提升访问效率
    ua = UserAgent(verify_ssl=False)
    # cookie = {'uuid_n_v': 'v1', ' uuid': '3B86C410D39F11EA84945F632DCF0A4D55C95913EA904E5FAAC9E2EA19B779D0',
    #           ' _csrf': 'beec5daabd1275ce5d50f8ab635b09088d5ef40adc0ecb5dc815577704266602',
    #           ' Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1596249145',
    #           ' _lxsdk_cuid': '173a7dcfffbc8-046569a3c04ea5-31677301-100200-173a7dcfffb88',
    #           ' _lxsdk': '3B86C410D39F11EA84945F632DCF0A4D55C95913EA904E5FAAC9E2EA19B779D0',
    #           ' mojo-uuid': '80d550754e96a80ba616c635ca256d8d',
    #           ' mojo-session-id': '{"id":"b28952d4010f939d8c01a40a662dd71b","time":1596376332284}',
    #           ' mojo-trace-id': '1', ' Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1596376332',
    #           ' __mta': '209138349.1596249145688.1596291815503.1596376332441.23',
    #           ' _lxsdk_s': '173af71b292-746-321-5e7%7C%7C3'}

    # 正则
    def re_text(self, html_text):

        pattern = r"</span>\s+(?P<text>\S+)\s+</div>"
        result = re.search(pattern, html_text)
        text = result.group("text")
        return text

    # 根据url进行抓取
    def start_requests(self):

        for start_url in self.start_urls:

            response = scrapy.Request(start_url, headers={'User-Agent': self.ua.random},
                                      # cookies=self.cookie,
                                      callback=self.parse_info)

            yield response

    # 获取抓取详情信息
    def parse_info(self, response):

        item = TaskOneItem()

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
                movie_name = Selector(text=movie_element_list).xpath('//div[1]//span[1]/text()').extract()[0]

                # 电影类型
                movie_type = Selector(text=movie_element_list).xpath('//div[2]/text()').extract()[1].strip()

                # 电影上映时间
                movie_time = Selector(text=movie_element_list).xpath('//div[4]/text()').extract()[1].strip()

                item['movie_name'] = movie_name
                item['movie_type'] = movie_type
                item['movie_time'] = movie_time

                yield item

            print('插入数据已完成')

        except Exception:

            print('可能被猫眼识别，没有获取到数据，请重新执行程序!')










