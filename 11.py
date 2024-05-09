import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic # ui를 연결

#ui 파일 연동
from_class =uic.loadUiType("calculator.ui")[0]

class Window(QWidget, from_class):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
if __name__=='__main__':
    app= QApplication(sys.argv)
    myCalc= Window()
    sys,exit(app.exec_())