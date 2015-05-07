# coding=utf-8
__author__ = 'KiddoMa'


import json

fr = open('../config/message.json','r+w')
s = json.load(fr)
print s['server2']
s['server2']['ip'] = '10.10.10.4'
ss = json.dumps(s)
fr.write(ss)
fr.close()

# fw = open('../config/message.json','w')
# fw.write(ss)
# fw.close()

# f = file('../config/message.json')
#
# s = json.load(f)w
# print s['server2']
# print s['server2']['ip']
#
#
# s['server2']['ip'] = '10.10.10.3'



# print s['server2']['ip']