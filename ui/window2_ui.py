# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window2.ui'
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
        Dialog.setStyleSheet(u"image: url(:/newPrefix/Windows (2).png)")
        self.Type2 = QPushButton(Dialog)
        self.Type2.setObjectName(u"Type2")
        self.Type2.setGeometry(QRect(960, 0, 960, 540))
        self.Type2.setStyleSheet(u"image: none;\n"
"border: none;\n"
"")
        self.Type1 = QPushButton(Dialog)
        self.Type1.setObjectName(u"Type1")
        self.Type1.setGeometry(QRect(0, 0, 960, 540))
        self.Type1.setStyleSheet(u"image: none;\n"
"border: none;")
        self.Type3 = QPushButton(Dialog)
        self.Type3.setObjectName(u"Type3")
        self.Type3.setGeometry(QRect(0, 540, 960, 540))
        self.Type3.setStyleSheet(u"image: none;\n"
"border: none;\n"
"")
        self.Type4 = QPushButton(Dialog)
        self.Type4.setObjectName(u"Type4")
        self.Type4.setGeometry(QRect(960, 540, 960, 540))
        self.Type4.setStyleSheet(u"image: none;\n"
"border: none;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Type2.setText("")
        self.Type1.setText("")
        self.Type3.setText("")
        self.Type4.setText("")
    # retranslateUi

