# coding=utf-8
import tornado
from tornado import template

__author__ = 'KiddoMa'


from xml.etree import ElementTree
import ServersDao
import json

class selectServersHandler(tornado.web.RequestHandler):
    #获取已经配置的服务器列表
    def get(self):
        try:
            serversList = ServersDao.getServersList()
            loader = template.Loader('./template')
            self.write(loader.load('selectServices.html').generate(serversList=serversList))
        except Exception as e:
            print e

    #保存选择的服务器列表
    def post(self):
        try:
            serversList = json.loads(self.get_argument('servers'))
            print type(serversList)
            ServersDao.saveServersList(serversList=serversList)
        except Exception as e:
            print e



    # def post(self):
    #     try:
    #         tree = ElementTree.parse('./config/Services.xml')
    #         root = tree.getroot()
    #     except Exception as e:
    #         print e
    #     elements = root.find("servers").findall("server")
    #     for element in elements:
    #         element[1].text = self.get_argument(element[0].text)
    #     tree.write('./config/Services.xml')


class configServersHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            #读取XML文件的根目录
            root = ElementTree.fromstring(open('./config/Services.xml').read())
            #初始化返回的Model
            ipList = {}
            #遍历循环servers节点下所有的子节点,即所有的server节点
            for name in root.find('servers').getchildren():
                #用ip作为key,status作为value,存储在iplist中
                #TODO
                #此处可以优化,key和value的值可以商榷
                ipList[name.getchildren()[0].text] = name.getchildren()[1].text
            #创建一个模板的读取
            loader = template.Loader('./template')
            #将给定的数据用模板渲染之后,将输出流写到response的responseText
            self.write(loader.load('configServices.html').generate(ipList=ipList))
        except Exception as e:
            print e

    #用作更新配置服务器
    def post(self):
        try:
            tree = ElementTree.parse('./config/Services.xml')
            root = tree.getroot()
        except Exception as e:
            print e
        #1.删除所有的节点
        #2.新增推送过来的节点

        #拿到推送过来的servers数组
        servers = self.get_argument('servers')

        elements = root.find("servers").findall("server")
        for element in elements:
            element[1].text = self.get_argument(element[0].text)

        tree.write('./config/Services.xml')

class getTestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')