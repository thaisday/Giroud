# coding=utf-8
__author__ = 'KiddoMa'


import os
import tornado.web
import url

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "template"),
    static_path = os.path.join(os.path.dirname(__file__), "css"),
)

application = tornado.web.Application(url.url,**settings)