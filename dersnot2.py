import sys
from PyQt4.QtGui import *
uyg=QApplication(sys.argv)
pencere=QWidget()
etiket=QLabel('<font size=5>YBS</font>')
dugme=QPushButton("tıkla")
kutu=QVBoxLayout()
kutu.addWidget(etiket)
kutu.addWidget(dugme)
pencere.setLayout(kutu)
pencere.resize(400,200)
pencere.setWindowTitle("programım")
pencere.show()
etiket.show()
uyg.exec_()

