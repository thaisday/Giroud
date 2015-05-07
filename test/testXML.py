# coding=utf-8
__author__ = 'KiddoMa'


from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element


try:
    tree = ET.parse("../config/Services.xml")
    root = tree.getroot()
except Exception as e:
    print e

servers = root.find("servers")
print servers
children = servers.getchildren()
print children

# servers.remove(children[0])
server = Element(tag='server',attrib={})

ip = Element(tag='ip',attrib={})
ip.text = '111.222.333.4444'

status = Element(tag='status',attrib={})
status.text = 'Y'


server.append(ip)
server.append(status)
servers.append(server)
tree.write("../config/Services.xml")
print children
#
# elements = root.find("servers").findall("server")
#
# for eachEle in elements:
#     print eachEle[1].text
#     eachEle[1].text = "Y"
#
# tree.write("../config/Services.xml")
#
# print "================="
#
# for eachEle in elements:
#     print eachEle[1].text