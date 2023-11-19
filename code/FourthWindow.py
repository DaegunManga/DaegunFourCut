from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import components.ImageCropTest as IC
from FifthWindow import FifthWindow
import components.makeQR as MQ

New = uic.loadUiType("../ui/window4.ui")[0]
class FourthWindow(QDialog,QWidget,New):
    def __init__(self, Type):
        super().__init__()
        self.setupUi(self) 

        self.label_L = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7, self.label_8]
        self.pushButton_L = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8]
        self.def_L = [self.Select_1, self.Select_2, self.Select_3, self.Select_4, self.Select_5, self.Select_6, self.Select_7, self.Select_8]

        self.UploadImage()

        self.Image_L = []

        if Type == 1 or Type == 2 :
            self.limit = 3
        elif Type == 3 or Type == 4 :
            self.limit = 5
        
        self.Type = Type

        for n in range(8) :
            self.pushButton_L[n].clicked.connect(self.def_L[n])    
        
        self.pushButton_9.clicked.connect(self.makeImage)

    def UploadImage (self) :
        for n in range(8) :
            image = QImage(f"../src/Picture{n}.jpg")
            pixmap = QPixmap.fromImage(image).scaledToWidth(250)
            self.label_L[n].setPixmap(pixmap)
    
    def Select_1 (self) :
        button = self.pushButton_L[0] 
        if button.text() == "" :
            if len(self.Image_L) <= self.limit :
                button.setText("Selected")
                self.Image_L.append(0)
        else :
            button.setText("")
            self.Image_L.remove(0)
    def Select_2 (self) :

        button = self.pushButton_L[1] 
        if button.text() == "" :
            if len(self.Image_L) <=self.limit :
                button.setText("Selected")
                self.Image_L.append(1)
        else :
            button.setText("")
            self.Image_L.remove(1)
    def Select_3 (self) :
        button = self.pushButton_L[2] 
        if button.text() == "" :
            if len(self.Image_L) <=self.limit :
                button.setText("Selected")
                self.Image_L.append(2)
        else :
            button.setText("")
            self.Image_L.remove(2)
    def Select_4 (self) :
        button = self.pushButton_L[3] 
        if button.text() == "" :
            if len(self.Image_L) <= self.limit :
                button.setText("Selected")
                self.Image_L.append(3)
        else :
            button.setText("")
            self.Image_L.remove(3)
    def Select_5 (self) :
        button = self.pushButton_L[4] 
        if button.text() == "" :
            if len(self.Image_L) <= self.limit :
                button.setText("Selected")
                self.Image_L.append(4)
        else :
            button.setText("")
            self.Image_L.remove(4)
    def Select_6 (self) :
        button = self.pushButton_L[5] 
        if button.text() == "" :
            if len(self.Image_L) <= self.limit :
                button.setText("Selected")
                self.Image_L.append(5)
        else :
            button.setText("")
            self.Image_L.remove(5)
    def Select_7 (self) :
        button = self.pushButton_L[6] 
        if button.text() == "" :
            if len(self.Image_L) <= self.limit :
                button.setText("Selected")
                self.Image_L.append(6)
        else :
            button.setText("")
            self.Image_L.remove(6)
    def Select_8  (self) :
        button = self.pushButton_L[7] 
        if button.text() == "" :
            if len(self.Image_L) <= self.limit :
                button.setText("Selected")
                self.Image_L.append(7)
        else :
            button.setText("")
            self.Image_L.remove(7)
    
    def makeImage(self) :
        IC.StartCrop(self.Image_L, self.Type)
        MQ.StartMakeQR('https://www.youtube.com/', self.Type)
        self.hide() #메인 윈도우 숨김
        self.Fifth = FifthWindow()
        self.Fifth.exec() # 네 번째창 닫을때까지 기다림


        
        