#coding=utf-8
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('gbk')
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import sqlalchemy as sql

'''
获取html
'''
url = 'https://hk.finance.yahoo.com/quote/%5EIXIC/components?ltr=1'
content = urllib2.urlopen(url).read()

# file5 = open("test.txt","r")
# content = file5.read()
soup = BeautifulSoup(content,"html.parser")


'''
BeautifulSoup解析html
'''
#BeautifulSoup中文文档 http://beautifulsoup.readthedocs.io/zh_CN/latest/
#找到div的class属性为hotnews的部分在解析其中li部分
code = soup.find_all("a",{'class','C($c-fuji-blue-1-b) Cur(p) Td(n) Fw(500)'})
codeList = []
for i in code:
    '''
    获取公司代号
    '''
    codeList.append(i.text)



# companyName = soup.find_all('td',{'class','Py(10px) Ta(start) Pend(10px)'})
# companyList = []
# for i in companyName:
#     print i.text
'''
获取公司交易数据
'''
transactionData = soup.find_all('td',{'class','Py(10px) Pstart(10px)'})
transactionDataList = []
for i in transactionData:
    transactionDataList.append(i.text)

if len(transactionDataList) == 120:
    n = np.array(transactionDataList).reshape(30,4)


'''
保存为DateFrame并写入csv
'''
DateFrameColumnsList = ["code","Market price","Year-on-year change","Year-on-year change rate","volume"]
list2 = []
df = pd.DataFrame(columns=DateFrameColumnsList)
if len(codeList)==30:
    df["code"] = codeList
    df[["Market price","Year-on-year change","Year-on-year change rate","volume"]] = n
    df.to_csv("fu.csv",index=False,header=False)
    file1 = open("fu.csv","r")
    file2 = open("yahooDate.csv","r")
    content1 = file1.read()
    content2 = file2.read()
    # content1fu = content1.replace(',code,Market price,Year-on-year change,Year-on-year change rate,volume',"")
    # content1fu1 = content1fu.strip()+"\n"
    content2 += content1
    file1.close()
    file2.close()
    file2 = open("yahooDate.csv", "w")
    file2.write(content2)
    file2.close();





