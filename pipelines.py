# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request


class BaiduimagespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image in item['image_urls']:
            yield Request(image, meta={'item': item})

    # Name download version
    def file_path(self, request, response=None, info=None):
        image_name = request.meta['item']['image_name']
        image_guid = request.url.split('/')[-1]
        # return u'full/{0}/{1}'.format(item['folder_name'], image_guid)
        return 'full/{}/{}'.format(image_name, image_guid)

    # # Name thumbnail version
    # def thumb_path(self, request, thumb_id, response=None, info=None):
    #     image_guid = thumb_id + request.url.split('/')[-1]
    #     return 'thumbs/%s/%s.jpg' % (thumb_id, image_guid)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item
