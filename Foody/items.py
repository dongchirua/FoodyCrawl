# -*- coding: utf-8 -*-

import scrapy


class FoodyItem(scrapy.Item):
    city = scrapy.Field() # City
    district_id = scrapy.Field() # DistrictId
    main_url = scrapy.Field() # DetailUrl
    addr = scrapy.Field() # Address
    mobile_pic = scrapy.Field() # MobilePicturePath
    large_pic = scrapy.Field() # PicturePathLarge
    main_category_id = scrapy.Field() # MainCategoryId
    lat = scrapy.Field() # Latitude
    long = scrapy.Field() # Longitude
    views = scrapy.Field() # TotalView
    cuisines = scrapy.Field() # Cuisines[:]['Id']
    rating = scrapy.Field() # AvgRating
    id = scrapy.Field() # Id
    category = scrapy.Field() # MainCategoryId
    pass
