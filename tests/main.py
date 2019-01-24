import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QTextEdit


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #self.statusBar().showMessage("准备好嘞")

        # menubar=self.menuBar()
        # fileMenu=menubar.addMenu('File')
        #
        # impMenu=QMenu('Import', self)
        # imAct=QAction('Import mail', self)
        # impMenu.addAction(imAct)
        #
        # newAct=QAction('New', self)
        #
        # fileMenu.addAction(newAct)
        # fileMenu.addMenu(impMenu)

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('.././pics/icons/quit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300,300,500,600)
        self.setWindowTitle("状态栏")
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())