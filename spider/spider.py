# -*- coding: utf-8 -*-
import json
from time import sleep
from urllib.parse import urlencode

import scrapy

from BaiduImageSpider.items import BaiduimagespiderItem


class Spider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['image.baidu.com']
    search_lists = ['大雁塔', '肉夹馍']
    max_pages = 1

    def start_requests(self):
        for i in range(len(self.search_lists)):
            queryWord = urlencode({'queryWord': self.search_lists[i]})
            word = urlencode({'word': self.search_lists[i]})
            for k in range(self.max_pages):  # number of page to crawl
                url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&" + \
                      queryWord + "&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&" + \
                      word + "&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=" + str(k * 30) + "&rn=30"
                sleep(0.1)
                yield scrapy.Request(url, callback=self.parse, meta=({'search': self.search_lists[i]}), dont_filter=True)

    def parse(self, response):
        imgs = json.loads(response.body)['data']
        for img in imgs:
            item = BaiduimagespiderItem()
            item['image_name'] = response.meta['search']
            try:
                item['image_urls'] = [img['middleURL']]
                yield item
            except Exception as e:
                print(e)
