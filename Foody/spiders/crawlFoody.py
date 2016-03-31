"""
author: Quy, dongchirua@live.com
created 27 Dec, 2015
"""
import json, pdb, logging, re, requests
from scrapy import Request
from scrapy.spiders.init import InitSpider
from scrapy.shell import inspect_response
from Foody.items import FoodyItem


class FoodCrawler(InitSpider):
    name = "food"
    allowed_domains = ["www.foody.vn"]
    start_urls = [
        'http://www.foody.vn/ho-chi-minh/quan-an',
        'http://www.foody.vn/ho-chi-minh/an-vat-via-he',
        'http://www.foody.vn/ho-chi-minh/tiem-banh',
        'http://www.foody.vn/ho-chi-minh/nha-hang',
        'http://www.foody.vn/ho-chi-minh/an-chay'
    ]
    provider_per_page = 12
    provinceId = 217  # Saigon
    magic_number = 20 # don't ask why, it's magic ^.^
    category = {
        'quan-an': 3,
        'an-vat-via-he': 11,
        'tiem-banh': 6,
        'nha-hang': 1,
        'an-chay': 56
    }
    login_page = 'http://www.foody.vn/dang-nhap'

    def __init__(self, user=None, password=None, is_debug=False, *args, **kwargs):
        super(FoodCrawler, self).__init__(*args, **kwargs)
        self.password = password
        self.user = user
        self.is_debug = is_debug
        msg = 'The account will be used ' + user + ' ' + password
        self.log(msg, level=logging.INFO)
        self.log('That being said, it works for me. Thank you for using my work', level=logging.INFO)

    def init_request(self):
        """ This function is called before crawling starts. """
        msg = {'email': self.user, 'password': self.password,
               'reCaptchaResponse': '', 'rememberMe': 'true'}
        headers = {'Host': 'www.foody.vn',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'en-US,vi;q=0.5',
                   'Referer': 'http://www.foody.vn',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Content-Type': 'application/json'}
        return Request(self.login_page, method='POST', body=json.dumps(msg), headers=headers,
                       callback=self.check_login_response)

    def check_login_response(self, response):
        """
        Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if json.loads(response.body)['isSuccess']:
            self.log("Successfully logged in!", level=logging.INFO)
            return self.initialized()
        else:
            self.log("Can't login", level=logging.ERROR)

    def parse(self, response):
        """
        First step: yield request
        """
        page_name_ = re.sub('http://www.foody.vn\/ho-chi-minh\/', '', response.url)
        category_id = self.category[page_name_]
        total_ = response.xpath("//div[@class='result-status-count']/div/span/text()").extract()[0]
        total_ = int(int(re.sub('\.', '', total_)) / self.provider_per_page)
        header_ = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'en-US,vi;q=0.5',
                   'Referer': response.url,
                   'DNT': 1,
                   'Host': 'www.foody.vn',
                   'Pragma': 'no-cache',
                   'X-Foody-User-Token': '49f6ad1b-e2dc-4b68-ad0d-b18f64cb146c',
                   'X-Requested-With': 'XMLHttpRequest'}
        priority_ = self.magic_number
        for sub_page in range(1, self.magic_number):
            url_ = 'http://www.foody.vn/ho-chi-minh/dia-diem?ds=Restaurant&vt=row&st=1&dt=undefined&c=3&' \
                   'page={}&provinceId={}&categoryId={}&append=true'.format(sub_page, self.provinceId, category_id)
            yield Request(url=url_, dont_filter=True, meta={'page': sub_page}, callback=self.parse_items,
                          headers=header_,priority=priority_)
            priority_ -= 1

    def parse_items(self, response):
        """
        Second step: yield item
        """
        page_number = response.meta['page']
        response_ = json.loads(response.body)
        if self.is_debug:
            inspect_response(response, self)
        for i in response_['searchItems']:
            item = FoodyItem()
            item['city'] = i['City']
            item['district_id'] = i['DistrictId']
            item['main_url'] = self.allowed_domains[0] + i['DetailUrl']
            item['addr'] = i['Address']
            item['mobile_pic'] = re.sub('^//', '', i['MobilePicturePath'])
            item['large_pic'] = re.sub('^//', '', i['PicturePathLarge'])
            item['main_category_id'] = i['MainCategoryId']
            item['lat'] = i['Latitude']
            item['long'] = i['Longitude']
            item['views'] = i['TotalView']
            item['cuisines'] = dict()
            item['cuisines']['id'] = list()
            item['cuisines']['name'] = list()
            for j in i['Cuisines']:
                item['cuisines']['id'].append(j['Id'])
                item['cuisines']['name'].append(j['Name'])
            item['rating'] = i['AvgRating']
            item['id'] = i['Id']
            item['category'] = i['MainCategoryId']
            yield item
