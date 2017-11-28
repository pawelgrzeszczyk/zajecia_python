#Napisz program ktory pobiera dokument html i zapisuje go na dysku


import urllib2
response = urllib2.urlopen('https://www.blog.pythonlibrary.org/feed/')
html = response.read()
open("plik.xml","w").write(html)