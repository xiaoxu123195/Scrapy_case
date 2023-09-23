import scrapy
from scrapy.http import HtmlResponse
import json


class RecrultSpider(scrapy.Spider):
    name = 'recrult'

    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://hr.163.com/api/hr163/position/queryPage']

    def start_requests(self):
        headers = {
            'referer': 'https://hr.163.com/job-list.html',
            'content-type': 'application/json;charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/103.0.0.0 Safari/537.36 '
        }
        urls = ['https://hr.163.com/api/hr163/position/queryPage']
        for url in urls:
            yield scrapy.FormRequest(
                url=url,
                headers=headers,
                formdata={'currentPage': '1', 'pageSize': '10'},
                callback=self.parse,
            )

    def parse(self, response: HtmlResponse, **kwargs):
        print(response.text)
