# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deneme.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(456, 478)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image : url(back.jpg);")
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.personelKaydetme = QtWidgets.QPushButton(self.centralwidget)
        self.personelKaydetme.setEnabled(True)
        self.personelKaydetme.setGeometry(QtCore.QRect(88, 35, 280, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.personelKaydetme.setFont(font)
        self.personelKaydetme.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.personelKaydetme.setStyleSheet("border:3px solid;\n"
                                            "background:rgba(167, 167, 167, 50%);\n"
                                            "border-top-color:black;\n"
                                            "color:black;")
        self.personelKaydetme.setObjectName("personelKaydetme")
        self.kameraKaydetme = QtWidgets.QPushButton(self.centralwidget)
        self.kameraKaydetme.setGeometry(QtCore.QRect(88, 145, 280, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kameraKaydetme.setFont(font)
        self.kameraKaydetme.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.kameraKaydetme.setStyleSheet("border:3px solid;\n"
                                          "background:rgba(167, 167, 167, 50%);\n"
                                          "border-top-color:black;\n"
                                          "color:balck\n"
                                          "")
        self.kameraKaydetme.setObjectName("kameraKaydetme")
        self.kameraIzleme = QtWidgets.QPushButton(self.centralwidget)
        self.kameraIzleme.setGeometry(QtCore.QRect(88, 255, 280, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kameraIzleme.setFont(font)
        self.kameraIzleme.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.kameraIzleme.setStyleSheet("border:3px solid;\n"
                                        "background:rgba(167, 167, 167, 50%);\n"
                                        "border-top-color:black;\n"
                                        "color:black")
        self.kameraIzleme.setObjectName("kameraIzleme")
        self.rapor = QtWidgets.QPushButton(self.centralwidget)
        self.rapor.setGeometry(QtCore.QRect(88, 365, 280, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rapor.setFont(font)
        self.rapor.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.rapor.setStyleSheet("border:3px solid;\n"
                                 "background:rgba(167, 167, 167, 50%);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-top-color:black;\n"
                                 "color:black")
        self.rapor.setObjectName("rapor")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ana Sayfa"))
        self.personelKaydetme.setText(_translate("MainWindow", "Personel Kayıt"))
        self.kameraKaydetme.setText(_translate("MainWindow", "Kamera Kaydetme"))
        self.kameraIzleme.setText(_translate("MainWindow", "Kamera İzleme"))
        self.rapor.setText(_translate("MainWindow", "Raporlar"))
