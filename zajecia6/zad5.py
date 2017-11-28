#Napisz prosty czytnik RSS. Program ma miec mozliwsc zapamietywania ulubiuonych kanalow.
#Wiadomosci powinny byc czytelnie sformatowane
import urllib2
from xml.dom import minidom



def pobierzRss(strona):
    try:
        rss = urllib2.urlopen(strona)
        html = rss.read()
        dom = minidom.parseString(html)
        print 'Wiadomosci z ' + strona
        parsujRSS(dom)
    except Exception as ex:
        print ex
        print 'Odnosnik nie jest RSS-em lub nie moge go otworzyc.'

def parsujRSS(dom):
    chanel = dom.getElementsByTagName("channel")
    for c in chanel:
        items = c.getElementsByTagName("item")
        for i in range(len(items)):
            title = items[i].getElementsByTagName("title")
            link = items[i].getElementsByTagName("link")
            for j in range(len(title)):
                wiadomosc = title[j].firstChild.data+' link: '+link[j].firstChild.data
                print ("%s") % wiadomosc

pobierzRss('https://www.blog.pythonlibrary.org/feed/')
