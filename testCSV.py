# coding=utf-8
__author__ = 'KiddoMa'

import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


df = pd.read_csv(r'/Users/KiddoMa/Documents/pgpginout.csv',encoding='utf-8')

s = r'pgpgin/s'.decode('utf-8')
s1 = r'pgpgout/s'.decode('utf-8')
time = r'time'



print type(df[s].values[1])
print type(df[s1].values[1])
