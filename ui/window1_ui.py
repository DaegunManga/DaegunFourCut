# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import backgrounds_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1920, 1080)
        Dialog.setStyleSheet(u"image: url(:/newPrefix/Windows (1).png);")
        self.StartButton = QPushButton(Dialog)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(-1, -5, 1920, 1580))
        font = QFont()
        font.setFamily(u"Edwardian Script ITC")
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setCursor(QCursor(Qt.ArrowCursor))
        self.StartButton.setStyleSheet(u"font-size: 150px;\n"
"font-weight: bold;\n"
"color: navy;\n"
"image: none;\n"
"border: none;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.StartButton.setText(QCoreApplication.translate("Dialog", u"Touch To Continue", None))
    # retranslateUi

