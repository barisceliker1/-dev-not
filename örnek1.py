import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import*

uyg=QApplication(sys.argv)
pencere=QWidget()
İzgara=QGridLayout()

sabit=QLabel("Sabit Maliyet")
degiskenma=QLabel("Degisken maliyet")
yatırımınekonomik=QLabel("Ekonomik ömür")
toplam=QLabel("Toplam gelir")
gelirmikt=QLabel("5000 TL'dir")
durum=QLabel("durum:")
kar=QLabel("şirket/kar/zarar noktasındadır")


degisken=QLineEdit("")
sabitmaliyet=QLineEdit("")
eko=QLineEdit("")
buton=QPushButton("hesapla")                 

                 

İzgara.addWidget(sabit,0,0)
İzgara.addWidget(degiskenma,1,0)
İzgara.addWidget(yatırımınekonomik,2,0)
İzgara.addWidget(toplam,3,0)
İzgara.addWidget(gelirmikt,3,1)
İzgara.addWidget(durum,5,0)
İzgara.addWidget(kar,5,1)

İzgara.addWidget(sabitmaliyet,0,1)
İzgara.addWidget(degisken,1,1)
İzgara.addWidget(eko,2,1)

İzgara.addWidget(buton,6,1)



pencere.setFixedSize(500,150)

pencere.setLayout(İzgara)
pencere.show()
uyg.exec()
