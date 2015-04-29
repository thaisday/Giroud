# coding=utf-8
import json

__author__ = 'KiddoMa'

import pandas as pd
import sys
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    startTime = "05:09:01"
    endTime = "05:14:02"
    # dr = pd.date_range(datetime(hour=05,minute=8,second=0),datetime(hour=05,minute=10,second=0))

    df = pd.read_csv(r'/Users/KiddoMa/Documents/pgpginout.csv', encoding='utf-8')
    name_list = [r'times', r'pgpgin', r'pgpgout', r'fault', r'majflt', r'pgfree', r'pgscank', r'pgscand', r'pgsteal',
                 r'vmeff']
    d = dict()
    #时间段传一个 类似 05:09:01 就能够判断时间
    good = df[startTime<df["times"]]
    goods = good[good["times"]<=endTime]
    print df['pgpgin'].tolist()

    print "==============="

    dates = pd.date_range('201404151510',periods=1,freq='M');
    df1 = pd.read_csv(r'/Users/KiddoMa/Documents/pgpginout.csv',encoding='utf-8',index_col=dates)
    print df1
    # print good['times']
    # print good['pgpgin'].tolist()
    # print goods["times"].tolist()
    # print goods
    # for name in name_list:
    #     d[name] = df[name].tolist()
    # print json.dumps(d)
except Exception as e:
    print e



# df = pd.read_csv(r'/Users/KiddoMa/Documents/pgpginout.csv',encoding='utf-8')
#
# s = r'pgpgin/s'.decode('utf-8')
# s1 = r'pgpgout/s'.decode('utf-8')
# time = r'time'
#
# print type(df[s].values[1])
# print type(df[s1].values[1])
