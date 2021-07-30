import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import triangle as ui

class Main(QMainWindow, ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        angle = ui.angle.textEdit.toPlainText()
        length = ui.length.textEdit.toPlainText()
        
        self.pushButton.clicked.connect(lambda: self.CalNum(angle))
    def CalNum(self,angle):
        #angle = float(angle)
        #print(angle)
        #print(type(angle))
        print("Hello")
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())