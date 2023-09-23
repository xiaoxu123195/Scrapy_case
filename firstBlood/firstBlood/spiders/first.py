import scrapy
from scrapy.http import HtmlResponse

from firstBlood.firstBlood.items import FirstbloodItem


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://you.ctrip.com/sight/jiuzhaigou25/77380.html']

    # 基于终端的储存
    # def parse(self, response: HtmlResponse, **kwargs):
    #     div_list = response.xpath('//div[@class="commentItem"]')
    #     all_data = []
    #     for div in div_list:
    #         auto = div.xpath('./div[1]/div[2]/text()')[0].extract()
    #         another = div.xpath('./div[2]/div[2]/text()')[0].extract()
    #         times = div.xpath('./div[2]/div[4]/div[1]/text()')[0].extract()
    #         fabulous = div.xpath('./div[2]/div[4]/div[2]/span[2]/text()').extract()
    #         fabulous = ''.join(fabulous)
    #         dic = {
    #             'auto': auto,
    #             'another': another,
    #             'times': times,
    #             'fabulous': fabulous,
    #         }
    #         all_data.append(dic)
    #     return all_data

    # 基于管道的持久化储存
    def parse(self, response: HtmlResponse, **kwargs):
        div_list = response.xpath('//div[@class="commentItem"]')
        all_data = []
        for div in div_list:
            auto = div.xpath('./div[1]/div[2]/text()')[0].extract()
            another = div.xpath('./div[2]/div[2]/text()')[0].extract()
            times = div.xpath('./div[2]/div[4]/div[1]/text()')[0].extract()
            fabulous = div.xpath('./div[2]/div[4]/div[2]/span[2]/text()').extract()
            fabulous = ''.join(fabulous)

            item = FirstbloodItem()
            item['auto'] = auto
            item['another'] = another
            item['times'] = times
            item['fabulous'] = fabulous

            yield item
