import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

from ..items import FbsproItem


class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']
    redis_key = 'sun'

    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath('//ul[@class="title-state-ul"]//li')
        for tr in tr_list:
            new_num = tr.xpath('./span/text()').extract_first()
            new_title = tr.xpath('./span[3]/a/text()').extract_first()
            item = FbsproItem()
            item['new_num'] = new_num
            item['new_title'] = new_title

            yield item
