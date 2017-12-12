#coding=utf-8
from __future__ import division
import pandas as pd
from  pandas import Series,DataFrame

import sys
reload(sys)
sys.setdefaultencoding("GB18030")
import matplotlib.pyplot as plt
'''
import seaborn as sns

sns.set_style("whitegrid")
%matplotlib lnline
'''

import pandas_datareader as web
from datetime import datetime




if __name__ == '__main__':
    #date = web.DataReader('601857.SS','yahoo')
    #date.to_csv("date.csv")

    date = pd.read_csv("date.csv")
    plt.plot(date['Date'],date['Close'])
    plt.title("SINOPEC")
    plt.xlabel("date")
    plt.ylabel("close")
    plt.show()