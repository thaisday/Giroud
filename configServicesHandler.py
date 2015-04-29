# coding=utf-8
import tornado

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
            self.render('configServices.html',ipList=ipList)
        except Exception as e:
            print e