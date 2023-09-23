import scrapy
from scrapy.http import HtmlResponse


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'https://www.zhipin.com/job_detail/?query=%E5%8C%97%E4%BA%ACpython&city=100010000&industry=&position=']

    # def parse_detail(self, response):
    #     job_desc = response.xpath('//*[@id="main"]/div/div[3]/ul/li//text()').extract()
    #     job_desc = ''.join(job_desc)
    #     # print(job_desc)

    def parse(self, response: HtmlResponse, **kwargs):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul//li[1]')
        print(li_list)
        for li in li_list:
            job_name = li.xpath('./div/a/div/span/text()')[0].extract()
            print(job_name)
            # detail_url = 'https://www.zhipin.com/' + li.xpath(
            #     './/div[@class="info-primary"]/h3/a/@href').extract_first()
            # yield scrapy.Request(detail_url, callback=self.parse_detail)
