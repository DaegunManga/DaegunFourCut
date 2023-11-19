# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window4.ui'
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
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(u"image: url(:/newPrefix/Windows (3).png);")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(451, 191, 250, 349))
        self.pushButton.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 50px;\n"
"")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(701, 191, 250, 349))
        self.pushButton_2.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 50px;\n"
"")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(951, 191, 250, 349))
        self.pushButton_3.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 50px;\n"
"")
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1201, 191, 250, 349))
        self.pushButton_4.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 50px;\n"
"")
        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(451, 541, 250, 349))
        self.pushButton_5.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 50px;\n"
"")
        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(701, 541, 250, 349))
        self.pushButton_6.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 50px;\n"
"\n"
"")
        self.pushButton_7 = QPushButton(Dialog)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(951, 541, 250, 349))
        self.pushButton_7.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 50px;\n"
"\n"
"")
        self.pushButton_8 = QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(1201, 541, 250, 349))
        self.pushButton_8.setStyleSheet(u"border: none;\n"
"image: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 50px;\n"
"")
        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(1510, 10, 401, 191))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"image: none;\n"
"border: none;\n"
"color: red;\n"
"font-weight: bold;\n"
"font-size: 100px;")
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(450, 190, 1001, 701))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_1 = QLabel(self.gridLayoutWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setStyleSheet(u"image: none;\n"
"border: none;\n"
"")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QRect(750, 80, 661, 81))
        font1 = QFont()
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"font-size: 50px;\n"
"color: red;\n"
"image: none;")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QRect(460, 910, 1841, 71))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"font-size: 25px;\n"
"color: red;\n"
"image: none;")
        self.label.raise_()
        self.gridLayoutWidget.raise_()
        self.label_9.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label_10.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"o", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Next >>", None))
        self.label_2.setText("")
        self.label_1.setText("")
        self.label_3.setText("")
        self.label_7.setText("")
        self.label_5.setText("")
        self.label_8.setText("")
        self.label_4.setText("")
        self.label_6.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Select Your Photo ", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Next\ub97c \ub204\ub974\uace0 \uc2dc\uac04\uc774 \uc18c\uc694\ub420 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \ud654\uba74\uc774 \ud558\uc598\uc9c0\ub354\ub77c\ub3c4 \uae30\ub2e4\ub824\uc8fc\uc2dc\uae30 \ubc14\ub78d\ub2c8\ub2e4.", None))
    # retranslateUi

