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
# #csv�ܽ�Ϊ�����ת��Ϊ�������ݽṹ
# locaFlie = open("huaer.csv","w")
#
# locaFlie.write(content)
#
# locaFlie.close()
'''
genfromtxt
��ȡcsv�ļ�
����numpy������������
delimiter �ָ��

'''
date = genfromtxt("huaer.csv",delimiter=",",usecols=(0,1,2,3,),dtype=str)

target = genfromtxt('huaer.csv',delimiter=',',usecols=(4),dtype=str)

#��target��Ԫ�ط���Ϊdate���ݼ����±�����ֵԪ��
s = date[target=="setosa"]
v = date[target=="versicolor"]
vi = date[target=="virginica"]
'''
scatter
����ɢ��ͼ
c:��ɫ
s[:,1]ѡ��������ݵ�һ��ȫ��
'''
plt.scatter(s[:,0],s[:,2],s=20,c="red")
plt.scatter(v[:,0],v[:,2],s=20,c="blue")
plt.scatter(vi[:,0],vi[:,2],s=20,c="yellow")
#plt.show()


'''
����
'''