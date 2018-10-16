from PyQt4.QtGui import *
from PyQt4.QtCore import*
class maliyethesaplama(QDialog):
    def __init__(self,ebeveyn=None):
        super(maliyethesaplama,self).__init__(ebeveyn)
#Grid Layout tanımlandı
        grid=QGridLayout()
#sabit maliyet Label Eklendi
        grid.addWidget(QLabel("sabitmaliyet"),0,0)
#Sabit Maliyet Text input tanımlandı ve eklendi
        self.sabitMaliyet=QLineEdit()
        grid.addWidget(self.sabitMaliyet,0,1)
#Değişken Maliyet Label Eklendi
        grid.addWidget(QLabel("degisken Maliyet:"),1,0)
#Değişken Maliyet Text input tanımlandı
        self.degiskenMaliyet=QLineEdit()
        grid.addWidget(self.degiskenMaliyet,1,1)
#yatırımın ekonomik yılı label eklendi
        grid.addWidget(QLabel("Yatırım ekonomik yılı"),2,0)
#yatırım yılı döner kutusu eklendi
        self.yatirimyili=QSpinBox()
        self.yatirimyili.setRange(1,10)
        self.yatirimyili.setValue(1)
        grid.addWidget(self.yatirimyili,2,1)
#toplam gelir label eklendi
        grid.addWidget(QLabel("Toplam gelir"),3,0)
        self.toplamGelir=QLabel("")
        grid.addWidget(self.toplamGelir,3,1)
#toplam gelir input eklendi
        grid.addWidget(QLabel("sirketin durumu"),4,0)
#şirketin durumu label eklendi
        self.sirketDurum=QLabel("")
        grid.addWidget(self.sirketDurum,4,1)
#buton eklendi       
        hesaplam=QPushButton("Hesapla")
        grid.addWidget(hesaplam,5,1)
        self.connect(hesaplam,SIGNAL('pressed()'),self.hesapla)
#grid Layout set etdildi
        self.setLayout(grid)
#program başlık
        self.setWindowTitle("maliyet hesaplama")
        self.resize(500,150)
    def hesapla(self):
        sm=int(self.sabitMaliyet.text())
        dm=int(self.degiskenMaliyet.text())
        yy=int(self.yatirimyili.text())
        tgider=sm+(dm*yy)
        self.toplamGelir.setText('<font color="blue"><b>%0.1</b></font>'"yüzde" ,tgider)
        tgelir=15000
        kar=tgelir-tgider
        if kar>0:
            self.sirketDurum.setText("şirketiniz kar etmiştir")
        elif(kar<0):
            self.sirketDurum.setText("şirket zarar etmiştir")
        else:
            self.sirketDurum.setText("şirket başa baş notkasında")
                            
uygulama=QApplication([])
pencere=maliyethesaplama()
pencere.show()
uygulama.exec_

        
