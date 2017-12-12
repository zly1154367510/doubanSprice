

import urllib2
import re
import sys
import urllib
reload(sys)
sys.setdefaultencoding("utf-8")



class openUrl:
    def __init__(self,url):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
        self.url = url

    def openURL(self):
        request = urllib2.Request(url=self.url,headers=self.headers)
        response = urllib2.urlopen(request).read().decode('utf-8')

        return response


    def getStickInfoURL(self,response):
        patten = re.compile(u'<a  href="(/[0-9].*?.html)" >')
        res = re.findall(patten,response)
        return res
        #print res

class stickInfos:
    def __init__(self,URLs):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
        self.urls = URLs
        self.url = 'https://bbs.hupu.com'


    def getCompleteStickURL(self):
        completeUrls = []
        for url in self.urls:
            completeUrls.append(self.url+url)
        return completeUrls

    def pi(self):
        print "downloading img"

    def getStickinfo(self,comleteUrls):
        stickInfos = []
        x = 1
        for url in comleteUrls:
           # si = stickInfo()
            request = urllib2.Request(url=url,headers=self.headers)
            response = urllib2.urlopen(request).read().decode('utf-8')
            patten = re.compile(u'<p><img src="(.*?)"')
            res = re.findall(patten,response)
            print res

            for imgurl in res:
              urllib.urlretrieve(imgurl,"D:/HupuImg/%s.jpeg"%x,self.pi())
              x+=1








URL = openUrl('https://bbs.hupu.com/selfie')

stickURLs = URL.getStickInfoURL(URL.openURL())

stickInfos = stickInfos(stickURLs)

sis = stickInfos.getCompleteStickURL()

page = stickInfos.getStickinfo(sis)

print
