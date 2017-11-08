# -*- coding: utf-8 -*-
import scrapy
from gitdata.items import GitdataItem

class GitspiderSpider(scrapy.Spider):
    name = 'gitspider'
    url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'

    @property
    def start_urls(self):
        return (self.url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for repository in response.css('li.public'):
            item =  GitdataItem({
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').extract_first().split()[0],
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
                })
            url = response.urljoin('/shiyanlou/'+item['name'])
            request = scrapy.Request(url, callback=self.parse_context)
            request.meta['item'] = item
            yield request

    def parse_context(self, response):
        item = response.meta['item']

        context = response.xpath('.//ul[@class="numbers-summary"]')
        item['commits'] = context.xpath('.//span[@class="num text-emphasized"]/text()')[0].re('\n\s*(\S*)\s*\n')
        item['branches'] = context.xpath('.//span[@class="num text-emphasized"]/text()')[1].re('\n\s*(\S*)\s*\n')
        item['releases'] = context.xpath('.//span[@class="num text-emphasized"]/text()')[2].re('\n\s*(\S*)\s*\n')

        yield item
