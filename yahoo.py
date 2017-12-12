# -*- coding:utf-8 -*-
import urllib2
import re
import sys

class MoveYahoo:

    def __init__(self):
        self.url = "https://hk.finance.yahoo.com/q/cp?s=%5EIXIC"
        reload(sys)
        sys.setdefaultencoding("utf-8")
        self.filePath = "yahooDate.txt"
        self.movieList = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}

    def getData(self):
        request = urllib2.Request(url=self.url, headers=self.headers)
        response = urllib2.urlopen(request)
        data = response.read().decode('utf-8')
        print "正在抓取网页数据"
        return data

    def CleanData(self):
        patten = re.compile("<td.*?class=Py(10px).*?>(.*?)</td>")
        data = self.getData()
        res = re.findall(patten,data)
        return res

    def duquData(self):
        patten = re.compile("")
        date = open('yy.txt','r').read().decode('utf-8')
        res = re.findall(patten,date)
        return date



move = MoveYahoo()
res = move.duquData()
print res



