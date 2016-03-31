# -*- coding: utf-8 -*-

from pymongo import MongoClient
from scrapy import log
from scrapy.conf import settings


class FoodyPipeline(object):
    # def __init__(self):
    #     client = MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
    #     db = client[settings['MONGODB_DB']]
    #     self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        item_ = dict(item)
        return item

        """ IF YOU WANT USE MONGODB
            + UNCOMMENT def __init__
            + UNCOMMENT LINES BELLOW
            + COMMENT return item above """
            
        # if self.collection.find(
        #         {'$or': [
        #             {'main_url': item_['main_url']},
        #             {'id': item_['id'], 'district_id': item_['district_id']}
        #         ]
        #         }
        # ).count() == 0:  # query if there are duplicated documents
        #     self.collection.insert(dict(item_))
        #     log.msg("Item wrote to MongoDB database %s/%s" %
        #             (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
        #             level=log.DEBUG, spider=spider)
        #     return item


