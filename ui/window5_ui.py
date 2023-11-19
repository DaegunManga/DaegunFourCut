# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window5.ui'
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
        Dialog.setStyleSheet(u"image:url(:/newPrefix/Windows (1).png)")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1578))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: skyblue;\n"
"font-weight: bold;\n"
"font-size: 100px;\n"
"color: red;")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(560, 40, 781, 451))
        font1 = QFont()
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"image: none;\n"
"border: none;\n"
"color: red;\n"
"font-size: 150px;\n"
"")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 180, 351, 531))
        self.label_2.setStyleSheet(u"image: none;\n"
"border: none;\n"
"")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1320, 180, 351, 531))
        self.label_3.setStyleSheet(u"image: none;\n"
"border: none;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\uc791\uc5c5\uc744 \uc131\uacf5\uc801\uc73c\ub85c \uc218\ud589\ud588\uc2b5\ub2c8\ub2e4.", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"HOME", None))
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

