# coding=utf-8
__author__ = 'KiddoMa'

import sys

from urlHandler import *
from ServicesHandler import *

reload(sys)

url = [
    (r'/', indexHandler),
    (r'/result', showHandler),
    (r'/result1', showHandler1),
    (r'/getdata', getDataHandler),
    (r'/getdata1', getDataHandler1),
    (r'/selectServer', selectServersHandler),
    (r'/configService', configServersHandler),
    (r'/test', getTestHandler),
]