import bs4 as bs
import urllib.request
import sqlite3
kaynak=urllib.request.urlopen("http://www.milliyet.com").read()
sayfa=bs.BeautifulSoup(kaynak,'lxml')
print(sayfa.title.string)
print(sayfa.findAll('p'))
for paragraf in sayfa.findAll('p'):
    print(paragraf.string)
