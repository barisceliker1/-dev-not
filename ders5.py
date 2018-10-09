import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import*
uyg=QApplication(sys.argv)
pencere=QWidget()
izgara=QGridLayout()
metin=QLabel("GideceğinizYol")
Yakit=QLabel("yakıt litre")
kmyakit=QLabel("100 km de tüketilen yakıt")


Yol=QLineEdit("")
Yakit2=QLineEdit("")
kmyak=QLineEdit("")

buttonKirmizi=QPushButton("hesaplama")

izgara.addWidget(metin,0,0)
izgara.addWidget(Yakit,1,0)
izgara.addWidget(kmyakit,2,0)

izgara.addWidget(Yol,0,1)
izgara.addWidget(Yakit2,1,1)
izgara.addWidget(kmyak,2,1)

izgara.addWidget(buttonKirmizi,5,1)
pencere.setFixedSize(300,200)
pencere.setLayout(izgara)
pencere.show()
uyg.exec()
