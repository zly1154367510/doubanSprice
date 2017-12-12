#coding=gb2312
import sys
reload(sys)
sys.setdefaultencoding('GB18030')
import urllib2
from numpy import genfromtxt ,zeros
import matplotlib.pyplot as plt
# url = "http://aima.cs.berkeley.edu/data/iris.csv"
#
# content = urllib2.urlopen(url).read();
#
# #csv能较为方便地转化为各种数据结构
# locaFlie = open("huaer.csv","w")
#
# locaFlie.write(content)
#
# locaFlie.close()
'''
genfromtxt
读取csv文件
返回numpy数组数据类型
delimiter 分割符

'''
date = genfromtxt("huaer.csv",delimiter=",",usecols=(0,1,2,3,),dtype=str)

target = genfromtxt('huaer.csv',delimiter=',',usecols=(4),dtype=str)

#以target的元素分类为date数据集的下标来赋值元素
s = date[target=="setosa"]
v = date[target=="versicolor"]
vi = date[target=="virginica"]
'''
scatter
绘制散点图
c:颜色
s[:,1]选择矩阵数据第一列全部
'''
plt.scatter(s[:,0],s[:,2],s=20,c="red")
plt.scatter(v[:,0],v[:,2],s=20,c="blue")
plt.scatter(vi[:,0],vi[:,2],s=20,c="yellow")
#plt.show()


'''
绘制
'''