import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import*
def kirmiziMetin():
    metin.setText('<center><font color="red">taş</font></center>')
def maviMetin():
    metin.setText('<center><font color="blue">kağıt</font></center>')
uyg=QApplication(sys.argv)
pencere=QWidget()
İzgara=QGridLayout()
metin=QLabel("yönetim bilişim sistemleri")
buttonKirmizi=QPushButton("Kirmizi")
pencere.connect(buttonKirmizi,SIGNAL('pressed()'),kirmiziMetin)
buttonMavi=QPushButton("mavi")
pencere.connect(buttonMavi,SIGNAL('pressed()'),maviMetin)
İzgara.addWidget(metin,0,1,2,1)
İzgara.addWidget(buttonKirmizi,0,0)
İzgara.addWidget(buttonMavi,1,0)
pencere.setFixedSize(500,300)
pencere.setLayout(İzgara)
pencere.show()
uyg.exec()


