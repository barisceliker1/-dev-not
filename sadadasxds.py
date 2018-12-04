import bs4 as bs
import urllib.request
import sqlite3
#baglanti=sqlite3.connect("ornek.db")
#isaretci=baglanti.cursor()
#tablo=isaretci.execute('''CREATE TABLE haberler''')
kaynak=urllib.request.urlopen("http://www.milliyet.com").read()
sayfa=bs.beautifulsoup(kaynak,'lxml')
tablo=isaretci.execute('''CREATE TABLE linkler(id INTEGER PRIMARY KEY,link VARCHAR(255))''')

for nav in sayfa.findAll('a'):
    isaretci.execute('''INSERT INTO linkler(link)VALUES(2)''',([nav.get('href')))
                  
    print(nav.get('href'))
print(sayfa.title.string)
print(sayfa.findAll('p'))
#p etiketi olan şeylerbuluyor
for paragraf in sayfa.findAll('p'):
    #isaretci.execute('''INSERT INTO haberler(haber)VALUES(?)''',(paragraf.string))
    print(paragraf.string)
sonuc=isaretci.execute("SELECT*FROM linkler")
print(sonuc.fetchall())
                     
