import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

from main import Ui_MainWindow


class inStore:
    def __init__(self):
        self.widget=QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.widget)
        #self.show()
        self.widget.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex=inStore()
    sys.exit(app.exec_())