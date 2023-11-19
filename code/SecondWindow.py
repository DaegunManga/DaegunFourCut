from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from ThirdWindow import ThirdWindow


New = uic.loadUiType("../ui/window2.ui")[0]
class SecondWindow(QDialog,QWidget,New):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Type1.clicked.connect(self.Type1_def)
        self.Type2.clicked.connect(self.Type2_def)
        self.Type3.clicked.connect(self.Type3_def)
        self.Type4.clicked.connect(self.Type4_def)
    
    def Type1_def (self) :
        self.hide() #메인 윈도우 숨김
        self.Third = ThirdWindow(1)
        self.Third.exec() # 세 번째창 닫을때까지 기다림
    
    def Type2_def (self) :
        self.hide() #메인 윈도우 숨김
        self.Third = ThirdWindow(2)
        self.Third.exec() # 세 번째창 닫을때까지 기다림
        
    def Type3_def (self) :
        self.hide() #메인 윈도우 숨김
        self.Third = ThirdWindow(3)
        self.Third.exec() # 세 번째창 닫을때까지 기다림
        
    def Type4_def (self) :
        self.hide() #메인 윈도우 숨김
        self.Third = ThirdWindow(4)
        self.Third.exec() # 세 번째창 닫을때까지 기다림
        