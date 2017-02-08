# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import dbutil

class TutorialPipeline(object):
    mysql=dbutil.Mysql()
    def process_item(self, item, spider):
        selectStr='select * from sbw.sblist where regNo=%s'
        insertStr='insert into sbw.sblist values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        updateStr='update sbw.sblist set typeNo=%s,applyDate=%s,applyNameC=%s,applyAddressC=%s,applyNameE=%s,applyAddressE=%s,pic=%s,productList=%s,preliminaryNo=%s,registerNo=%s,preliminaryDate=%s,registerDate=%s,exclusiveLimit=%s,share=%s,lateDate=%s,internationalRegisterDate=%s,priorityDate=%s,agentName=%s,color=%s,type=%s,status=%s,announcement=%s  where regNo=%s'
        if self.mysql.getOne(selectStr,[[item["regNo"]]])==False:
            self.mysql.insertOne(insertStr,([item["regNo"],item["typeNo"],item["applyDate"],item["applyNameC"],item["applyAddressC"],item["applyNameE"],item["applyAddressE"],item["pic"],item["productList"],item["preliminaryNo"],
                         item["registerNo"],item["preliminaryDate"],item["registerDate"],item["exclusiveLimit"],item["share"],item["lateDate"],item["internationalRegisterDate"],item["priorityDate"],item["agentName"],
                         item["color"],item["type"],item["status"],item["announcement"]]))
        else:
            self.mysql.update(updateStr,(item["typeNo"],item["applyDate"],item["applyNameC"],item["applyAddressC"],item["applyNameE"],item["applyAddressE"],item["pic"],item["productList"],item["preliminaryNo"],
                         item["registerNo"],item["preliminaryDate"],item["registerDate"],item["exclusiveLimit"],item["share"],item["lateDate"],item["internationalRegisterDate"],item["priorityDate"],item["agentName"],
                         item["color"],item["type"],item["status"],item["announcement"],item["regNo"]))



