# coding=utf-8
import tornado
from tornado import template

__author__ = 'KiddoMa'


from xml.etree import ElementTree

class getServersHandler(tornado.web.RequestHandler):
    #获取所有配置的服务器列表
    def get(self):
        try:
            #读取XML文件的根目录
            root = ElementTree.fromstring(open('./config/configServices.xml').read())
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

    def post(self):
        try:
            tree = ElementTree.parse('./config/configServices.xml')
            root = tree.getroot()
        except Exception as e:
            print e
        elements = root.find("servers").findall("server")
        for element in elements:
            element[1].text = self.get_argument(element[0].text)
        tree.write('./config/configServices.xml')



class getTestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')