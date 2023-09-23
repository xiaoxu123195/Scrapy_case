# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecrultwangyiItem(scrapy.Item):
    # 职位名称
    name = scrapy.Field()
    # 所属部门
    department = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 工作类型
    type = scrapy.Field()
    # 工作地点
    place = scrapy.Field()
    # 招聘人数
    people = scrapy.Field()
    # 发布时间
    time = scrapy.Field()


