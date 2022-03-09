from PyQt5.QtWidgets import *
from Camera_Page import Ui_KameraKayit
import Main_Compile
from Camera_Process import kamerayi_Kaydet

class Kamera_Kayit(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_KameraKayit()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.yaz)
        self.ui.pushButton_4.clicked.connect(self.geri)

    def yaz(self):
        self.gonder=kamerayi_Kaydet(self.ui.lineKameraAd.text(), self.ui.lineIP.text(), self.ui.lineProtokol.text(), self.ui.lineKullanc.text(), self.ui.lineSifre.text(), self.ui.Uzani.text(), self.ui.lineEdit.text())
    def geri(self):
        self.hide()
        self.ana = Main_Compile.AnaSafanın()
        self.ana.show()