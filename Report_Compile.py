from PyQt5.QtWidgets import *
from Report_Page import Ui_Rapor
import Main_Compile

class Rapor_Goruntule(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_Rapor()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.geri)
        self.ui.tableWidget.setColumnWidth(0,244)
        self.ui.tableWidget.setColumnWidth(1,235)
        self.ui.tableWidget.setColumnWidth(2,235)


        text_file = open("Logfile.log", "r")
        logs = text_file.readlines()
        text_file.close()

        for i in range(len(logs)):
            bol=logs[i].split('-')
            self.ui.tableWidget.setRowCount(len(logs))
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(bol[3]))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(bol[0]))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(bol[1]))


#****************************************************************************************


    def geri(self):
        self.hide()
        self.ana = Main_Compile.AnaSafanın()
        self.ana.show()