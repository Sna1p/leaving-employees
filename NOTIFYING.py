# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'un2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import notif
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StaffList(object):
    def setupUi(self, StaffList):
        StaffList.setObjectName("StaffList")
        StaffList.setEnabled(True)
        StaffList.resize(620, notif.Space[0] + notif.Space[len(notif.Space) - 1])
        self.centralwidget = QtWidgets.QWidget(StaffList)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, 20, 615, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        # Цикл для добавления новых лейблов если сотруднико
        # уходит больше одного 

        for i in range (0, len(notif.FiredList)):
            if i > 0:
                self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser.setGeometry(QtCore.QRect(1, notif.Space[i], 620, 35))
                self.textBrowser.setFont(font)
                self.textBrowser.setText(f"[{notif.FiredNameList[i]}  --->  {notif.FiredList[i].replace('-', '.')}]")
                self.textBrowser.setObjectName("textBrowser_{}".format(i + 1))
            
                '''elif i == 4:
                y += 100
                self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser.setGeometry(QtCore.QRect(1, y, 620, 35))
                self.textBrowser.setFont(font)
                self.textBrowser.setText(f"[{i}]")
                self.textBrowser.setObjectName("textBrowser_{}".format(i + 1))'''
            else:
                self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
                self.textBrowser.setGeometry(QtCore.QRect(1, 70, 620, 35))
                self.textBrowser.setFont(font)
                self.textBrowser.setText(f"[{notif.FiredNameList[i]}  --->  {notif.FiredList[i].replace('-', '.')}]")
                self.textBrowser.setObjectName("textBrowser_{}".format(i + 1))
        
        '''self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1, 70, 620, 35))
        self.textBrowser.setFont(font)
        self.textBrowser.setText(f"1")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1, 115, 620, 35))
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setText(f"2")
        self.textBrowser_2.setObjectName("textBrowser_2")
        

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1, 160, 620, 35))
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setText(f"3")
        self.textBrowser_3.setObjectName("textBrowser_3")'''
        
        StaffList.setCentralWidget(self.centralwidget)
        self.retranslateUi(StaffList)
        QtCore.QMetaObject.connectSlotsByName(StaffList)

    def retranslateUi(self, StaffList):
        _translate = QtCore.QCoreApplication.translate
        StaffList.setWindowTitle(_translate("StaffList", "Список уходящих сотрудников"))
        self.label.setText(_translate("StaffList", "Список сотрутников которые ЗАВТРА уходят и нужно забрать пропуск"))
