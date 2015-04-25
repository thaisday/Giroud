# coding=utf-8
import json

__author__ = 'KiddoMa'


import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#此时读取的时候,已经解析成unicode流处理,所以后面的处理都应该依照unicode来处理
s = '\tproductOrderNo'
fee = '手续费'.decode('utf-8')
df = pd.read_csv(r'/Users/KiddoMa/Downloads/对账2015-03-25至2015-03-26.csv',encoding='gbk')

# s = '\tproductOrderNo'
#内部处理还是依靠unicode
s1 = '订单金额'.decode('utf-8')#.encode('gbk')

fee = '手续费'.decode('utf-8')

# print pd.pivot_table(df,index=[s1],values=[fee])
# print type(df[fee])
# print df
# print df[fee]
# print df[s].values

a = ["pgpgin","pgpgout"]
b = json.dumps(a)
print b
