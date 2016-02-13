# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Mon Jan 18 10:39:25 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_titel(object):
    def setupUi(self, titel):
        titel.setObjectName("titel")
        titel.setEnabled(True)
        titel.resize(551, 390)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(titel.sizePolicy().hasHeightForWidth())
        titel.setSizePolicy(sizePolicy)
        titel.setMinimumSize(QtCore.QSize(551, 390))
        titel.setMaximumSize(QtCore.QSize(551, 379))
        titel.setBaseSize(QtCore.QSize(551, 379))
        self.centralwidget = QtGui.QWidget(titel)
        self.centralwidget.setObjectName("centralwidget")
        self.laden_button = QtGui.QPushButton(self.centralwidget)
        self.laden_button.setGeometry(QtCore.QRect(10, 340, 110, 41))
        self.laden_button.setObjectName("laden_button")
        self.speichern_button = QtGui.QPushButton(self.centralwidget)
        self.speichern_button.setGeometry(QtCore.QRect(430, 340, 110, 41))
        self.speichern_button.setObjectName("speichern_button")
        self.textarea = QtGui.QPlainTextEdit(self.centralwidget)
        self.textarea.setGeometry(QtCore.QRect(0, 0, 551, 331))
        self.textarea.setObjectName("textarea")
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(130, 350, 291, 20))
        self.status.setText("")
        self.status.setObjectName("status")
        titel.setCentralWidget(self.centralwidget)

        self.retranslateUi(titel)
        QtCore.QMetaObject.connectSlotsByName(titel)

    def retranslateUi(self, titel):
        titel.setWindowTitle(QtGui.QApplication.translate("titel", "CSV-IO - Jakub Kopec", None, QtGui.QApplication.UnicodeUTF8))
        self.laden_button.setText(QtGui.QApplication.translate("titel", "Laden", None, QtGui.QApplication.UnicodeUTF8))
        self.speichern_button.setText(QtGui.QApplication.translate("titel", "Speichern", None, QtGui.QApplication.UnicodeUTF8))

