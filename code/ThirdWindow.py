from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import components.VideoCaptureTest as VC
from FourthWindow import FourthWindow
from threading import Thread


New = uic.loadUiType("../ui/window3.ui")[0]
class ThirdWindow(QDialog,QWidget,New):
    def __init__(self, Type:int):
        super().__init__()
        self.setupUi(self)
        self.n=0
        self.L = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8]
        
        self.Type = Type
        print(Type)
        self.pushButton.clicked.connect(self.Capture)
    
    def Capture(self) :
        if self.n == 8 :
            self.hide() #메인 윈도우 숨김
            self.Fourth = FourthWindow(self.Type)
            self.Fourth.exec() # 네 번째창 닫을때까지 기다림
        else :
            VC.StartCapturing(self.n)
        self.StartCapturing()
        self.n += 1

    def StartCapturing (self) :
        try:
            image = QImage(f"../src/Picture{self.n}.jpg")
            pixmap = QPixmap.fromImage(image).scaledToWidth(250)
            self.L[self.n].setPixmap(pixmap)
        except IndexError :
            pass
        
        
        
        
        