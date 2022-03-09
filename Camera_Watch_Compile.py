from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from Camera_Watch import Ui_KameraIzle
import pickle
import Main_Compile
from Camera_Watch_Codes import kamerayi_Ac
import Camera_Watch_Codes

class Kamera_Izle(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_KameraIzle()
        self.ui.setupUi(self)

        self.ui.geriGel.clicked.connect(self.geri)
        self.ui.tableWidget.setColumnWidth(0, 160)
        self.ui.tableWidget.setColumnWidth(1, 370)

        file = open('cameras.pkl', 'rb')  # Kamera kayıtlarını al
        cameras = pickle.load(file)
        file.close()
        self.camera_Name_List = []
        self.camera_Adress_List = []
        i=0
        for camera in cameras:  # Kamera kayıtlarını listeye kaydet
            self.ui.tableWidget.setRowCount(len(cameras))
            self.camera_Name_List.append(camera)
            self.camera_Adress_List.append(cameras[camera])
            self.ui.tableWidget.setItem(i,0, QTableWidgetItem(self.camera_Name_List[i]))
            self.ui.tableWidget.setItem(i,1, QTableWidgetItem(self.camera_Adress_List[i]))
            self.ui.comboBox.addItem(self.camera_Name_List[i])
            i+=1
        self.ui.pushButton.clicked.connect(self.yaz)


    def yaz(self):
        self.index=self.camera_Name_List.index(self.ui.comboBox.currentText())
        self.gonder=kamerayi_Ac(self.camera_Adress_List[self.index])
        
        print(self.camera_Adress_List[self.index])
        


    def geri(self):
        self.hide()
        self.ana = Main_Compile.AnaSafanın()
        self.ana.show()
