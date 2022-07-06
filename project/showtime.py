# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showtime.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(629, 401)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setLineWidth(9)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 200, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_2.setLineWidth(9)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(200, 320, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton.clicked.connect(self.show)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def show(self):
        dt = datetime.datetime.now()
        self.textBrowser.setText("Date:- %s:%s:%s" %(dt.day, dt.month, dt.year))
        self.textBrowser_2.setText("Time:- %s:%s:%s" %(dt.hour, dt.minute, dt.second))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_16.setText(_translate("Form", "Show Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
