from PyQt5.QtWidgets import *
from User_Registry_Page import Ui_Personel
import Main_Compile
from User_Registry import kullanici_Kaydet

class Personel_Kayit(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_Personel()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.yaz)
        self.ui.pushButton_2.clicked.connect(self.geri)
        self.ui.pushFoto.clicked.connect(self.sec)
        self.fname=""

    
    def geri(self):
        self.hide()
        self.ana=Main_Compile.AnaSafanın()
        self.ana.show()

    def sec(self):
        self.fname=QFileDialog.getOpenFileName(self,'Open file','C:/Users/Acer/Desktop','Images(*.PNG *.jpg *.jpeg)')
        print(self.fname[0])
        
        
        
    def yaz(self):
        self.gonder=kullanici_Kaydet(self.ui.lineAd.text(), self.ui.lineSoyad.text(), self.ui.lineTelefon.text(), self.fname[0], self.ui.lineCinsiyet.text(), self.ui.lineTc.text(), self.ui.lineAdres.text())
