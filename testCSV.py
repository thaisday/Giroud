# coding=utf-8
import json

__author__ = 'KiddoMa'

import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    startTime = "05:09:01"
    df = pd.read_csv(r'/Users/KiddoMa/Documents/pgpginout.csv', encoding='utf-8')
    name_list = [r'times', r'pgpgin', r'pgpgout', r'fault', r'majflt', r'pgfree', r'pgscank', r'pgscand', r'pgsteal',
                 r'vmeff']
    d = dict()
    #时间段传一个 类似 05:09:01 就能够判断时间
    good = df[df["times"]>startTime]
    print df['pgpgin'].tolist()
    print "==============="
    print good['times'].tolist()
    print good['pgpgin'].tolist()
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
