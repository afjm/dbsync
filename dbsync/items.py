# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbsyncItem(scrapy.Item):
    # define the fields for your item here like:

    id =scrapy.Field()
    # 期号
    sn = scrapy.Field()
    # 开奖号码
    code = scrapy.Field()
