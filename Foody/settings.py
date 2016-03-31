# -*- coding: utf-8 -*-

BOT_NAME = 'Foody'
SPIDER_MODULES = ['Foody.spiders']
NEWSPIDER_MODULE = 'Foody.spiders'
DOWNLOAD_HANDLERS = {
    's3': None,
}
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'Foody.spiders.rotate_useragent.RotateUserAgentMiddleware': 400
}
ITEM_PIPELINES = {
    'Foody.pipelines.FoodyPipeline': 300,
}
MONGODB_SERVER = "YOUR_HOST"
MONGODB_PORT = 'PORT'
MONGODB_DB = "DB_NAME"
MONGODB_COLLECTION = "COLLECTION"

CONCURRENT_REQUESTS = 2
DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS_PER_DOMAIN = 2

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 10