# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionSaveSettings = QAction(MainWindow)
        self.actionSaveSettings.setObjectName(u"actionSaveSettings")
        self.actionLoadSettings = QAction(MainWindow)
        self.actionLoadSettings.setObjectName(u"actionLoadSettings")
        self.actionExitApp = QAction(MainWindow)
        self.actionExitApp.setObjectName(u"actionExitApp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnFindDevice = QPushButton(self.centralwidget)
        self.btnFindDevice.setObjectName(u"btnFindDevice")

        self.horizontalLayout.addWidget(self.btnFindDevice)

        self.btnConnectDevice = QPushButton(self.centralwidget)
        self.btnConnectDevice.setObjectName(u"btnConnectDevice")

        self.horizontalLayout.addWidget(self.btnConnectDevice)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblDevice = QTableWidget(self.centralwidget)
        if (self.tblDevice.columnCount() < 2):
            self.tblDevice.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblDevice.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblDevice.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblDevice.setObjectName(u"tblDevice")

        self.verticalLayout.addWidget(self.tblDevice)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menu_File.addAction(self.actionSaveSettings)
        self.menu_File.addAction(self.actionLoadSettings)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExitApp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GestureApp Settings", None))
        self.actionSaveSettings.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.actionLoadSettings.setText(QCoreApplication.translate("MainWindow", u"Load Settings", None))
        self.actionExitApp.setText(QCoreApplication.translate("MainWindow", u"Exit App", None))
        self.btnFindDevice.setText(QCoreApplication.translate("MainWindow", u"Find Devices", None))
        self.btnConnectDevice.setText(QCoreApplication.translate("MainWindow", u"Connect to Device", None))
        ___qtablewidgetitem = self.tblDevice.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Device Name", None));
        ___qtablewidgetitem1 = self.tblDevice.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Addess", None));
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

