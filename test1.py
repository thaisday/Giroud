# coding=utf-8
__author__ = 'KiddoMa'
from xml.etree import ElementTree

def test():
    try:
        root = ElementTree.fromstring(open('./config/Services.xml').read())

        for name in root.find('servers').getchildren():
            print name.getchildren()[0].text
            print name.getchildren()[1].text
    except Exception as e:
        print e


if __name__ == '__main__':
    test()