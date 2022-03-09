# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kamera_izle.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KameraIzle(object):
    def setupUi(self, KameraIzle):
        KameraIzle.setObjectName("KameraIzle")
        KameraIzle.setFixedSize(788, 433)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("camera_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KameraIzle.setWindowIcon(icon)
        KameraIzle.setStyleSheet("background-image : url(back3.jpg);")
        KameraIzle.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(KameraIzle)
        self.centralwidget.setObjectName("centralwidget")
        self.geriGel = QtWidgets.QPushButton(self.centralwidget)
        self.geriGel.setGeometry(QtCore.QRect(690, 0, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.geriGel.setFont(font)
        self.geriGel.setStyleSheet("border:2px solid;\n"
                                   "background:rgba(134, 134, 134, 50%);")
        self.geriGel.setObjectName("geriGel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background:transparent")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 551, 351))
        self.tableWidget.setStyleSheet("border:1px solid;\n"
                                       "background:rgba(207, 207, 207, 0%);\n"
                                       "")
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(590, 110, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border:1px solid;\n"
                                    "background:rgba(207, 207, 207, 50%);")
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:3px solid;\n"
                                      "background:rgba(167, 167, 167, 50%);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "border-top-color:black;\n"
                                      "color:black")
        self.pushButton.setObjectName("pushButton")
        KameraIzle.setCentralWidget(self.centralwidget)

        self.retranslateUi(KameraIzle)
        QtCore.QMetaObject.connectSlotsByName(KameraIzle)

    def retranslateUi(self, KameraIzle):
        _translate = QtCore.QCoreApplication.translate
        KameraIzle.setWindowTitle(_translate("KameraIzle", "Kamera İzle"))
        self.geriGel.setText(_translate("KameraIzle", "Geri Gel"))
        self.label.setText(_translate("KameraIzle", "KAMERA İZLE"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("KameraIzle", "Kamera Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("KameraIzle", "Kamera Yolu"))
        self.label_2.setText(_translate("KameraIzle", "KAMERALAR"))
        self.pushButton.setText(_translate("KameraIzle", "İzle"))
