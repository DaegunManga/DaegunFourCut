from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication


New = uic.loadUiType("../ui/window5.ui")[0]
class FifthWindow(QDialog,QWidget,New):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.n=0        
        self.pushButton.clicked.connect(self.Exit)
        image = QImage("../src/result.png")
        pixmap = QPixmap.fromImage(image).scaledToWidth(351)
        self.label_2.setPixmap(pixmap)
        self.label_3.setPixmap(pixmap)
    
    def Exit (self) :
        self.close()

        
        
        