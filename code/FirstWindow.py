import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from SecondWindow import SecondWindow

form_class = uic.loadUiType("../ui/window1.ui")[0]
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("대건네컷")
        self.StartButton.clicked.connect(self.LoadNextWindow)
        

    def LoadNextWindow(self) :
        self.hide() #메인 윈도우 숨김
        self.second = SecondWindow()
        self.second.exec() # 두번째창 닫을때까지 기다림
        self.show()
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MyWindow()
    window.showMaximized()
    app.exec_()
            

    