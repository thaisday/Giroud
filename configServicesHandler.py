# coding=utf-8
import tornado
from tornado import template

__author__ = 'KiddoMa'


from xml.etree import ElementTree

class getServersHandler(tornado.web.RequestHandler):
    #获取所有配置的服务器列表
    def get(self):
        try:
            root = ElementTree.fromstring(open('./config/configServices.xml').read())
            ipList = {}
            for name in root.find('servers').getchildren():
                ipList[name.getchildren()[0].text] = name.getchildren()[1].text
            loader = template.Loader('./template')
            self.write(loader.load('serversCheckbox.html').generate(ipList=ipList))
        # self.write(loader.load('result.html').generate(resultList=resultList))
        #     self.render('serversCheckbox.html',ipList=ipList)
        except Exception as e:
            print e

class getTestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')