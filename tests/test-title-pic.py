import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QPushButton, QMessageBox, QMessageBox, QMessageBox, \
    QDesktopWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('这是个<b>组件</b>')
        btn = QPushButton('退出', self)
        btn.setToolTip('这是个<b>PushButton</b>')
        #点击退出
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        #setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小。参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是resize()和move()的合体
        #self.setGeometry(300,300,300,220)
        self.resize(500,600)
        self.center()
        self.setWindowTitle("Test")
        self.setWindowIcon(QIcon('.././pics/icons/tracking.png'))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', '你确定要退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())