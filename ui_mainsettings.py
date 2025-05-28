# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainsettings.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QKeySequenceEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainSettings(object):
    def setupUi(self, MainSettings):
        if not MainSettings.objectName():
            MainSettings.setObjectName(u"MainSettings")
        MainSettings.resize(375, 170)
        self.gridLayout = QGridLayout(MainSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chkSwipeUpYPlus = QCheckBox(MainSettings)
        self.chkSwipeUpYPlus.setObjectName(u"chkSwipeUpYPlus")

        self.verticalLayout.addWidget(self.chkSwipeUpYPlus)

        self.chkSwipeDownYMinus = QCheckBox(MainSettings)
        self.chkSwipeDownYMinus.setObjectName(u"chkSwipeDownYMinus")

        self.verticalLayout.addWidget(self.chkSwipeDownYMinus)

        self.chkSwipeRightXPlus = QCheckBox(MainSettings)
        self.chkSwipeRightXPlus.setObjectName(u"chkSwipeRightXPlus")

        self.verticalLayout.addWidget(self.chkSwipeRightXPlus)

        self.chkSwipeLeftXMinus = QCheckBox(MainSettings)
        self.chkSwipeLeftXMinus.setObjectName(u"chkSwipeLeftXMinus")

        self.verticalLayout.addWidget(self.chkSwipeLeftXMinus)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.kseSwipeUpYPlus = QKeySequenceEdit(MainSettings)
        self.kseSwipeUpYPlus.setObjectName(u"kseSwipeUpYPlus")
        self.kseSwipeUpYPlus.setClearButtonEnabled(True)
        self.kseSwipeUpYPlus.setMaximumSequenceLength(1)

        self.verticalLayout_2.addWidget(self.kseSwipeUpYPlus)

        self.kseSwipeDownYMinus = QKeySequenceEdit(MainSettings)
        self.kseSwipeDownYMinus.setObjectName(u"kseSwipeDownYMinus")
        self.kseSwipeDownYMinus.setClearButtonEnabled(True)
        self.kseSwipeDownYMinus.setMaximumSequenceLength(1)

        self.verticalLayout_2.addWidget(self.kseSwipeDownYMinus)

        self.kseSwipeRightXPlus = QKeySequenceEdit(MainSettings)
        self.kseSwipeRightXPlus.setObjectName(u"kseSwipeRightXPlus")
        self.kseSwipeRightXPlus.setClearButtonEnabled(True)
        self.kseSwipeRightXPlus.setMaximumSequenceLength(1)

        self.verticalLayout_2.addWidget(self.kseSwipeRightXPlus)

        self.kseSwipeLeftXMinus = QKeySequenceEdit(MainSettings)
        self.kseSwipeLeftXMinus.setObjectName(u"kseSwipeLeftXMinus")
        self.kseSwipeLeftXMinus.setClearButtonEnabled(True)
        self.kseSwipeLeftXMinus.setMaximumSequenceLength(1)

        self.verticalLayout_2.addWidget(self.kseSwipeLeftXMinus)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(MainSettings)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_2.addWidget(self.btnSave)

        self.btnClose = QPushButton(MainSettings)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(MainSettings)

        QMetaObject.connectSlotsByName(MainSettings)
    # setupUi

    def retranslateUi(self, MainSettings):
        MainSettings.setWindowTitle(QCoreApplication.translate("MainSettings", u"Dialog", None))
        self.chkSwipeUpYPlus.setText(QCoreApplication.translate("MainSettings", u"Swipe Up (Y+) ", None))
        self.chkSwipeDownYMinus.setText(QCoreApplication.translate("MainSettings", u"Swipe Down (Y-) ", None))
        self.chkSwipeRightXPlus.setText(QCoreApplication.translate("MainSettings", u"Swipe Right (X+)", None))
        self.chkSwipeLeftXMinus.setText(QCoreApplication.translate("MainSettings", u"Swipe Left (X-)", None))
        self.btnSave.setText(QCoreApplication.translate("MainSettings", u"Save", None))
        self.btnClose.setText(QCoreApplication.translate("MainSettings", u"Close", None))
    # retranslateUi

