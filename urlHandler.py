# coding=utf-8
__author__ = 'KiddoMa'



import tornado
import pandas as pd
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'KiddoMa'

class showHandler(tornado.web.RequestHandler):
    def get(self):
        pass

class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class showHandler1(tornado.web.RequestHandler):
    def get(self):
        pass

class getDataHandler1(tornado.web.RequestHandler):
    def post(self):
        startTime = self.get_argument('startTime')[-8:0];
        endTime = self.get_argument('endTime')[-8:0];
        print startTime
        print endTime
        try:
            df = pd.read_csv(r'/Users/KiddoMa/Documents/pgpginout.csv',encoding='utf-8')
            name_list = [r'times',r'pgpgin',r'pgpgout',r'fault',r'majflt',r'pgfree',r'pgscank',r'pgscand',r'pgsteal',r'vmeff']
            d = dict()
            # df1 = df[df["times"]>startTime]
            # df2 = df1[df1["times"]<endTime]
            for name in name_list:
                d[name] = df[name].tolist()
            self.write(json.dumps(d))
        except Exception as e:
            print e

class getDataHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            #以UTF-8的形式读取拉取到监控结果文件
            df = pd.read_csv(r'/Users/KiddoMa/Documents/pgpginout.csv',encoding='utf-8')
            #创建一个dict,用来保存从文件中拉取到得结果
            d = dict()
            dataList = json.loads(self.get_argument('dataList'))
            print dataList
            #根据前面JS传过来的datalist,返回对应的数据
            #datalist中放的是需要的数据的表头的名称
            for name in dataList:
                #把数据取出来,变成list,放进字典中
                d[name] = df[name].tolist()
            #将结果写到response中
            self.write(json.dumps(d))
            print json.dumps(d)
        except Exception as e:
            print e



