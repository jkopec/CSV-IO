import sys

from PySide.QtGui import *

from mvc import model, view

__author__ = 'Jakub Kopec'


class Controller(QMainWindow):

    def __init__(self, parent=None):

        super(Controller,self).__init__(parent)
        self.myForm = view.Ui_titel()
        self.myForm.setupUi(self)
        self.myModel = model.Model()
        self.connectButtons()

    def connectButtons(self):
        self.myForm.laden_button.clicked.connect(lambda: self.click(self.myForm.laden_button.text()))
        self.myForm.speichern_button.clicked.connect(lambda: self.click(self.myForm.speichern_button.text()))

    def click(self,beschriftung):
        text=""
        if beschriftung == "Laden":
            text = self.myModel.loadCSV()
            self.myForm.status.setText("Erfolgreich geladen!")
        elif beschriftung == "Speichern":
            self.myModel.saveCSV(self.myForm.textarea.toPlainText())
            text = self.myModel.loadCSV()
            self.myForm.status.setText("Erfolgreich gespeichert!")
        self.output(text)

    def output(self, text):
        self.myForm.textarea.clear()
        self.myForm.textarea.insertPlainText(text)
