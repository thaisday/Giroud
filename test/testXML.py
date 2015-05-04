# coding=utf-8
__author__ = 'KiddoMa'


from xml.etree import ElementTree as ET

try:
    tree = ET.parse("../config/configServices.xml")
    root = tree.getroot()
except Exception as e:
    print e

elements = root.find("servers").findall("server")

for eachEle in elements:
    print eachEle[1].text
    eachEle[1].text = "Y"

tree.write("../config/configServices.xml")

print "================="

for eachEle in elements:
    print eachEle[1].text