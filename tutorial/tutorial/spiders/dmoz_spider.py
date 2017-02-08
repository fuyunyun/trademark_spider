# -*- coding: utf-8 -*-

from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.http import request
import dbutil
from tutorial.items import *
import  json
import requests
session=requests.session()
class DmozSpider(BaseSpider):

    name = "dmoz"
    allowed_domains = ["shangdun.org"]
    start_urls = []
    headers={
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
}
    def if_null(self,list):
        if list==[]:
            list=""
            return list
        else:
            return list[0]
    def elimate(self,data):
        if " " in str(data):
            a=str(data).replace(u" ",u"")
            return a

    def start_requests(self):
        mysql=dbutil.Mysql()
        select="select * from sbw.list2 order by regNo asc limit 13000,500" #ing   #110500,500  ing
        result=mysql.getAll(select)
        for list in result:
            yield Request("http://api.shangdun.org/show/?APIkey=UYT856h09TQurw8rsW&APIpassword=Tdwh58dkP04w&RegNo="+list['regNo']+"&ClassNo="+list['typeNo'],headers=self.headers,callback=self.parse)
        mysql.dispose()

    def parse(self,response):
            info=[]
            def get_pic(link):
                strl=link.split("?")[1]
                url="http://img.shangdun.org/Img.asp?"+str(strl)   #http://img.shangdun.org/Img.asp?R=4093360&T=43   ../Img/?R=778475&T=42&p=778475.jpg
                html=session.get(url=url,headers=self.headers)
                content=html.content
                return content
            content=json.loads(response.body_as_unicode())
            if content:
                item=TutorialItem()
                item["regNo"]=content['RegNo']
                item["typeNo"]=content['TMclass']
                item["applyDate"]=content['SQdate']
                item["applyNameC"]=content['Proposer']
                item["applyAddressC"]=content['ProposerAdress']
                item["applyNameE"]=""
                item["applyAddressE"]=""
                pic_link="/Img/?R="+content['RegNo']+"&T="+content['TMclass']+"&p="+content['RegNo']+".jpg"   #http://www.shangdun.org/Img/?R=4093363&T=44&p=4093363.jpg
                item["pic"]=get_pic(pic_link)
                item["productList"]=content['Services']
                item["preliminaryNo"]=content['CSGGNum']
                item["registerNo"]=content['ZCGGNum']
                item["preliminaryDate"]=content['CSGGdate']
                item["registerDate"]=content['ZCGGdate']
                item["exclusiveLimit"]=content['ZYQdate']
                item["share"]=""
                item["lateDate"]=""
                item["internationalRegisterDate"]=""
                item["priorityDate"]=""
                item["agentName"]=content['Agent']
                item["color"]=""
                item["type"]=""
                item["status"]=""
                if content["Process"]:
                    for i in content["Process"]:
                        item["status"]=item["status"]+i["ProcessDate"]+" "+i['ProcessInfo']+"\n"
                item["announcement"]=""
                return item


    def handle_error(self, result, *args, **kw):
        print "error url is :%s" % result.request.url
        self.logger.error("error url is :%s" % result.request.url)

