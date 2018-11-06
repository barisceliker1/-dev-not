import sqlite3
baglanti=sqlite3.connect('ornek.db')
isaretci=baglanti.cursor()
#sorgu=isaretci.execute('''CREATE TABLE ogrenci(kayit_no INTEGER PRIMARY KEY AUTOINCREMENT,adi VARCHAR(50),soyadi VARCHAR(50),bolum VARCHAR(50))''')
#adi=input("ogrenci adını giriniz")
#soyadi=input("ogrenci soyadi giriniz")
#bolum=input("ogrencinin bolumunu girniz")
#kod başlnagıcı
sorgu=isaretci.execute("SELECT name FROM sqlite_master")
print(sorgu.fetchall())
#kod bitiş
#isaretci.execute('''INSERT INTO ogrenci(adi,soyadi,bolum) VALUES("%s","%s","s")'''%(adi,soyadi,bolum))
#printt(sorgu.fetchall())
#baglanti.row_factory=sqlite3.Row
#isaretci=baglanti.cursor()
#sorgu=isaretci.execute('SELECT * FROM ogrenciler')
#alan adına göre sıralama
#for i in sorgu.fetchall():
#arama=input("aramak istediğimi ogrenci Adını giriniz")
#kod başlangıcı
#sorgu=isaretci.execute('''SELECT * FROM ogrenci WHERE adi LIKE"%(0)%"'''.format(arama))
#for i  in sorgu.fetchall():
    #print(i[0],i[1],i[2])
#kod bitiş                 
     #print(i['Adi'])
#Değişken sıralamasına göre sorgulama
#for i in sorgu.fetchall():
    #print("Adi:%s,Soyadi:%s,Bölümü:%s"%i)
#sorgu=isaretci.execute('''UPDATE ogrenciler SET adi="Mehmet"
#WHERE kayit_no="3"''')
#sorgu=isaretci.execute('''DELETE FROM ogrenciler WHERE kayit_no="2"''')
#sorgu=isaretci.execute('SELECT * From ogrenciler')
#print(sorgu.fetchall())

baglanti.commit()
baglanti.close()

