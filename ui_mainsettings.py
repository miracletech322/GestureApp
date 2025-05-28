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
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainSettings(object):
    def setupUi(self, MainSettings):
        if not MainSettings.objectName():
            MainSettings.setObjectName(u"MainSettings")
        MainSettings.resize(601, 378)
        self.gridLayout_7 = QGridLayout(MainSettings)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tabWidget = QTabWidget(MainSettings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chkSwipeUpYPlus = QCheckBox(self.tab)
        self.chkSwipeUpYPlus.setObjectName(u"chkSwipeUpYPlus")

        self.verticalLayout.addWidget(self.chkSwipeUpYPlus)

        self.chkSwipeDownYMinus = QCheckBox(self.tab)
        self.chkSwipeDownYMinus.setObjectName(u"chkSwipeDownYMinus")

        self.verticalLayout.addWidget(self.chkSwipeDownYMinus)

        self.chkSwipeRightXPlus = QCheckBox(self.tab)
        self.chkSwipeRightXPlus.setObjectName(u"chkSwipeRightXPlus")

        self.verticalLayout.addWidget(self.chkSwipeRightXPlus)

        self.chkSwipeLeftXMinus = QCheckBox(self.tab)
        self.chkSwipeLeftXMinus.setObjectName(u"chkSwipeLeftXMinus")

        self.verticalLayout.addWidget(self.chkSwipeLeftXMinus)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.kseSwipeUpYPlus = QKeySequenceEdit(self.tab)
        self.kseSwipeUpYPlus.setObjectName(u"kseSwipeUpYPlus")
        self.kseSwipeUpYPlus.setClearButtonEnabled(True)
        self.kseSwipeUpYPlus.setMaximumSequenceLength(1)

        self.verticalLayout_2.addWidget(self.kseSwipeUpYPlus)

        self.kseSwipeDownYMinus = QKeySequenceEdit(self.tab)
        self.kseSwipeDownYMinus.setObjectName(u"kseSwipeDownYMinus")
        self.kseSwipeDownYMinus.setClearButtonEnabled(True)
        self.kseSwipeDownYMinus.setMaximumSequenceLength(1)

        self.verticalLayout_2.addWidget(self.kseSwipeDownYMinus)

        self.kseSwipeRightXPlus = QKeySequenceEdit(self.tab)
        self.kseSwipeRightXPlus.setObjectName(u"kseSwipeRightXPlus")
        self.kseSwipeRightXPlus.setClearButtonEnabled(True)
        self.kseSwipeRightXPlus.setMaximumSequenceLength(1)

        self.verticalLayout_2.addWidget(self.kseSwipeRightXPlus)

        self.kseSwipeLeftXMinus = QKeySequenceEdit(self.tab)
        self.kseSwipeLeftXMinus.setObjectName(u"kseSwipeLeftXMinus")
        self.kseSwipeLeftXMinus.setClearButtonEnabled(True)
        self.kseSwipeLeftXMinus.setMaximumSequenceLength(1)

        self.verticalLayout_2.addWidget(self.kseSwipeLeftXMinus)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.chkPinchIn = QCheckBox(self.tab_2)
        self.chkPinchIn.setObjectName(u"chkPinchIn")

        self.verticalLayout_4.addWidget(self.chkPinchIn)

        self.chkPinchOut = QCheckBox(self.tab_2)
        self.chkPinchOut.setObjectName(u"chkPinchOut")

        self.verticalLayout_4.addWidget(self.chkPinchOut)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ksePinchIn = QKeySequenceEdit(self.tab_2)
        self.ksePinchIn.setObjectName(u"ksePinchIn")
        self.ksePinchIn.setClearButtonEnabled(True)
        self.ksePinchIn.setMaximumSequenceLength(1)

        self.verticalLayout_5.addWidget(self.ksePinchIn)

        self.ksePinchOut = QKeySequenceEdit(self.tab_2)
        self.ksePinchOut.setObjectName(u"ksePinchOut")
        self.ksePinchOut.setClearButtonEnabled(True)
        self.ksePinchOut.setMaximumSequenceLength(1)

        self.verticalLayout_5.addWidget(self.ksePinchOut)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.chkMHSwipeUp = QCheckBox(self.tab_3)
        self.chkMHSwipeUp.setObjectName(u"chkMHSwipeUp")

        self.verticalLayout_7.addWidget(self.chkMHSwipeUp)

        self.chkMHSwipeDown = QCheckBox(self.tab_3)
        self.chkMHSwipeDown.setObjectName(u"chkMHSwipeDown")

        self.verticalLayout_7.addWidget(self.chkMHSwipeDown)

        self.chkMHSwipeLeft = QCheckBox(self.tab_3)
        self.chkMHSwipeLeft.setObjectName(u"chkMHSwipeLeft")

        self.verticalLayout_7.addWidget(self.chkMHSwipeLeft)

        self.chkMHSwipeRight = QCheckBox(self.tab_3)
        self.chkMHSwipeRight.setObjectName(u"chkMHSwipeRight")

        self.verticalLayout_7.addWidget(self.chkMHSwipeRight)

        self.chkMHTap = QCheckBox(self.tab_3)
        self.chkMHTap.setObjectName(u"chkMHTap")

        self.verticalLayout_7.addWidget(self.chkMHTap)

        self.chkMHDoubleTap = QCheckBox(self.tab_3)
        self.chkMHDoubleTap.setObjectName(u"chkMHDoubleTap")

        self.verticalLayout_7.addWidget(self.chkMHDoubleTap)

        self.chkMHTripleTap = QCheckBox(self.tab_3)
        self.chkMHTripleTap.setObjectName(u"chkMHTripleTap")

        self.verticalLayout_7.addWidget(self.chkMHTripleTap)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.kseMHSwipeUp = QKeySequenceEdit(self.tab_3)
        self.kseMHSwipeUp.setObjectName(u"kseMHSwipeUp")
        self.kseMHSwipeUp.setClearButtonEnabled(True)
        self.kseMHSwipeUp.setMaximumSequenceLength(1)

        self.verticalLayout_8.addWidget(self.kseMHSwipeUp)

        self.kseMHSwipeDown = QKeySequenceEdit(self.tab_3)
        self.kseMHSwipeDown.setObjectName(u"kseMHSwipeDown")
        self.kseMHSwipeDown.setClearButtonEnabled(True)
        self.kseMHSwipeDown.setMaximumSequenceLength(1)

        self.verticalLayout_8.addWidget(self.kseMHSwipeDown)

        self.kseMHSwipeLeft = QKeySequenceEdit(self.tab_3)
        self.kseMHSwipeLeft.setObjectName(u"kseMHSwipeLeft")
        self.kseMHSwipeLeft.setClearButtonEnabled(True)
        self.kseMHSwipeLeft.setMaximumSequenceLength(1)

        self.verticalLayout_8.addWidget(self.kseMHSwipeLeft)

        self.kseMHSwipeRight = QKeySequenceEdit(self.tab_3)
        self.kseMHSwipeRight.setObjectName(u"kseMHSwipeRight")
        self.kseMHSwipeRight.setClearButtonEnabled(True)
        self.kseMHSwipeRight.setMaximumSequenceLength(1)

        self.verticalLayout_8.addWidget(self.kseMHSwipeRight)

        self.kseMHTap = QKeySequenceEdit(self.tab_3)
        self.kseMHTap.setObjectName(u"kseMHTap")
        self.kseMHTap.setClearButtonEnabled(True)
        self.kseMHTap.setMaximumSequenceLength(1)

        self.verticalLayout_8.addWidget(self.kseMHTap)

        self.kseMHDoubleTap = QKeySequenceEdit(self.tab_3)
        self.kseMHDoubleTap.setObjectName(u"kseMHDoubleTap")
        self.kseMHDoubleTap.setClearButtonEnabled(True)
        self.kseMHDoubleTap.setMaximumSequenceLength(1)

        self.verticalLayout_8.addWidget(self.kseMHDoubleTap)

        self.kseMHTripleTap = QKeySequenceEdit(self.tab_3)
        self.kseMHTripleTap.setObjectName(u"kseMHTripleTap")
        self.kseMHTripleTap.setClearButtonEnabled(True)
        self.kseMHTripleTap.setMaximumSequenceLength(1)

        self.verticalLayout_8.addWidget(self.kseMHTripleTap)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.chkModifierSwipeLeft = QCheckBox(self.tab_4)
        self.chkModifierSwipeLeft.setObjectName(u"chkModifierSwipeLeft")

        self.verticalLayout_10.addWidget(self.chkModifierSwipeLeft)

        self.chkModifierSwipeRight = QCheckBox(self.tab_4)
        self.chkModifierSwipeRight.setObjectName(u"chkModifierSwipeRight")

        self.verticalLayout_10.addWidget(self.chkModifierSwipeRight)

        self.chkModifierSingleTap = QCheckBox(self.tab_4)
        self.chkModifierSingleTap.setObjectName(u"chkModifierSingleTap")

        self.verticalLayout_10.addWidget(self.chkModifierSingleTap)

        self.chkModifierDoubleTap = QCheckBox(self.tab_4)
        self.chkModifierDoubleTap.setObjectName(u"chkModifierDoubleTap")

        self.verticalLayout_10.addWidget(self.chkModifierDoubleTap)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.kseModifierSwipeLeft = QKeySequenceEdit(self.tab_4)
        self.kseModifierSwipeLeft.setObjectName(u"kseModifierSwipeLeft")
        self.kseModifierSwipeLeft.setClearButtonEnabled(True)
        self.kseModifierSwipeLeft.setMaximumSequenceLength(1)

        self.verticalLayout_11.addWidget(self.kseModifierSwipeLeft)

        self.kseModifierSwipeRight = QKeySequenceEdit(self.tab_4)
        self.kseModifierSwipeRight.setObjectName(u"kseModifierSwipeRight")
        self.kseModifierSwipeRight.setClearButtonEnabled(True)
        self.kseModifierSwipeRight.setMaximumSequenceLength(1)

        self.verticalLayout_11.addWidget(self.kseModifierSwipeRight)

        self.kseModifierSingleTap = QKeySequenceEdit(self.tab_4)
        self.kseModifierSingleTap.setObjectName(u"kseModifierSingleTap")
        self.kseModifierSingleTap.setClearButtonEnabled(True)
        self.kseModifierSingleTap.setMaximumSequenceLength(1)

        self.verticalLayout_11.addWidget(self.kseModifierSingleTap)

        self.kseModifierDoubleTap = QKeySequenceEdit(self.tab_4)
        self.kseModifierDoubleTap.setObjectName(u"kseModifierDoubleTap")
        self.kseModifierDoubleTap.setClearButtonEnabled(True)
        self.kseModifierDoubleTap.setMaximumSequenceLength(1)

        self.verticalLayout_11.addWidget(self.kseModifierDoubleTap)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)


        self.gridLayout_4.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.chkGestureSwipeUp = QCheckBox(self.tab_5)
        self.chkGestureSwipeUp.setObjectName(u"chkGestureSwipeUp")

        self.verticalLayout_13.addWidget(self.chkGestureSwipeUp)

        self.chkGestureSwipeDown = QCheckBox(self.tab_5)
        self.chkGestureSwipeDown.setObjectName(u"chkGestureSwipeDown")

        self.verticalLayout_13.addWidget(self.chkGestureSwipeDown)

        self.chkGestureSwipeLeft = QCheckBox(self.tab_5)
        self.chkGestureSwipeLeft.setObjectName(u"chkGestureSwipeLeft")

        self.verticalLayout_13.addWidget(self.chkGestureSwipeLeft)

        self.chkGestureSwipeRight = QCheckBox(self.tab_5)
        self.chkGestureSwipeRight.setObjectName(u"chkGestureSwipeRight")

        self.verticalLayout_13.addWidget(self.chkGestureSwipeRight)

        self.chkGestureSwipeIn = QCheckBox(self.tab_5)
        self.chkGestureSwipeIn.setObjectName(u"chkGestureSwipeIn")

        self.verticalLayout_13.addWidget(self.chkGestureSwipeIn)

        self.chkGestureSwipeOut = QCheckBox(self.tab_5)
        self.chkGestureSwipeOut.setObjectName(u"chkGestureSwipeOut")

        self.verticalLayout_13.addWidget(self.chkGestureSwipeOut)

        self.chkGestureSingleTap = QCheckBox(self.tab_5)
        self.chkGestureSingleTap.setObjectName(u"chkGestureSingleTap")

        self.verticalLayout_13.addWidget(self.chkGestureSingleTap)

        self.chkGestureDoubleTap = QCheckBox(self.tab_5)
        self.chkGestureDoubleTap.setObjectName(u"chkGestureDoubleTap")

        self.verticalLayout_13.addWidget(self.chkGestureDoubleTap)

        self.chkGestureTripleTap = QCheckBox(self.tab_5)
        self.chkGestureTripleTap.setObjectName(u"chkGestureTripleTap")

        self.verticalLayout_13.addWidget(self.chkGestureTripleTap)


        self.horizontalLayout_6.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.kseGestureSwipeUp = QKeySequenceEdit(self.tab_5)
        self.kseGestureSwipeUp.setObjectName(u"kseGestureSwipeUp")
        self.kseGestureSwipeUp.setClearButtonEnabled(True)
        self.kseGestureSwipeUp.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureSwipeUp)

        self.kseGestureSwipeDown = QKeySequenceEdit(self.tab_5)
        self.kseGestureSwipeDown.setObjectName(u"kseGestureSwipeDown")
        self.kseGestureSwipeDown.setClearButtonEnabled(True)
        self.kseGestureSwipeDown.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureSwipeDown)

        self.kseGestureSwipeLeft = QKeySequenceEdit(self.tab_5)
        self.kseGestureSwipeLeft.setObjectName(u"kseGestureSwipeLeft")
        self.kseGestureSwipeLeft.setClearButtonEnabled(True)
        self.kseGestureSwipeLeft.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureSwipeLeft)

        self.kseGestureSwipeRight = QKeySequenceEdit(self.tab_5)
        self.kseGestureSwipeRight.setObjectName(u"kseGestureSwipeRight")
        self.kseGestureSwipeRight.setClearButtonEnabled(True)
        self.kseGestureSwipeRight.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureSwipeRight)

        self.kseGestureSwipeIn = QKeySequenceEdit(self.tab_5)
        self.kseGestureSwipeIn.setObjectName(u"kseGestureSwipeIn")
        self.kseGestureSwipeIn.setClearButtonEnabled(True)
        self.kseGestureSwipeIn.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureSwipeIn)

        self.kseGestureSwipeOut = QKeySequenceEdit(self.tab_5)
        self.kseGestureSwipeOut.setObjectName(u"kseGestureSwipeOut")
        self.kseGestureSwipeOut.setClearButtonEnabled(True)
        self.kseGestureSwipeOut.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureSwipeOut)

        self.kseGestureSingleTap = QKeySequenceEdit(self.tab_5)
        self.kseGestureSingleTap.setObjectName(u"kseGestureSingleTap")
        self.kseGestureSingleTap.setClearButtonEnabled(True)
        self.kseGestureSingleTap.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureSingleTap)

        self.kseGestureDoubleTap = QKeySequenceEdit(self.tab_5)
        self.kseGestureDoubleTap.setObjectName(u"kseGestureDoubleTap")
        self.kseGestureDoubleTap.setClearButtonEnabled(True)
        self.kseGestureDoubleTap.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureDoubleTap)

        self.kseGestureTripleTap = QKeySequenceEdit(self.tab_5)
        self.kseGestureTripleTap.setObjectName(u"kseGestureTripleTap")
        self.kseGestureTripleTap.setClearButtonEnabled(True)
        self.kseGestureTripleTap.setMaximumSequenceLength(1)

        self.verticalLayout_14.addWidget(self.kseGestureTripleTap)


        self.horizontalLayout_6.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)


        self.gridLayout_5.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_6 = QGridLayout(self.tab_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.chkMHGestureSwipeUp = QCheckBox(self.tab_6)
        self.chkMHGestureSwipeUp.setObjectName(u"chkMHGestureSwipeUp")

        self.verticalLayout_16.addWidget(self.chkMHGestureSwipeUp)

        self.chkMHGestureSwipeDown = QCheckBox(self.tab_6)
        self.chkMHGestureSwipeDown.setObjectName(u"chkMHGestureSwipeDown")

        self.verticalLayout_16.addWidget(self.chkMHGestureSwipeDown)

        self.chkMHGestureSwipeLeft = QCheckBox(self.tab_6)
        self.chkMHGestureSwipeLeft.setObjectName(u"chkMHGestureSwipeLeft")

        self.verticalLayout_16.addWidget(self.chkMHGestureSwipeLeft)

        self.chkMHGestureSwipeRight = QCheckBox(self.tab_6)
        self.chkMHGestureSwipeRight.setObjectName(u"chkMHGestureSwipeRight")

        self.verticalLayout_16.addWidget(self.chkMHGestureSwipeRight)

        self.chkMHGestureSwipeIn = QCheckBox(self.tab_6)
        self.chkMHGestureSwipeIn.setObjectName(u"chkMHGestureSwipeIn")

        self.verticalLayout_16.addWidget(self.chkMHGestureSwipeIn)

        self.chkMHGestureSwipeOut = QCheckBox(self.tab_6)
        self.chkMHGestureSwipeOut.setObjectName(u"chkMHGestureSwipeOut")

        self.verticalLayout_16.addWidget(self.chkMHGestureSwipeOut)


        self.horizontalLayout_7.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.kseMHGestureSwipeUp = QKeySequenceEdit(self.tab_6)
        self.kseMHGestureSwipeUp.setObjectName(u"kseMHGestureSwipeUp")
        self.kseMHGestureSwipeUp.setClearButtonEnabled(True)
        self.kseMHGestureSwipeUp.setMaximumSequenceLength(1)

        self.verticalLayout_17.addWidget(self.kseMHGestureSwipeUp)

        self.kseMHGestureSwipeDown = QKeySequenceEdit(self.tab_6)
        self.kseMHGestureSwipeDown.setObjectName(u"kseMHGestureSwipeDown")
        self.kseMHGestureSwipeDown.setClearButtonEnabled(True)
        self.kseMHGestureSwipeDown.setMaximumSequenceLength(1)

        self.verticalLayout_17.addWidget(self.kseMHGestureSwipeDown)

        self.kseMHGestureSwipeLeft = QKeySequenceEdit(self.tab_6)
        self.kseMHGestureSwipeLeft.setObjectName(u"kseMHGestureSwipeLeft")
        self.kseMHGestureSwipeLeft.setClearButtonEnabled(True)
        self.kseMHGestureSwipeLeft.setMaximumSequenceLength(1)

        self.verticalLayout_17.addWidget(self.kseMHGestureSwipeLeft)

        self.kseMHGestureSwipeRight = QKeySequenceEdit(self.tab_6)
        self.kseMHGestureSwipeRight.setObjectName(u"kseMHGestureSwipeRight")
        self.kseMHGestureSwipeRight.setClearButtonEnabled(True)
        self.kseMHGestureSwipeRight.setMaximumSequenceLength(1)

        self.verticalLayout_17.addWidget(self.kseMHGestureSwipeRight)

        self.kseMHGestureSwipeIn = QKeySequenceEdit(self.tab_6)
        self.kseMHGestureSwipeIn.setObjectName(u"kseMHGestureSwipeIn")
        self.kseMHGestureSwipeIn.setClearButtonEnabled(True)
        self.kseMHGestureSwipeIn.setMaximumSequenceLength(1)

        self.verticalLayout_17.addWidget(self.kseMHGestureSwipeIn)

        self.kseMHGestureSwipeOut = QKeySequenceEdit(self.tab_6)
        self.kseMHGestureSwipeOut.setObjectName(u"kseMHGestureSwipeOut")
        self.kseMHGestureSwipeOut.setClearButtonEnabled(True)
        self.kseMHGestureSwipeOut.setMaximumSequenceLength(1)

        self.verticalLayout_17.addWidget(self.kseMHGestureSwipeOut)


        self.horizontalLayout_7.addLayout(self.verticalLayout_17)


        self.verticalLayout_18.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_6)


        self.gridLayout_6.addLayout(self.verticalLayout_18, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_19.addWidget(self.tabWidget)

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


        self.verticalLayout_19.addLayout(self.horizontalLayout_2)


        self.gridLayout_7.addLayout(self.verticalLayout_19, 0, 0, 1, 1)


        self.retranslateUi(MainSettings)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainSettings)
    # setupUi

    def retranslateUi(self, MainSettings):
        MainSettings.setWindowTitle(QCoreApplication.translate("MainSettings", u"Gesture App Settings", None))
        self.chkSwipeUpYPlus.setText(QCoreApplication.translate("MainSettings", u"Swipe Up (Y+) ", None))
        self.chkSwipeDownYMinus.setText(QCoreApplication.translate("MainSettings", u"Swipe Down (Y-) ", None))
        self.chkSwipeRightXPlus.setText(QCoreApplication.translate("MainSettings", u"Swipe Right (X+)", None))
        self.chkSwipeLeftXMinus.setText(QCoreApplication.translate("MainSettings", u"Swipe Left (X-)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainSettings", u"Solo Touch", None))
        self.chkPinchIn.setText(QCoreApplication.translate("MainSettings", u"Pinch In", None))
        self.chkPinchOut.setText(QCoreApplication.translate("MainSettings", u"Pinch Out", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainSettings", u"Dual Touch", None))
        self.chkMHSwipeUp.setText(QCoreApplication.translate("MainSettings", u"MH+Swipe Up", None))
        self.chkMHSwipeDown.setText(QCoreApplication.translate("MainSettings", u"MH+Swipe Down", None))
        self.chkMHSwipeLeft.setText(QCoreApplication.translate("MainSettings", u"MH+Swipe Left", None))
        self.chkMHSwipeRight.setText(QCoreApplication.translate("MainSettings", u"MH+Swipe Right", None))
        self.chkMHTap.setText(QCoreApplication.translate("MainSettings", u"MH+Tap", None))
        self.chkMHDoubleTap.setText(QCoreApplication.translate("MainSettings", u"MH+Double Tap", None))
        self.chkMHTripleTap.setText(QCoreApplication.translate("MainSettings", u"MH+Triple Tap", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainSettings", u"Modified Touch", None))
        self.chkModifierSwipeLeft.setText(QCoreApplication.translate("MainSettings", u"Modifier Swipe Left", None))
        self.chkModifierSwipeRight.setText(QCoreApplication.translate("MainSettings", u"Modifier Swipe Right", None))
        self.chkModifierSingleTap.setText(QCoreApplication.translate("MainSettings", u"Modifier Single Tap", None))
        self.chkModifierDoubleTap.setText(QCoreApplication.translate("MainSettings", u"Modifier Double Tap", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainSettings", u"Modifier Only", None))
        self.chkGestureSwipeUp.setText(QCoreApplication.translate("MainSettings", u"Gesture Swipe Up", None))
        self.chkGestureSwipeDown.setText(QCoreApplication.translate("MainSettings", u"Gesture Swipe Down", None))
        self.chkGestureSwipeLeft.setText(QCoreApplication.translate("MainSettings", u"Gesture Swipe Left", None))
        self.chkGestureSwipeRight.setText(QCoreApplication.translate("MainSettings", u"Gesture Swipe Right", None))
        self.chkGestureSwipeIn.setText(QCoreApplication.translate("MainSettings", u"Gesture Swipe In", None))
        self.chkGestureSwipeOut.setText(QCoreApplication.translate("MainSettings", u"Gesture Swipe Out", None))
        self.chkGestureSingleTap.setText(QCoreApplication.translate("MainSettings", u"Gesture Single Tap", None))
        self.chkGestureDoubleTap.setText(QCoreApplication.translate("MainSettings", u"Gesture Double Tap", None))
        self.chkGestureTripleTap.setText(QCoreApplication.translate("MainSettings", u"Gesture Triple Tap", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainSettings", u"Air Mode", None))
        self.chkMHGestureSwipeUp.setText(QCoreApplication.translate("MainSettings", u"MH + Gesture Swipe Up", None))
        self.chkMHGestureSwipeDown.setText(QCoreApplication.translate("MainSettings", u"MH + Gesture Swipe Down", None))
        self.chkMHGestureSwipeLeft.setText(QCoreApplication.translate("MainSettings", u"MH + Gesture Swipe Left", None))
        self.chkMHGestureSwipeRight.setText(QCoreApplication.translate("MainSettings", u"MH + Gesture Swipe Right", None))
        self.chkMHGestureSwipeIn.setText(QCoreApplication.translate("MainSettings", u"MH + Gesture Swipe In", None))
        self.chkMHGestureSwipeOut.setText(QCoreApplication.translate("MainSettings", u"MH + Gesture Swipe Out", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainSettings", u"Modified Air Mode", None))
        self.btnSave.setText(QCoreApplication.translate("MainSettings", u"Save", None))
        self.btnClose.setText(QCoreApplication.translate("MainSettings", u"Close", None))
    # retranslateUi

