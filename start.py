# coding=utf-8
__author__ = 'KiddoMa'

import tornado
import tornado.httpserver
from tornado.options import define, options
import application


__author__ = 'KiddoMa'


define('port',default=9906,help='run on the given port',type=int)

def start():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application.application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    start()