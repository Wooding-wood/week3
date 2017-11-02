import json
import scrapy

class git(scrapy.Spider):

	name = 'git'

	def start_requests(self):
		urltmp = 'https://github.com/shiyanlou?page={}&tab=repositories'
		urllist = (urltmp.format(i) for i in range(1,5))

		#print(urllist)
		for url in urllist:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		#print (response)
		for course in response.css('li.public'):

			yield {
				'name': course.xpath('.//div[(@class = "d-inline-block mb-1")]/h3/a[@itemprop="name codeRepository"]/text()').re_first('\n\s*(\S*)'),
				'update_time': course.xpath('.//div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
			}

