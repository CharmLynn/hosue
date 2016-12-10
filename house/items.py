# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    thum_pic_url = scrapy.Field()
    alt = scrapy.Field()
    title = scrapy.Field()
    xiaoqu = scrapy.Field()
    rooms = scrapy.Field()
    square = scrapy.Field()
    direction = scrapy.Field() 
    decoration =  scrapy.Field() 
    buildtime = scrapy.Field()
    # floorhigh = scrapy.Field()
    area  = scrapy.Field()
    follows  = scrapy.Field()
    saws = scrapy.Field()
    tag = scrapy.Field()
    totalPrice = scrapy.Field()
    perPrice = scrapy.Field()
    
