import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import version_3 as ui
import math

class Main(QMainWindow, ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.CalNum)
        self.pushButton_2.clicked.connect(self.Reset)
        
    def CalNum(self,angle):
        angle = float((self.comboBox_angle.currentText())[:-1])
        length = float(self.textEdit_2.text())

        angle = angle/2
        result = math.sin(angle*math.pi/180) * length * 2
        self.textBrowser.setText(str(round(result,2)))

    def Reset(self):
        self.textEdit_2.setText("")
        self.textBrowser.setText("")

        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())