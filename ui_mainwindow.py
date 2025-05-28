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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 381)
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

        self.btnSettings = QPushButton(self.centralwidget)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(120, 30))

        self.horizontalLayout.addWidget(self.btnSettings)

        self.btnFindDevice = QPushButton(self.centralwidget)
        self.btnFindDevice.setObjectName(u"btnFindDevice")
        self.btnFindDevice.setMinimumSize(QSize(120, 30))

        self.horizontalLayout.addWidget(self.btnFindDevice)

        self.btnConnectDevice = QPushButton(self.centralwidget)
        self.btnConnectDevice.setObjectName(u"btnConnectDevice")
        self.btnConnectDevice.setMinimumSize(QSize(120, 30))

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
        self.tblDevice.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.tblDevice)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btnSettings, self.btnFindDevice)
        QWidget.setTabOrder(self.btnFindDevice, self.btnConnectDevice)
        QWidget.setTabOrder(self.btnConnectDevice, self.tblDevice)
        QWidget.setTabOrder(self.tblDevice, self.plainTextEdit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GestureApp Settings", None))
        self.actionSaveSettings.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.actionLoadSettings.setText(QCoreApplication.translate("MainWindow", u"Load Settings", None))
        self.actionExitApp.setText(QCoreApplication.translate("MainWindow", u"Exit App", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btnFindDevice.setText(QCoreApplication.translate("MainWindow", u"Find Devices", None))
        self.btnConnectDevice.setText(QCoreApplication.translate("MainWindow", u"Connect to Device", None))
        ___qtablewidgetitem = self.tblDevice.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Device Name", None));
        ___qtablewidgetitem1 = self.tblDevice.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Addess", None));
    # retranslateUi

