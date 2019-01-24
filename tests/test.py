import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    #resize()方法能改变控件的大小，这里的意思是窗口宽250px，高150px。
    w.resize(250,150)
    #move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(300, 300)的位置。注：屏幕坐标系的原点是屏幕的左上角。
    w.move(300, 300)
    w.setWindowTitle("Test")
    w.show()

    sys.exit(app.exec_())