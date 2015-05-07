# coding=utf-8
__author__ = 'KiddoMa'


import json


def getServersList():
    try:
        fp = open('./config/message.json','r')
        s = json.load(fp)
        return s
    except Exception as e:
        print e
    finally:
        fp.close()

def saveServersList(serversList):
    try:
        fp = open('./config/message.json','r+w')
        s = json.load(fp)
        print serversList
        for key in serversList.keys():
            for i in s['server']:
                if s['server'][i]['ip'] == key:
                    s['server'][i]['monitorStatus'] = serversList[key]
        fp.write(s)
    except Exception as e:
        print e
    finally:
        fp.close()


# serverList = getServersList()
# print serverList
# print serverList['server']
# print serverList['server'][0]