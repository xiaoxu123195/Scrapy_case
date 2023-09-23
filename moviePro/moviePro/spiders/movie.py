import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import MovieproItem, DetailItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.nssdy.com/vod-type-id-1-pg-1.html']

    link = LinkExtractor(allow=r'vod-type-id-1-pg-\d+')
    link_detail = LinkExtractor(allow=r'vod-detail-id-\d+\.html')
    rules = (
        Rule(link, callback='parse_item', follow=False),
        Rule(link_detail, callback='parse_detail')
    )

    # http://www.nssdy.com/vod-detail-id-219711.html
    # http://www.nssdy.com/vod-detail-id-219710.html
    def parse_item(self, response):
        # print(response)
        tr_list = response.xpath('//ul[@class="img-list"]//li')
        for tr in tr_list:
            title = tr.xpath('./h5/a/text()').extract_first()
            price = tr.xpath('./p[2]/em/text()').extract_first()
            # print(title, price)
            item = MovieproItem()
            item['title'] = title
            item['price'] = price

            yield item

    def parse_detail(self, response):
        name = response.xpath('//*[@id="main"]/div[3]/div[1]/div[2]/a/text()').extract_first()
        spaker = response.xpath('//*[@id="main"]/div[3]/div[1]/div[2]/ul/li[5]/a[1]/text()').extract_first()
        # print(name, spaker)
        item = DetailItem()
        item['name'] = name
        item['spaker'] = spaker

        yield item


