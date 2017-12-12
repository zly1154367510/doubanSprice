#coding=utf-8
from bs4 import BeautifulSoup
import pandas as pd
locaFile = open("test.txt","r")

content = locaFile.read()
'''
 "html.parser"html解析器 
 Beautifulsoup构造方法
'''
soup = BeautifulSoup(content,"html.parser")

'''
找到a标签
'''
res = soup.find_all("a")
'''
for i in res:
    print i
'''
list1 = ["代号","ninini","收市价","变化","变化率","成交量"]
df = pd.DataFrame(list1);
df.to_csv("fu.csv",index=False)
file = open("fu.csv","r")
file1 = open("yahooDate.csv","r")
content = file.read();
content1 = file1.read();
content1 +=content

file.close()
file1.close()

file3 = open("yahooDate.csv","w")
file3.write(content1)
file3.close()



