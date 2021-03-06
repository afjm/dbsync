# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class DbsyncPipeline(object):
    def __init__(self):
        self.f = open('cqssc.json', 'w')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.f.write(line)

        return item

    def close_spider(self, spider):
        self.f.close()