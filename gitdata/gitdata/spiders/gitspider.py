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
            yield item
