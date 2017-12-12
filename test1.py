#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('GB18030')
import pandas as pd
import matplotlib.pyplot as plt
import re

str1 = "123456789"
str2 = "hello world"
str3 = "在线时间：4582小时    加入时间：2012-07-19"

print re.findall(re.compile("加入时间"),str3)