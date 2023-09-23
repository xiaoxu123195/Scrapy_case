import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from ..items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    # start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}&filter=')

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            movie_item = MovieItem()
            movie_item['title'] = list_item.css('span.title::text').extract_first()
            # list_item.css 返回的结果任然是选择器对象 即使用.extract_first() 抽取第一个对象
            movie_item['rank'] = list_item.css('span.rating_num::text').extract_first()
            movie_item['subject'] = list_item.css('span.inq::text').extract_first()
            yield movie_item
            # 将最会拿到的数据交由yield处理

            # hrefs_list = sel.css('div.paginator > a::attr(href)')
            # for href in hrefs_list:
            #    url = response.urljoin(href.extract())
            #    print(url)

        pass
