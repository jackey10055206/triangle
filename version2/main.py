import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import version_2 as ui
import math

class Main(QMainWindow, ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        self.btn_cal.clicked.connect(self.CalNum)
        self.btn_reset.clicked.connect(self.Reset)
    def CalNum(self):
        angle = float(self.input_angle.text())
        length = float(self.input_length.text())

        angle = angle/2
        result = math.sin(angle*math.pi/180) * length * 2
        self.textBrowser.setText(str(round(result,2)))
        print(result)

    def Reset(self):
        self.input_angle.setText("")
        self.input_length.setText("")
        self.textBrowser.setText("")
        
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())