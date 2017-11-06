# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
from sqlalchemy.orm import sessionmaker
from gitdata.models import Repository, engine
#from gitdata.items import GitdataItem

class GitdataPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.datetime.strptime(item['update_time'], '%Y-%m-%dT%H:%M:%SZ')
        self.session.add(Repository(**item))

        return item

    def open_spider(self, item):
        Session = sessionmaker(bind = engine)
        self.session = Session()

    def close_spider(self, item):
        self.session.commit()
        self.session.close()
