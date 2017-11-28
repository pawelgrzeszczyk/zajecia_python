#wyjatki

#print 1/0
# slownik = {}
# print slownik['test']

# lista = []
# print lista[2]

# def devide(x,y):
#     try:
#         result = x/y
#     except (ZeroDivisionError, TypeError) as ex:
#         print ex
#         #print "dzielenie przez zero"
#     else:
#         print "brak wyjatku"
#         return result
#     finally:
#         print "koniec"
#
# print devide(0,'test')

# class Wyjatek(Exception):
#     pass
# try:
#     raise Wyjatek("wyjatek")
# except Wyjatek as w:
#     print w

#get http
# import urllib2
# response = urllib2.urlopen('http://python.org')
# html = response.read()
# print html

#parsowanie XML
from xml.dom import minidom

xml = '''<?xml version="1.0"?>
<mdomtest>
    <el id ="1">
        <test>T1</test>
    </el>
    <el id ="2">
        <test>T2</test>
    </el>
</mdomtest>'''
print xml
doc = minidom.parseString(xml)
els = doc.getElementsByTagName("el")
for el in els:
    sid = el.getAttribute("id")
    print sid
    test = el.getElementsByTagName("test")[0].firstChild.data
    print ("id: %s. val: %s") % (sid, test)