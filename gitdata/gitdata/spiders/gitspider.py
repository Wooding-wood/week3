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
        item =  GitdataItem({
            'name': response.css('div.d-inline-block.mb-1 h3 a::text').extract_first().split()[0],
            'update_time': response.xpath('.//relative-time/@datetime').extract_first()
            })
        yield item
