import bs4 as bs
import urllib.request
import sqlite3
#baglanti=sqlite3.connect("ornek.db")
#isaretci=baglanti.cursor()
#tablo=isaretci.execute('''CREATE TABLE haberler''')
kaynak=urllib.request.urlopen("http://www.milliyet.com").read()
sayfa=bs.BeautifulSoup(kaynak,'lxml')
print(sayfa.title.string)
print(sayfa.findAll('p'))
#p etiketi olan şeylerbuluyor
for paragraf in sayfa.findAll('p'):
    #isaretci.execute('''INSERT INTO haberler(haber)VALUES(?)''',(paragraf.string))
    print(paragraf.string)
    
