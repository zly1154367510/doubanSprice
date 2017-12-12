#coding=gb2312
import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class oldTree:

    def __init__(self,url):
        #self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
        self.url = url;
        self.header = {'User-Agent':'Mozilla/5.0(window NT 6.1;WOW64)'};

    def getHtml(self):

        request = urllib2.Request(url=self.url,headers=self.header);
        response = urllib2.urlopen(request);
        self.content = response.read().decode('gb2312');
        print self.content;



    def cleanHtml(self):

        patten = re.compile("<div.*?class=\"WB_text_W_f14\".*?nick-name=\"老树画画\">(.*?)")
        mo = re.findall(patten,self.content)
        print mo



if __name__ == '__main__':
    o = oldTree('https://weibo.com/p/1005051454064140/home?from=page_100505_profile&wvr=6&mod=data&is_hot=1#place');
    o.getHtml()
    o.cleanHtml()
