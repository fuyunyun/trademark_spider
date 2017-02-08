# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    regNo=scrapy.Field()
    typeNo=scrapy.Field()
    applyDate=scrapy.Field()
    applyNameC=scrapy.Field()
    applyAddressC=scrapy.Field()
    applyNameE=scrapy.Field()
    applyAddressE=scrapy.Field()
    pic_link=scrapy.Field()
    pic=scrapy.Field()
    productList=scrapy.Field()
    preliminaryNo=scrapy.Field()
    registerNo=scrapy.Field()
    preliminaryDate=scrapy.Field()
    registerDate=scrapy.Field()
    exclusiveLimit=scrapy.Field()
    share=scrapy.Field()
    lateDate=scrapy.Field()
    internationalRegisterDate=scrapy.Field()
    priorityDate=scrapy.Field()
    agentName=scrapy.Field()
    color=scrapy.Field()
    type=scrapy.Field()
    status=scrapy.Field()
    announcement=scrapy.Field()