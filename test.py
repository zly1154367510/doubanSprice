#coding=utf-8
import re
import pandas as pd
import string
import matplotlib.pyplot as plt

df2015 = pd.read_csv("df2015.csv")
let = []
for i in df2015['日期']:
	l = i.split("/")
	let.append(l[0]+l[1]+l[2])

df2015.index = let
df2015 = df2015.drop(["日期"],axis=1) #必须有一个变量接收返回值

lsa=df2015.index
lsb=[]
lsyct=[0,31,28,31,30,31,30,31,31,30,31,30,31]
sumdays=0
t=0
y=0
m=0
d=0

#201756
for i in lsa:
	sumdays = 0
	#得出年月日
	y = string.atoi(i)/100
	m = string.atoi(i)/10%10
	d = string.atoi(i)%10



	for j in lsyct[0:m]:
		sumdays += j

	sumdays = (sumdays + d - 2)/7
	lsb.append("第%s周"%sumdays)

	#df2015.index = lsb


df2015.index = lsb
df2015.to_csv("df_bor_201005_0716074.csv",index=False)

print df2015["名称"]
