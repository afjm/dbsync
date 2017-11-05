# -*- coding: utf-8 -*-
import scrapy
from dbsync.items import DbsyncItem
import datetime


class CqsscSpider(scrapy.Spider):
    # 爬虫名称
    name = 'cqssc'
    # 爬虫作用域
    allowed_domains = ['chart.cp.360.cn']
    # 基础URL
    base_url = 'http://chart.cp.360.cn/kaijiang/kaijiang?lotId=255401&spanType=2&span='
    # 开始日期
    begin = datetime.date(2010, 1, 1)
    # 结束日期
    # end = datetime.date(2017, 9, 10)
    end = datetime.date.today()
    # URL拼接字符串
    offset = str(begin) + '_' + str(begin)
    # 起始URL
    start_urls = [base_url + offset]

    i = 1

    # start_urls = ['http://chart.cp.360.cn/kaijiang/kaijiang?lotId=255401&spanType=2&span=2017-09-10_2017-09-10']

    # 在命令行中执行scrapy crawl cqssc

    def parse(self, response):
        node_list = response.xpath("//td[@class='red big']")

        for node in node_list:
            item = DbsyncItem()

            sn = node.xpath("../td[position()=1]/text()").extract_first()
            code = node.xpath("./text()").extract_first()
            # 加逗号隔开
            # str_code = code[0] + ',' + code[1] + ',' + code[2] + ',' + code[3] + ',' + code[4]
            # 不加逗号
            str_code = code

            item['id'] = self.i
            item['sn'] = str(self.begin.strftime('%Y%m%d'))[2:] + sn
            # item['sn'] = '170910' + sn[0]
            item['code'] = str_code
            self.i += 1

            # items.append(item)
            yield item

        if self.begin < self.end:
            self.begin += datetime.timedelta(days=1)
            self.offset = str(self.begin) + '_' + str(self.begin)
            url = self.base_url + self.offset
            yield scrapy.Request(url, callback=self.parse)
