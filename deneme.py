import sys
from PyQt4.QtGui import*
uyg=QApplication(sys.argv)
pencere=QWidget()
goruntulenen=QLineEdit()
hesaplanan=QLineEdit()
ekle=QPushButton("ekle")
hesapla=QPushButton("hesapla")
sonuc=QLabel("Buraya sonuc yazılacak")
solKutu=QVBoxLayout()
sagkutu=QVBoxLayout()
ortalama=QHBoxLayout()
solKutu.addWidget(goruntulenen)
solKutu.addWidget(ekle)
sagKutu.addWidget(hesaplanan)
sagKutu.addWidget(hesapla)
sagKutu.addWidget(sonuc)
ortalama.addLayout(solKutu)
ortalama.addLayout(sagKutu)
pencere.setLayout(ortalama)
pencere.show()
uyg.exec_
