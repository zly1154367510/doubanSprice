#coding=utf-8
import urllib2
import re
import sys
import numpy as np
import pandas as pd



class MovieTop250:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        self.start = 0
        self.wed = "https://movie.douban.com/top250?start="
        self.param = ""
        self.filePath = "doubanDate.txt"
        self.movieList = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}


    def getPage(self):
        '''
        抓取一页网页数据
        while循环调用
        :return: 对应页数的源码
        '''
        URL = self.wed+str(self.start)
        request = urllib2.Request(url = URL,headers=self.headers)
        response = urllib2.urlopen(request)
        page = response.read().decode("utf-8")
        pageNum = (self.start+25)/25
        print "正在抓取第"+`pageNum`+"页数据"
        self.start+=25
        return page

    def getMovie(self):
        '''
        获取getPage（）返回htmly源码
        正则表达式匹配
        存入
        :return:
        '''
        #作品名称
        patten = re.compile(u'<span class="title">([^a-z]*?)</span>')
        #出品年份
        patten1 = re.compile(u'<span.*?class="other">&nbsp;/&nbsp;(.*?)</span>.*?')
        #评论人数
        patten2 = re.compile(u'<span>(.*?)人评价</span>')
        result = pd.DataFrame()
        while self.start<250:
            page = self.getPage()
            movies = re.findall(patten,page)
            movies1 = re.findall(patten1,page)
            movies2 = re.findall(patten2,page)

            arr2 = pd.DataFrame({"电影名":movies,"发行商":movies1,"评论人数":movies2})
            result1 = pd.concat([arr2,result])
            result = result1
           # print arr2



        #result1.to_csv("yy.csv",index=False)
        print type(movies2[0])

    def writeText(self):
        fileTop250 = open(self.filePath,"w")
        num = 1
        for movie in self.movieList:
            fileTop250.write(movie[0])
            fileTop250.write(movie[1]+'\n')
            num+=1
            print "写入第"+`num`+"个网页"

douban = MovieTop250()
douban.getMovie()
#douban.writeText()