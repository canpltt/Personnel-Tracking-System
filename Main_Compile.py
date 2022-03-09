from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from Main import Ui_MainWindow  #from sayfa.py import method yaparak sayfayı dail ediyoruz
from User_Registry_Compile import Personel_Kayit
from Camera_Page_Compile import Kamera_Kayit
from Camera_Watch_Compile import Kamera_Izle
from Report_Compile import Rapor_Goruntule

class AnaSafanın(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.kayit = Personel_Kayit()
        self.kamera_kayit = Kamera_Kayit()
        self.kamera_izle = Kamera_Izle()
        self.rpr=Rapor_Goruntule()

        self.ui.personelKaydetme.clicked.connect(self.PersonelKayit)
        self.ui.kameraKaydetme.clicked.connect(self.KameraKayit)
        self.ui.kameraIzleme.clicked.connect(self.KameraIzle)
        self.ui.rapor.clicked.connect(self.Rapor)
        


    def PersonelKayit(self):
        self.hide()
        self.kayit.show()

    def KameraKayit(self):
        self.hide()
        self.kamera_kayit.show()

    def KameraIzle(self):
        self.hide()
        self.kamera_izle.show()

    def Rapor(self):
        self.hide()
        self.rpr.show()