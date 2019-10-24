# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from camera_driver import camera_driver


class Ui_InStore(object):
    def setupUi(self, InStore):
        InStore.setObjectName("InStore")
        InStore.setWindowModality(QtCore.Qt.ApplicationModal)
        InStore.setEnabled(True)
        InStore.resize(900, 656)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InStore.sizePolicy().hasHeightForWidth())
        InStore.setSizePolicy(sizePolicy)
        InStore.setBaseSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        InStore.setFont(font)
        InStore.setFocusPolicy(QtCore.Qt.ClickFocus)
        InStore.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/icons/refund.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        InStore.setWindowIcon(icon)
        InStore.setWindowOpacity(0.9)
        InStore.setToolTipDuration(1)
        InStore.setStatusTip("")
        InStore.setWhatsThis("")
        InStore.setAutoFillBackground(True)
        InStore.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        InStore.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhTime)
        InStore.setTabShape(QtWidgets.QTabWidget.Rounded)
        InStore.setDockNestingEnabled(True)
        InStore.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        InStore.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(InStore)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.infoInput = QtWidgets.QWidget()
        self.infoInput.setObjectName("infoInput")
        self.formLayout = QtWidgets.QFormLayout(self.infoInput)
        self.formLayout.setObjectName("formLayout")
        self.openCamera = QtWidgets.QPushButton(self.infoInput)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pics/icons/webcam.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.openCamera.setIcon(icon1)
        self.openCamera.setObjectName("openCamera")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.openCamera)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pics/icons/invoice.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.tabWidget.addTab(self.infoInput, icon2, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        InStore.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InStore)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setToolTipDuration(1)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        InStore.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InStore)
        self.statusbar.setToolTipDuration(1)
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        InStore.setStatusBar(self.statusbar)

        self.retranslateUi(InStore)
        QtCore.QMetaObject.connectSlotsByName(InStore)

    def retranslateUi(self, InStore):
        _translate = QtCore.QCoreApplication.translate
        InStore.setWindowTitle(_translate("InStore", "入库管理系统"))
        InStore.setToolTip(_translate("InStore", "<html><head/><body><p>入库管理系统</p></body></html>"))
        self.openCamera.setToolTip(_translate("InStore", "点此处打开摄像头，进行信息录入"))
        self.openCamera.setText(_translate("InStore", "打开摄像头"))
        self.openCamera.clicked.connect(self.open_camera)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoInput), _translate("InStore", "信息录入"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("InStore", "Tab 2"))

    def open_camera(self):
        camera_driver().camera_open(os.path.abspath("temp"), "hands")

