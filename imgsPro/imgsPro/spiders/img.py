import scrapy
from scrapy.http import HtmlResponse

from ..items import ImgsproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response: HtmlResponse, **kwargs):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            src = div.xpath('./div/a/img/@src').extract_first()
            src = "https:"+src
            # print("http:"+src)
            item = ImgsproItem()
            item['src'] = src
            yield item


