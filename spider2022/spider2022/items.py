# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 爬虫获取到的数据需要组装成一个item对象
class MovieItem(scrapy.Item):
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()

    pass


class XcItem(scrapy.Item):
    article = scrapy.Field()
    time = scrapy.Field()

    pass
