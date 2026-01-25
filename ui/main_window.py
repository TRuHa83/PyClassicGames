# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 560)
        MainWindow.setMinimumSize(QSize(400, 560))
        MainWindow.setMaximumSize(QSize(400, 560))
        icon = QIcon()
        icon.addFile(u":/logo/logo_128.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionMenu = QAction(MainWindow)
        self.actionMenu.setObjectName(u"actionMenu")
        self.actionMine = QAction(MainWindow)
        self.actionMine.setObjectName(u"actionMine")
        self.actionHorse = QAction(MainWindow)
        self.actionHorse.setObjectName(u"actionHorse")
        self.actionWordle = QAction(MainWindow)
        self.actionWordle.setObjectName(u"actionWordle")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionReset = QAction(MainWindow)
        self.actionReset.setObjectName(u"actionReset")
        self.actionFacil = QAction(MainWindow)
        self.actionFacil.setObjectName(u"actionFacil")
        self.actionMedio = QAction(MainWindow)
        self.actionMedio.setObjectName(u"actionMedio")
        self.actionDificil = QAction(MainWindow)
        self.actionDificil.setObjectName(u"actionDificil")
        self.actionPuntuaci_n = QAction(MainWindow)
        self.actionPuntuaci_n.setObjectName(u"actionPuntuaci_n")
        self.actionScore = QAction(MainWindow)
        self.actionScore.setObjectName(u"actionScore")
        self.actionCheckRun = QAction(MainWindow)
        self.actionCheckRun.setObjectName(u"actionCheckRun")
        self.actionCheckRun.setCheckable(True)
        self.actionCheckRun.setChecked(True)
        self.actionCheckNow = QAction(MainWindow)
        self.actionCheckNow.setObjectName(u"actionCheckNow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.gridLayout_3 = QGridLayout(self.menu)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(10)
        self.stackedWidget.addWidget(self.menu)
        self.mine = QWidget()
        self.mine.setObjectName(u"mine")
        self.gridLayout_4 = QGridLayout(self.mine)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.mine)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(304, 440))
        self.groupBox.setMaximumSize(QSize(304, 440))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lcd_lags = QLCDNumber(self.groupBox)
        self.lcd_lags.setObjectName(u"lcd_lags")
        self.lcd_lags.setMinimumSize(QSize(80, 40))
        self.lcd_lags.setMaximumSize(QSize(80, 40))
        font = QFont()
        font.setBold(True)
        self.lcd_lags.setFont(font)
        self.lcd_lags.setDigitCount(4)
        self.lcd_lags.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.lcd_lags)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.face_btn = QPushButton(self.groupBox)
        self.face_btn.setObjectName(u"face_btn")
        self.face_btn.setMinimumSize(QSize(40, 40))
        self.face_btn.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.face_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.face_btn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lcd_clock = QLCDNumber(self.groupBox)
        self.lcd_clock.setObjectName(u"lcd_clock")
        self.lcd_clock.setMinimumSize(QSize(80, 40))
        self.lcd_clock.setMaximumSize(QSize(80, 40))
        self.lcd_clock.setFont(font)
        self.lcd_clock.setFrameShape(QFrame.Shape.Box)
        self.lcd_clock.setFrameShadow(QFrame.Shadow.Sunken)
        self.lcd_clock.setDigitCount(4)
        self.lcd_clock.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.lcd_clock)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.mineLayout = QFrame(self.groupBox)
        self.mineLayout.setObjectName(u"mineLayout")
        self.mineLayout.setFrameShape(QFrame.Shape.Box)
        self.mineLayout.setFrameShadow(QFrame.Shadow.Sunken)
        self.minesLayout = QGridLayout(self.mineLayout)
        self.minesLayout.setSpacing(1)
        self.minesLayout.setObjectName(u"minesLayout")
        self.btn_mine_6_0 = QPushButton(self.mineLayout)
        self.btn_mine_6_0.setObjectName(u"btn_mine_6_0")
        self.btn_mine_6_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_0, 6, 0, 1, 1)

        self.btn_mine_13_8 = QPushButton(self.mineLayout)
        self.btn_mine_13_8.setObjectName(u"btn_mine_13_8")
        self.btn_mine_13_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_8, 13, 8, 1, 1)

        self.btn_mine_12_7 = QPushButton(self.mineLayout)
        self.btn_mine_12_7.setObjectName(u"btn_mine_12_7")
        self.btn_mine_12_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_7, 12, 7, 1, 1)

        self.btn_mine_13_4 = QPushButton(self.mineLayout)
        self.btn_mine_13_4.setObjectName(u"btn_mine_13_4")
        self.btn_mine_13_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_4, 13, 4, 1, 1)

        self.btn_mine_2_2 = QPushButton(self.mineLayout)
        self.btn_mine_2_2.setObjectName(u"btn_mine_2_2")
        self.btn_mine_2_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_2, 2, 2, 1, 1)

        self.btn_mine_12_2 = QPushButton(self.mineLayout)
        self.btn_mine_12_2.setObjectName(u"btn_mine_12_2")
        self.btn_mine_12_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_2, 12, 2, 1, 1)

        self.btn_mine_13_3 = QPushButton(self.mineLayout)
        self.btn_mine_13_3.setObjectName(u"btn_mine_13_3")
        self.btn_mine_13_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_3, 13, 3, 1, 1)

        self.btn_mine_3_1 = QPushButton(self.mineLayout)
        self.btn_mine_3_1.setObjectName(u"btn_mine_3_1")
        self.btn_mine_3_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_1, 3, 1, 1, 1)

        self.btn_mine_10_0 = QPushButton(self.mineLayout)
        self.btn_mine_10_0.setObjectName(u"btn_mine_10_0")
        self.btn_mine_10_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_0, 10, 0, 1, 1)

        self.btn_mine_5_0 = QPushButton(self.mineLayout)
        self.btn_mine_5_0.setObjectName(u"btn_mine_5_0")
        self.btn_mine_5_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_0, 5, 0, 1, 1)

        self.btn_mine_7_2 = QPushButton(self.mineLayout)
        self.btn_mine_7_2.setObjectName(u"btn_mine_7_2")
        self.btn_mine_7_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_2, 7, 2, 1, 1)

        self.btn_mine_5_6 = QPushButton(self.mineLayout)
        self.btn_mine_5_6.setObjectName(u"btn_mine_5_6")
        self.btn_mine_5_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_6, 5, 6, 1, 1)

        self.btn_mine_15_8 = QPushButton(self.mineLayout)
        self.btn_mine_15_8.setObjectName(u"btn_mine_15_8")
        self.btn_mine_15_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_8, 15, 8, 1, 1)

        self.btn_mine_3_8 = QPushButton(self.mineLayout)
        self.btn_mine_3_8.setObjectName(u"btn_mine_3_8")
        self.btn_mine_3_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_8, 3, 8, 1, 1)

        self.btn_mine_15_1 = QPushButton(self.mineLayout)
        self.btn_mine_15_1.setObjectName(u"btn_mine_15_1")
        self.btn_mine_15_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_1, 15, 1, 1, 1)

        self.btn_mine_11_7 = QPushButton(self.mineLayout)
        self.btn_mine_11_7.setObjectName(u"btn_mine_11_7")
        self.btn_mine_11_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_7, 11, 7, 1, 1)

        self.btn_mine_1_2 = QPushButton(self.mineLayout)
        self.btn_mine_1_2.setObjectName(u"btn_mine_1_2")
        self.btn_mine_1_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_2, 1, 2, 1, 1)

        self.btn_mine_2_8 = QPushButton(self.mineLayout)
        self.btn_mine_2_8.setObjectName(u"btn_mine_2_8")
        self.btn_mine_2_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_8, 2, 8, 1, 1)

        self.btn_mine_12_5 = QPushButton(self.mineLayout)
        self.btn_mine_12_5.setObjectName(u"btn_mine_12_5")
        self.btn_mine_12_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_5, 12, 5, 1, 1)

        self.btn_mine_14_7 = QPushButton(self.mineLayout)
        self.btn_mine_14_7.setObjectName(u"btn_mine_14_7")
        self.btn_mine_14_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_7, 14, 7, 1, 1)

        self.btn_mine_6_5 = QPushButton(self.mineLayout)
        self.btn_mine_6_5.setObjectName(u"btn_mine_6_5")
        self.btn_mine_6_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_5, 6, 5, 1, 1)

        self.btn_mine_11_5 = QPushButton(self.mineLayout)
        self.btn_mine_11_5.setObjectName(u"btn_mine_11_5")
        self.btn_mine_11_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_5, 11, 5, 1, 1)

        self.btn_mine_10_2 = QPushButton(self.mineLayout)
        self.btn_mine_10_2.setObjectName(u"btn_mine_10_2")
        self.btn_mine_10_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_2, 10, 2, 1, 1)

        self.btn_mine_2_7 = QPushButton(self.mineLayout)
        self.btn_mine_2_7.setObjectName(u"btn_mine_2_7")
        self.btn_mine_2_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_7, 2, 7, 1, 1)

        self.btn_mine_5_1 = QPushButton(self.mineLayout)
        self.btn_mine_5_1.setObjectName(u"btn_mine_5_1")
        self.btn_mine_5_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_1, 5, 1, 1, 1)

        self.btn_mine_5_2 = QPushButton(self.mineLayout)
        self.btn_mine_5_2.setObjectName(u"btn_mine_5_2")
        self.btn_mine_5_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_2, 5, 2, 1, 1)

        self.btn_mine_6_7 = QPushButton(self.mineLayout)
        self.btn_mine_6_7.setObjectName(u"btn_mine_6_7")
        self.btn_mine_6_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_7, 6, 7, 1, 1)

        self.btn_mine_1_8 = QPushButton(self.mineLayout)
        self.btn_mine_1_8.setObjectName(u"btn_mine_1_8")
        self.btn_mine_1_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_8, 1, 8, 1, 1)

        self.btn_mine_3_4 = QPushButton(self.mineLayout)
        self.btn_mine_3_4.setObjectName(u"btn_mine_3_4")
        self.btn_mine_3_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_4, 3, 4, 1, 1)

        self.btn_mine_3_0 = QPushButton(self.mineLayout)
        self.btn_mine_3_0.setObjectName(u"btn_mine_3_0")
        self.btn_mine_3_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_0, 3, 0, 1, 1)

        self.btn_mine_15_5 = QPushButton(self.mineLayout)
        self.btn_mine_15_5.setObjectName(u"btn_mine_15_5")
        self.btn_mine_15_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_5, 15, 5, 1, 1)

        self.btn_mine_15_3 = QPushButton(self.mineLayout)
        self.btn_mine_15_3.setObjectName(u"btn_mine_15_3")
        self.btn_mine_15_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_3, 15, 3, 1, 1)

        self.btn_mine_14_6 = QPushButton(self.mineLayout)
        self.btn_mine_14_6.setObjectName(u"btn_mine_14_6")
        self.btn_mine_14_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_6, 14, 6, 1, 1)

        self.btn_mine_9_4 = QPushButton(self.mineLayout)
        self.btn_mine_9_4.setObjectName(u"btn_mine_9_4")
        self.btn_mine_9_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_4, 9, 4, 1, 1)

        self.btn_mine_4_1 = QPushButton(self.mineLayout)
        self.btn_mine_4_1.setObjectName(u"btn_mine_4_1")
        self.btn_mine_4_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_1, 4, 1, 1, 1)

        self.btn_mine_1_7 = QPushButton(self.mineLayout)
        self.btn_mine_1_7.setObjectName(u"btn_mine_1_7")
        self.btn_mine_1_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_7, 1, 7, 1, 1)

        self.btn_mine_14_4 = QPushButton(self.mineLayout)
        self.btn_mine_14_4.setObjectName(u"btn_mine_14_4")
        self.btn_mine_14_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_4, 14, 4, 1, 1)

        self.btn_mine_4_4 = QPushButton(self.mineLayout)
        self.btn_mine_4_4.setObjectName(u"btn_mine_4_4")
        self.btn_mine_4_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_4, 4, 4, 1, 1)

        self.btn_mine_7_8 = QPushButton(self.mineLayout)
        self.btn_mine_7_8.setObjectName(u"btn_mine_7_8")
        self.btn_mine_7_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_8, 7, 8, 1, 1)

        self.btn_mine_8_7 = QPushButton(self.mineLayout)
        self.btn_mine_8_7.setObjectName(u"btn_mine_8_7")
        self.btn_mine_8_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_7, 8, 7, 1, 1)

        self.btn_mine_7_5 = QPushButton(self.mineLayout)
        self.btn_mine_7_5.setObjectName(u"btn_mine_7_5")
        self.btn_mine_7_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_5, 7, 5, 1, 1)

        self.btn_mine_7_6 = QPushButton(self.mineLayout)
        self.btn_mine_7_6.setObjectName(u"btn_mine_7_6")
        self.btn_mine_7_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_6, 7, 6, 1, 1)

        self.btn_mine_6_6 = QPushButton(self.mineLayout)
        self.btn_mine_6_6.setObjectName(u"btn_mine_6_6")
        self.btn_mine_6_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_6, 6, 6, 1, 1)

        self.btn_mine_11_3 = QPushButton(self.mineLayout)
        self.btn_mine_11_3.setObjectName(u"btn_mine_11_3")
        self.btn_mine_11_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_3, 11, 3, 1, 1)

        self.btn_mine_6_8 = QPushButton(self.mineLayout)
        self.btn_mine_6_8.setObjectName(u"btn_mine_6_8")
        self.btn_mine_6_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_8, 6, 8, 1, 1)

        self.btn_mine_1_6 = QPushButton(self.mineLayout)
        self.btn_mine_1_6.setObjectName(u"btn_mine_1_6")
        self.btn_mine_1_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_6, 1, 6, 1, 1)

        self.btn_mine_14_1 = QPushButton(self.mineLayout)
        self.btn_mine_14_1.setObjectName(u"btn_mine_14_1")
        self.btn_mine_14_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_1, 14, 1, 1, 1)

        self.btn_mine_8_2 = QPushButton(self.mineLayout)
        self.btn_mine_8_2.setObjectName(u"btn_mine_8_2")
        self.btn_mine_8_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_2, 8, 2, 1, 1)

        self.btn_mine_12_1 = QPushButton(self.mineLayout)
        self.btn_mine_12_1.setObjectName(u"btn_mine_12_1")
        self.btn_mine_12_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_1, 12, 1, 1, 1)

        self.btn_mine_11_4 = QPushButton(self.mineLayout)
        self.btn_mine_11_4.setObjectName(u"btn_mine_11_4")
        self.btn_mine_11_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_4, 11, 4, 1, 1)

        self.btn_mine_3_2 = QPushButton(self.mineLayout)
        self.btn_mine_3_2.setObjectName(u"btn_mine_3_2")
        self.btn_mine_3_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_2, 3, 2, 1, 1)

        self.btn_mine_15_4 = QPushButton(self.mineLayout)
        self.btn_mine_15_4.setObjectName(u"btn_mine_15_4")
        self.btn_mine_15_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_4, 15, 4, 1, 1)

        self.btn_mine_2_6 = QPushButton(self.mineLayout)
        self.btn_mine_2_6.setObjectName(u"btn_mine_2_6")
        self.btn_mine_2_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_6, 2, 6, 1, 1)

        self.btn_mine_8_8 = QPushButton(self.mineLayout)
        self.btn_mine_8_8.setObjectName(u"btn_mine_8_8")
        self.btn_mine_8_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_8, 8, 8, 1, 1)

        self.btn_mine_12_0 = QPushButton(self.mineLayout)
        self.btn_mine_12_0.setObjectName(u"btn_mine_12_0")
        self.btn_mine_12_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_0, 12, 0, 1, 1)

        self.btn_mine_14_5 = QPushButton(self.mineLayout)
        self.btn_mine_14_5.setObjectName(u"btn_mine_14_5")
        self.btn_mine_14_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_5, 14, 5, 1, 1)

        self.btn_mine_5_4 = QPushButton(self.mineLayout)
        self.btn_mine_5_4.setObjectName(u"btn_mine_5_4")
        self.btn_mine_5_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_4, 5, 4, 1, 1)

        self.btn_mine_4_0 = QPushButton(self.mineLayout)
        self.btn_mine_4_0.setObjectName(u"btn_mine_4_0")
        self.btn_mine_4_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_0, 4, 0, 1, 1)

        self.btn_mine_2_5 = QPushButton(self.mineLayout)
        self.btn_mine_2_5.setObjectName(u"btn_mine_2_5")
        self.btn_mine_2_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_5, 2, 5, 1, 1)

        self.btn_mine_8_3 = QPushButton(self.mineLayout)
        self.btn_mine_8_3.setObjectName(u"btn_mine_8_3")
        self.btn_mine_8_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_3, 8, 3, 1, 1)

        self.btn_mine_9_6 = QPushButton(self.mineLayout)
        self.btn_mine_9_6.setObjectName(u"btn_mine_9_6")
        self.btn_mine_9_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_6, 9, 6, 1, 1)

        self.btn_mine_15_2 = QPushButton(self.mineLayout)
        self.btn_mine_15_2.setObjectName(u"btn_mine_15_2")
        self.btn_mine_15_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_2, 15, 2, 1, 1)

        self.btn_mine_9_2 = QPushButton(self.mineLayout)
        self.btn_mine_9_2.setObjectName(u"btn_mine_9_2")
        self.btn_mine_9_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_2, 9, 2, 1, 1)

        self.btn_mine_14_0 = QPushButton(self.mineLayout)
        self.btn_mine_14_0.setObjectName(u"btn_mine_14_0")
        self.btn_mine_14_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_0, 14, 0, 1, 1)

        self.btn_mine_4_7 = QPushButton(self.mineLayout)
        self.btn_mine_4_7.setObjectName(u"btn_mine_4_7")
        self.btn_mine_4_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_7, 4, 7, 1, 1)

        self.btn_mine_4_2 = QPushButton(self.mineLayout)
        self.btn_mine_4_2.setObjectName(u"btn_mine_4_2")
        self.btn_mine_4_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_2, 4, 2, 1, 1)

        self.btn_mine_14_3 = QPushButton(self.mineLayout)
        self.btn_mine_14_3.setObjectName(u"btn_mine_14_3")
        self.btn_mine_14_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_3, 14, 3, 1, 1)

        self.btn_mine_3_3 = QPushButton(self.mineLayout)
        self.btn_mine_3_3.setObjectName(u"btn_mine_3_3")
        self.btn_mine_3_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_3, 3, 3, 1, 1)

        self.btn_mine_10_1 = QPushButton(self.mineLayout)
        self.btn_mine_10_1.setObjectName(u"btn_mine_10_1")
        self.btn_mine_10_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_1, 10, 1, 1, 1)

        self.btn_mine_9_5 = QPushButton(self.mineLayout)
        self.btn_mine_9_5.setObjectName(u"btn_mine_9_5")
        self.btn_mine_9_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_5, 9, 5, 1, 1)

        self.btn_mine_5_7 = QPushButton(self.mineLayout)
        self.btn_mine_5_7.setObjectName(u"btn_mine_5_7")
        self.btn_mine_5_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_7, 5, 7, 1, 1)

        self.btn_mine_11_1 = QPushButton(self.mineLayout)
        self.btn_mine_11_1.setObjectName(u"btn_mine_11_1")
        self.btn_mine_11_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_1, 11, 1, 1, 1)

        self.btn_mine_13_0 = QPushButton(self.mineLayout)
        self.btn_mine_13_0.setObjectName(u"btn_mine_13_0")
        self.btn_mine_13_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_0, 13, 0, 1, 1)

        self.btn_mine_1_4 = QPushButton(self.mineLayout)
        self.btn_mine_1_4.setObjectName(u"btn_mine_1_4")
        self.btn_mine_1_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_4, 1, 4, 1, 1)

        self.btn_mine_3_5 = QPushButton(self.mineLayout)
        self.btn_mine_3_5.setObjectName(u"btn_mine_3_5")
        self.btn_mine_3_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_5, 3, 5, 1, 1)

        self.btn_mine_13_7 = QPushButton(self.mineLayout)
        self.btn_mine_13_7.setObjectName(u"btn_mine_13_7")
        self.btn_mine_13_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_7, 13, 7, 1, 1)

        self.btn_mine_4_5 = QPushButton(self.mineLayout)
        self.btn_mine_4_5.setObjectName(u"btn_mine_4_5")
        self.btn_mine_4_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_5, 4, 5, 1, 1)

        self.btn_mine_1_0 = QPushButton(self.mineLayout)
        self.btn_mine_1_0.setObjectName(u"btn_mine_1_0")
        self.btn_mine_1_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_0, 1, 0, 1, 1)

        self.btn_mine_1_3 = QPushButton(self.mineLayout)
        self.btn_mine_1_3.setObjectName(u"btn_mine_1_3")
        self.btn_mine_1_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_3, 1, 3, 1, 1)

        self.btn_mine_2_3 = QPushButton(self.mineLayout)
        self.btn_mine_2_3.setObjectName(u"btn_mine_2_3")
        self.btn_mine_2_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_3, 2, 3, 1, 1)

        self.btn_mine_9_0 = QPushButton(self.mineLayout)
        self.btn_mine_9_0.setObjectName(u"btn_mine_9_0")
        self.btn_mine_9_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_0, 9, 0, 1, 1)

        self.btn_mine_5_3 = QPushButton(self.mineLayout)
        self.btn_mine_5_3.setObjectName(u"btn_mine_5_3")
        self.btn_mine_5_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_3, 5, 3, 1, 1)

        self.btn_mine_8_1 = QPushButton(self.mineLayout)
        self.btn_mine_8_1.setObjectName(u"btn_mine_8_1")
        self.btn_mine_8_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_1, 8, 1, 1, 1)

        self.btn_mine_5_8 = QPushButton(self.mineLayout)
        self.btn_mine_5_8.setObjectName(u"btn_mine_5_8")
        self.btn_mine_5_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_8, 5, 8, 1, 1)

        self.btn_mine_11_6 = QPushButton(self.mineLayout)
        self.btn_mine_11_6.setObjectName(u"btn_mine_11_6")
        self.btn_mine_11_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_6, 11, 6, 1, 1)

        self.btn_mine_7_7 = QPushButton(self.mineLayout)
        self.btn_mine_7_7.setObjectName(u"btn_mine_7_7")
        self.btn_mine_7_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_7, 7, 7, 1, 1)

        self.btn_mine_6_2 = QPushButton(self.mineLayout)
        self.btn_mine_6_2.setObjectName(u"btn_mine_6_2")
        self.btn_mine_6_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_2, 6, 2, 1, 1)

        self.btn_mine_10_5 = QPushButton(self.mineLayout)
        self.btn_mine_10_5.setObjectName(u"btn_mine_10_5")
        self.btn_mine_10_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_5, 10, 5, 1, 1)

        self.btn_mine_4_6 = QPushButton(self.mineLayout)
        self.btn_mine_4_6.setObjectName(u"btn_mine_4_6")
        self.btn_mine_4_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_6, 4, 6, 1, 1)

        self.btn_mine_7_1 = QPushButton(self.mineLayout)
        self.btn_mine_7_1.setObjectName(u"btn_mine_7_1")
        self.btn_mine_7_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_1, 7, 1, 1, 1)

        self.btn_mine_15_7 = QPushButton(self.mineLayout)
        self.btn_mine_15_7.setObjectName(u"btn_mine_15_7")
        self.btn_mine_15_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_7, 15, 7, 1, 1)

        self.btn_mine_10_4 = QPushButton(self.mineLayout)
        self.btn_mine_10_4.setObjectName(u"btn_mine_10_4")
        self.btn_mine_10_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_4, 10, 4, 1, 1)

        self.btn_mine_1_1 = QPushButton(self.mineLayout)
        self.btn_mine_1_1.setObjectName(u"btn_mine_1_1")
        self.btn_mine_1_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_1, 1, 1, 1, 1)

        self.btn_mine_10_6 = QPushButton(self.mineLayout)
        self.btn_mine_10_6.setObjectName(u"btn_mine_10_6")
        self.btn_mine_10_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_6, 10, 6, 1, 1)

        self.btn_mine_6_4 = QPushButton(self.mineLayout)
        self.btn_mine_6_4.setObjectName(u"btn_mine_6_4")
        self.btn_mine_6_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_4, 6, 4, 1, 1)

        self.btn_mine_8_6 = QPushButton(self.mineLayout)
        self.btn_mine_8_6.setObjectName(u"btn_mine_8_6")
        self.btn_mine_8_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_6, 8, 6, 1, 1)

        self.btn_mine_6_3 = QPushButton(self.mineLayout)
        self.btn_mine_6_3.setObjectName(u"btn_mine_6_3")
        self.btn_mine_6_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_3, 6, 3, 1, 1)

        self.btn_mine_13_2 = QPushButton(self.mineLayout)
        self.btn_mine_13_2.setObjectName(u"btn_mine_13_2")
        self.btn_mine_13_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_2, 13, 2, 1, 1)

        self.btn_mine_11_2 = QPushButton(self.mineLayout)
        self.btn_mine_11_2.setObjectName(u"btn_mine_11_2")
        self.btn_mine_11_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_2, 11, 2, 1, 1)

        self.btn_mine_1_5 = QPushButton(self.mineLayout)
        self.btn_mine_1_5.setObjectName(u"btn_mine_1_5")
        self.btn_mine_1_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_1_5, 1, 5, 1, 1)

        self.btn_mine_14_8 = QPushButton(self.mineLayout)
        self.btn_mine_14_8.setObjectName(u"btn_mine_14_8")
        self.btn_mine_14_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_8, 14, 8, 1, 1)

        self.btn_mine_12_6 = QPushButton(self.mineLayout)
        self.btn_mine_12_6.setObjectName(u"btn_mine_12_6")
        self.btn_mine_12_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_6, 12, 6, 1, 1)

        self.btn_mine_13_1 = QPushButton(self.mineLayout)
        self.btn_mine_13_1.setObjectName(u"btn_mine_13_1")
        self.btn_mine_13_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_1, 13, 1, 1, 1)

        self.btn_mine_12_3 = QPushButton(self.mineLayout)
        self.btn_mine_12_3.setObjectName(u"btn_mine_12_3")
        self.btn_mine_12_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_3, 12, 3, 1, 1)

        self.btn_mine_8_4 = QPushButton(self.mineLayout)
        self.btn_mine_8_4.setObjectName(u"btn_mine_8_4")
        self.btn_mine_8_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_4, 8, 4, 1, 1)

        self.btn_mine_14_2 = QPushButton(self.mineLayout)
        self.btn_mine_14_2.setObjectName(u"btn_mine_14_2")
        self.btn_mine_14_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_14_2, 14, 2, 1, 1)

        self.btn_mine_4_3 = QPushButton(self.mineLayout)
        self.btn_mine_4_3.setObjectName(u"btn_mine_4_3")
        self.btn_mine_4_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_3, 4, 3, 1, 1)

        self.btn_mine_9_7 = QPushButton(self.mineLayout)
        self.btn_mine_9_7.setObjectName(u"btn_mine_9_7")
        self.btn_mine_9_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_7, 9, 7, 1, 1)

        self.btn_mine_6_1 = QPushButton(self.mineLayout)
        self.btn_mine_6_1.setObjectName(u"btn_mine_6_1")
        self.btn_mine_6_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_6_1, 6, 1, 1, 1)

        self.btn_mine_8_0 = QPushButton(self.mineLayout)
        self.btn_mine_8_0.setObjectName(u"btn_mine_8_0")
        self.btn_mine_8_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_0, 8, 0, 1, 1)

        self.btn_mine_15_6 = QPushButton(self.mineLayout)
        self.btn_mine_15_6.setObjectName(u"btn_mine_15_6")
        self.btn_mine_15_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_6, 15, 6, 1, 1)

        self.btn_mine_8_5 = QPushButton(self.mineLayout)
        self.btn_mine_8_5.setObjectName(u"btn_mine_8_5")
        self.btn_mine_8_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_8_5, 8, 5, 1, 1)

        self.btn_mine_10_8 = QPushButton(self.mineLayout)
        self.btn_mine_10_8.setObjectName(u"btn_mine_10_8")
        self.btn_mine_10_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_8, 10, 8, 1, 1)

        self.btn_mine_12_4 = QPushButton(self.mineLayout)
        self.btn_mine_12_4.setObjectName(u"btn_mine_12_4")
        self.btn_mine_12_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_4, 12, 4, 1, 1)

        self.btn_mine_9_1 = QPushButton(self.mineLayout)
        self.btn_mine_9_1.setObjectName(u"btn_mine_9_1")
        self.btn_mine_9_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_1, 9, 1, 1, 1)

        self.btn_mine_4_8 = QPushButton(self.mineLayout)
        self.btn_mine_4_8.setObjectName(u"btn_mine_4_8")
        self.btn_mine_4_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_4_8, 4, 8, 1, 1)

        self.btn_mine_2_4 = QPushButton(self.mineLayout)
        self.btn_mine_2_4.setObjectName(u"btn_mine_2_4")
        self.btn_mine_2_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_4, 2, 4, 1, 1)

        self.btn_mine_5_5 = QPushButton(self.mineLayout)
        self.btn_mine_5_5.setObjectName(u"btn_mine_5_5")
        self.btn_mine_5_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_5_5, 5, 5, 1, 1)

        self.btn_mine_12_8 = QPushButton(self.mineLayout)
        self.btn_mine_12_8.setObjectName(u"btn_mine_12_8")
        self.btn_mine_12_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_12_8, 12, 8, 1, 1)

        self.btn_mine_2_0 = QPushButton(self.mineLayout)
        self.btn_mine_2_0.setObjectName(u"btn_mine_2_0")
        self.btn_mine_2_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_0, 2, 0, 1, 1)

        self.btn_mine_9_3 = QPushButton(self.mineLayout)
        self.btn_mine_9_3.setObjectName(u"btn_mine_9_3")
        self.btn_mine_9_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_3, 9, 3, 1, 1)

        self.btn_mine_15_0 = QPushButton(self.mineLayout)
        self.btn_mine_15_0.setObjectName(u"btn_mine_15_0")
        self.btn_mine_15_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_15_0, 15, 0, 1, 1)

        self.btn_mine_10_7 = QPushButton(self.mineLayout)
        self.btn_mine_10_7.setObjectName(u"btn_mine_10_7")
        self.btn_mine_10_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_7, 10, 7, 1, 1)

        self.btn_mine_3_7 = QPushButton(self.mineLayout)
        self.btn_mine_3_7.setObjectName(u"btn_mine_3_7")
        self.btn_mine_3_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_7, 3, 7, 1, 1)

        self.btn_mine_9_8 = QPushButton(self.mineLayout)
        self.btn_mine_9_8.setObjectName(u"btn_mine_9_8")
        self.btn_mine_9_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_9_8, 9, 8, 1, 1)

        self.btn_mine_7_4 = QPushButton(self.mineLayout)
        self.btn_mine_7_4.setObjectName(u"btn_mine_7_4")
        self.btn_mine_7_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_4, 7, 4, 1, 1)

        self.btn_mine_11_0 = QPushButton(self.mineLayout)
        self.btn_mine_11_0.setObjectName(u"btn_mine_11_0")
        self.btn_mine_11_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_0, 11, 0, 1, 1)

        self.btn_mine_11_8 = QPushButton(self.mineLayout)
        self.btn_mine_11_8.setObjectName(u"btn_mine_11_8")
        self.btn_mine_11_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_11_8, 11, 8, 1, 1)

        self.btn_mine_2_1 = QPushButton(self.mineLayout)
        self.btn_mine_2_1.setObjectName(u"btn_mine_2_1")
        self.btn_mine_2_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_2_1, 2, 1, 1, 1)

        self.btn_mine_10_3 = QPushButton(self.mineLayout)
        self.btn_mine_10_3.setObjectName(u"btn_mine_10_3")
        self.btn_mine_10_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_10_3, 10, 3, 1, 1)

        self.btn_mine_7_3 = QPushButton(self.mineLayout)
        self.btn_mine_7_3.setObjectName(u"btn_mine_7_3")
        self.btn_mine_7_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_3, 7, 3, 1, 1)

        self.btn_mine_7_0 = QPushButton(self.mineLayout)
        self.btn_mine_7_0.setObjectName(u"btn_mine_7_0")
        self.btn_mine_7_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_7_0, 7, 0, 1, 1)

        self.btn_mine_13_5 = QPushButton(self.mineLayout)
        self.btn_mine_13_5.setObjectName(u"btn_mine_13_5")
        self.btn_mine_13_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_5, 13, 5, 1, 1)

        self.btn_mine_3_6 = QPushButton(self.mineLayout)
        self.btn_mine_3_6.setObjectName(u"btn_mine_3_6")
        self.btn_mine_3_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_3_6, 3, 6, 1, 1)

        self.btn_mine_0_8 = QPushButton(self.mineLayout)
        self.btn_mine_0_8.setObjectName(u"btn_mine_0_8")
        self.btn_mine_0_8.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_8, 0, 8, 1, 1)

        self.btn_mine_0_7 = QPushButton(self.mineLayout)
        self.btn_mine_0_7.setObjectName(u"btn_mine_0_7")
        self.btn_mine_0_7.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_7, 0, 7, 1, 1)

        self.btn_mine_0_6 = QPushButton(self.mineLayout)
        self.btn_mine_0_6.setObjectName(u"btn_mine_0_6")
        self.btn_mine_0_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_6, 0, 6, 1, 1)

        self.btn_mine_0_5 = QPushButton(self.mineLayout)
        self.btn_mine_0_5.setObjectName(u"btn_mine_0_5")
        self.btn_mine_0_5.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_5, 0, 5, 1, 1)

        self.btn_mine_0_4 = QPushButton(self.mineLayout)
        self.btn_mine_0_4.setObjectName(u"btn_mine_0_4")
        self.btn_mine_0_4.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_4, 0, 4, 1, 1)

        self.btn_mine_0_3 = QPushButton(self.mineLayout)
        self.btn_mine_0_3.setObjectName(u"btn_mine_0_3")
        self.btn_mine_0_3.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_3, 0, 3, 1, 1)

        self.btn_mine_0_2 = QPushButton(self.mineLayout)
        self.btn_mine_0_2.setObjectName(u"btn_mine_0_2")
        self.btn_mine_0_2.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_2, 0, 2, 1, 1)

        self.btn_mine_0_1 = QPushButton(self.mineLayout)
        self.btn_mine_0_1.setObjectName(u"btn_mine_0_1")
        self.btn_mine_0_1.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_1, 0, 1, 1, 1)

        self.btn_mine_0_0 = QPushButton(self.mineLayout)
        self.btn_mine_0_0.setObjectName(u"btn_mine_0_0")
        self.btn_mine_0_0.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_0_0, 0, 0, 1, 1)

        self.btn_mine_13_6 = QPushButton(self.mineLayout)
        self.btn_mine_13_6.setObjectName(u"btn_mine_13_6")
        self.btn_mine_13_6.setMaximumSize(QSize(30, 30))

        self.minesLayout.addWidget(self.btn_mine_13_6, 13, 6, 1, 1)


        self.verticalLayout.addWidget(self.mineLayout)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.stackedWidget.addWidget(self.mine)
        self.horse = QWidget()
        self.horse.setObjectName(u"horse")
        self.gridLayout_5 = QGridLayout(self.horse)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_2 = QGroupBox(self.horse)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(361, 421))
        self.groupBox_2.setMaximumSize(QSize(361, 421))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.groupBox_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(111, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.lcd_horse_score = QLCDNumber(self.frame)
        self.lcd_horse_score.setObjectName(u"lcd_horse_score")
        self.lcd_horse_score.setMinimumSize(QSize(80, 30))
        self.lcd_horse_score.setMaximumSize(QSize(80, 30))
        self.lcd_horse_score.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_2.addWidget(self.lcd_horse_score)


        self.verticalLayout_2.addWidget(self.frame)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_horse_0_4 = QPushButton(self.groupBox_2)
        self.btn_horse_0_4.setObjectName(u"btn_horse_0_4")
        self.btn_horse_0_4.setMinimumSize(QSize(40, 40))
        self.btn_horse_0_4.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.btn_horse_0_4.setFont(font2)
        self.btn_horse_0_4.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_0_4, 0, 4, 1, 1)

        self.btn_horse_3_3 = QPushButton(self.groupBox_2)
        self.btn_horse_3_3.setObjectName(u"btn_horse_3_3")
        self.btn_horse_3_3.setMinimumSize(QSize(40, 40))
        self.btn_horse_3_3.setMaximumSize(QSize(40, 40))
        self.btn_horse_3_3.setFont(font2)
        self.btn_horse_3_3.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_3_3, 3, 3, 1, 1)

        self.btn_horse_2_3 = QPushButton(self.groupBox_2)
        self.btn_horse_2_3.setObjectName(u"btn_horse_2_3")
        self.btn_horse_2_3.setMinimumSize(QSize(40, 40))
        self.btn_horse_2_3.setMaximumSize(QSize(40, 40))
        self.btn_horse_2_3.setFont(font2)
        self.btn_horse_2_3.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_2_3, 2, 3, 1, 1)

        self.btn_horse_0_3 = QPushButton(self.groupBox_2)
        self.btn_horse_0_3.setObjectName(u"btn_horse_0_3")
        self.btn_horse_0_3.setMinimumSize(QSize(40, 40))
        self.btn_horse_0_3.setMaximumSize(QSize(40, 40))
        self.btn_horse_0_3.setFont(font2)
        self.btn_horse_0_3.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_0_3, 0, 3, 1, 1)

        self.btn_horse_4_1 = QPushButton(self.groupBox_2)
        self.btn_horse_4_1.setObjectName(u"btn_horse_4_1")
        self.btn_horse_4_1.setMinimumSize(QSize(40, 40))
        self.btn_horse_4_1.setMaximumSize(QSize(40, 40))
        self.btn_horse_4_1.setFont(font2)
        self.btn_horse_4_1.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_4_1, 4, 1, 1, 1)

        self.btn_horse_5_6 = QPushButton(self.groupBox_2)
        self.btn_horse_5_6.setObjectName(u"btn_horse_5_6")
        self.btn_horse_5_6.setMinimumSize(QSize(40, 40))
        self.btn_horse_5_6.setMaximumSize(QSize(40, 40))
        self.btn_horse_5_6.setFont(font2)
        self.btn_horse_5_6.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_5_6, 5, 6, 1, 1)

        self.btn_horse_7_6 = QPushButton(self.groupBox_2)
        self.btn_horse_7_6.setObjectName(u"btn_horse_7_6")
        self.btn_horse_7_6.setMinimumSize(QSize(40, 40))
        self.btn_horse_7_6.setMaximumSize(QSize(40, 40))
        self.btn_horse_7_6.setFont(font2)
        self.btn_horse_7_6.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_7_6, 7, 6, 1, 1)

        self.btn_horse_3_0 = QPushButton(self.groupBox_2)
        self.btn_horse_3_0.setObjectName(u"btn_horse_3_0")
        self.btn_horse_3_0.setMinimumSize(QSize(40, 40))
        self.btn_horse_3_0.setMaximumSize(QSize(40, 40))
        self.btn_horse_3_0.setFont(font2)
        self.btn_horse_3_0.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_3_0, 3, 0, 1, 1)

        self.btn_horse_4_7 = QPushButton(self.groupBox_2)
        self.btn_horse_4_7.setObjectName(u"btn_horse_4_7")
        self.btn_horse_4_7.setMinimumSize(QSize(40, 40))
        self.btn_horse_4_7.setMaximumSize(QSize(40, 40))
        self.btn_horse_4_7.setFont(font2)
        self.btn_horse_4_7.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_4_7, 4, 7, 1, 1)

        self.btn_horse_4_5 = QPushButton(self.groupBox_2)
        self.btn_horse_4_5.setObjectName(u"btn_horse_4_5")
        self.btn_horse_4_5.setMinimumSize(QSize(40, 40))
        self.btn_horse_4_5.setMaximumSize(QSize(40, 40))
        self.btn_horse_4_5.setFont(font2)
        self.btn_horse_4_5.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_4_5, 4, 5, 1, 1)

        self.btn_horse_2_0 = QPushButton(self.groupBox_2)
        self.btn_horse_2_0.setObjectName(u"btn_horse_2_0")
        self.btn_horse_2_0.setMinimumSize(QSize(40, 40))
        self.btn_horse_2_0.setMaximumSize(QSize(40, 40))
        self.btn_horse_2_0.setFont(font2)
        self.btn_horse_2_0.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_2_0, 2, 0, 1, 1)

        self.btn_horse_6_4 = QPushButton(self.groupBox_2)
        self.btn_horse_6_4.setObjectName(u"btn_horse_6_4")
        self.btn_horse_6_4.setMinimumSize(QSize(40, 40))
        self.btn_horse_6_4.setMaximumSize(QSize(40, 40))
        self.btn_horse_6_4.setFont(font2)
        self.btn_horse_6_4.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_6_4, 6, 4, 1, 1)

        self.btn_horse_2_7 = QPushButton(self.groupBox_2)
        self.btn_horse_2_7.setObjectName(u"btn_horse_2_7")
        self.btn_horse_2_7.setMinimumSize(QSize(40, 40))
        self.btn_horse_2_7.setMaximumSize(QSize(40, 40))
        self.btn_horse_2_7.setFont(font2)
        self.btn_horse_2_7.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_2_7, 2, 7, 1, 1)

        self.btn_horse_5_4 = QPushButton(self.groupBox_2)
        self.btn_horse_5_4.setObjectName(u"btn_horse_5_4")
        self.btn_horse_5_4.setMinimumSize(QSize(40, 40))
        self.btn_horse_5_4.setMaximumSize(QSize(40, 40))
        self.btn_horse_5_4.setFont(font2)
        self.btn_horse_5_4.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_5_4, 5, 4, 1, 1)

        self.btn_horse_6_7 = QPushButton(self.groupBox_2)
        self.btn_horse_6_7.setObjectName(u"btn_horse_6_7")
        self.btn_horse_6_7.setMinimumSize(QSize(40, 40))
        self.btn_horse_6_7.setMaximumSize(QSize(40, 40))
        self.btn_horse_6_7.setFont(font2)
        self.btn_horse_6_7.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_6_7, 6, 7, 1, 1)

        self.btn_horse_1_3 = QPushButton(self.groupBox_2)
        self.btn_horse_1_3.setObjectName(u"btn_horse_1_3")
        self.btn_horse_1_3.setMinimumSize(QSize(40, 40))
        self.btn_horse_1_3.setMaximumSize(QSize(40, 40))
        self.btn_horse_1_3.setFont(font2)
        self.btn_horse_1_3.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_1_3, 1, 3, 1, 1)

        self.btn_horse_6_1 = QPushButton(self.groupBox_2)
        self.btn_horse_6_1.setObjectName(u"btn_horse_6_1")
        self.btn_horse_6_1.setMinimumSize(QSize(40, 40))
        self.btn_horse_6_1.setMaximumSize(QSize(40, 40))
        self.btn_horse_6_1.setFont(font2)
        self.btn_horse_6_1.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_6_1, 6, 1, 1, 1)

        self.btn_horse_2_4 = QPushButton(self.groupBox_2)
        self.btn_horse_2_4.setObjectName(u"btn_horse_2_4")
        self.btn_horse_2_4.setMinimumSize(QSize(40, 40))
        self.btn_horse_2_4.setMaximumSize(QSize(40, 40))
        self.btn_horse_2_4.setFont(font2)
        self.btn_horse_2_4.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_2_4, 2, 4, 1, 1)

        self.btn_horse_0_0 = QPushButton(self.groupBox_2)
        self.btn_horse_0_0.setObjectName(u"btn_horse_0_0")
        self.btn_horse_0_0.setMinimumSize(QSize(40, 40))
        self.btn_horse_0_0.setMaximumSize(QSize(40, 40))
        self.btn_horse_0_0.setFont(font2)
        self.btn_horse_0_0.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_0_0, 0, 0, 1, 1)

        self.btn_horse_7_7 = QPushButton(self.groupBox_2)
        self.btn_horse_7_7.setObjectName(u"btn_horse_7_7")
        self.btn_horse_7_7.setMinimumSize(QSize(40, 40))
        self.btn_horse_7_7.setMaximumSize(QSize(40, 40))
        self.btn_horse_7_7.setFont(font2)
        self.btn_horse_7_7.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_7_7, 7, 7, 1, 1)

        self.btn_horse_7_2 = QPushButton(self.groupBox_2)
        self.btn_horse_7_2.setObjectName(u"btn_horse_7_2")
        self.btn_horse_7_2.setMinimumSize(QSize(40, 40))
        self.btn_horse_7_2.setMaximumSize(QSize(40, 40))
        self.btn_horse_7_2.setFont(font2)
        self.btn_horse_7_2.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_7_2, 7, 2, 1, 1)

        self.btn_horse_5_0 = QPushButton(self.groupBox_2)
        self.btn_horse_5_0.setObjectName(u"btn_horse_5_0")
        self.btn_horse_5_0.setMinimumSize(QSize(40, 40))
        self.btn_horse_5_0.setMaximumSize(QSize(40, 40))
        self.btn_horse_5_0.setFont(font2)
        self.btn_horse_5_0.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_5_0, 5, 0, 1, 1)

        self.btn_horse_5_1 = QPushButton(self.groupBox_2)
        self.btn_horse_5_1.setObjectName(u"btn_horse_5_1")
        self.btn_horse_5_1.setMinimumSize(QSize(40, 40))
        self.btn_horse_5_1.setMaximumSize(QSize(40, 40))
        self.btn_horse_5_1.setFont(font2)
        self.btn_horse_5_1.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_5_1, 5, 1, 1, 1)

        self.btn_horse_6_2 = QPushButton(self.groupBox_2)
        self.btn_horse_6_2.setObjectName(u"btn_horse_6_2")
        self.btn_horse_6_2.setMinimumSize(QSize(40, 40))
        self.btn_horse_6_2.setMaximumSize(QSize(40, 40))
        self.btn_horse_6_2.setFont(font2)
        self.btn_horse_6_2.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_6_2, 6, 2, 1, 1)

        self.btn_horse_0_1 = QPushButton(self.groupBox_2)
        self.btn_horse_0_1.setObjectName(u"btn_horse_0_1")
        self.btn_horse_0_1.setMinimumSize(QSize(40, 40))
        self.btn_horse_0_1.setMaximumSize(QSize(40, 40))
        self.btn_horse_0_1.setFont(font2)
        self.btn_horse_0_1.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_0_1, 0, 1, 1, 1)

        self.btn_horse_7_0 = QPushButton(self.groupBox_2)
        self.btn_horse_7_0.setObjectName(u"btn_horse_7_0")
        self.btn_horse_7_0.setMinimumSize(QSize(40, 40))
        self.btn_horse_7_0.setMaximumSize(QSize(40, 40))
        self.btn_horse_7_0.setFont(font2)
        self.btn_horse_7_0.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_7_0, 7, 0, 1, 1)

        self.btn_horse_6_5 = QPushButton(self.groupBox_2)
        self.btn_horse_6_5.setObjectName(u"btn_horse_6_5")
        self.btn_horse_6_5.setMinimumSize(QSize(40, 40))
        self.btn_horse_6_5.setMaximumSize(QSize(40, 40))
        self.btn_horse_6_5.setFont(font2)
        self.btn_horse_6_5.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_6_5, 6, 5, 1, 1)

        self.btn_horse_0_6 = QPushButton(self.groupBox_2)
        self.btn_horse_0_6.setObjectName(u"btn_horse_0_6")
        self.btn_horse_0_6.setMinimumSize(QSize(40, 40))
        self.btn_horse_0_6.setMaximumSize(QSize(40, 40))
        self.btn_horse_0_6.setFont(font2)
        self.btn_horse_0_6.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_0_6, 0, 6, 1, 1)

        self.btn_horse_0_7 = QPushButton(self.groupBox_2)
        self.btn_horse_0_7.setObjectName(u"btn_horse_0_7")
        self.btn_horse_0_7.setMinimumSize(QSize(40, 40))
        self.btn_horse_0_7.setMaximumSize(QSize(40, 40))
        self.btn_horse_0_7.setFont(font2)
        self.btn_horse_0_7.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_0_7, 0, 7, 1, 1)

        self.btn_horse_2_1 = QPushButton(self.groupBox_2)
        self.btn_horse_2_1.setObjectName(u"btn_horse_2_1")
        self.btn_horse_2_1.setMinimumSize(QSize(40, 40))
        self.btn_horse_2_1.setMaximumSize(QSize(40, 40))
        self.btn_horse_2_1.setFont(font2)
        self.btn_horse_2_1.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_2_1, 2, 1, 1, 1)

        self.btn_horse_1_7 = QPushButton(self.groupBox_2)
        self.btn_horse_1_7.setObjectName(u"btn_horse_1_7")
        self.btn_horse_1_7.setMinimumSize(QSize(40, 40))
        self.btn_horse_1_7.setMaximumSize(QSize(40, 40))
        self.btn_horse_1_7.setFont(font2)
        self.btn_horse_1_7.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_1_7, 1, 7, 1, 1)

        self.btn_horse_3_1 = QPushButton(self.groupBox_2)
        self.btn_horse_3_1.setObjectName(u"btn_horse_3_1")
        self.btn_horse_3_1.setMinimumSize(QSize(40, 40))
        self.btn_horse_3_1.setMaximumSize(QSize(40, 40))
        self.btn_horse_3_1.setFont(font2)
        self.btn_horse_3_1.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_3_1, 3, 1, 1, 1)

        self.btn_horse_5_7 = QPushButton(self.groupBox_2)
        self.btn_horse_5_7.setObjectName(u"btn_horse_5_7")
        self.btn_horse_5_7.setMinimumSize(QSize(40, 40))
        self.btn_horse_5_7.setMaximumSize(QSize(40, 40))
        self.btn_horse_5_7.setFont(font2)
        self.btn_horse_5_7.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_5_7, 5, 7, 1, 1)

        self.btn_horse_6_3 = QPushButton(self.groupBox_2)
        self.btn_horse_6_3.setObjectName(u"btn_horse_6_3")
        self.btn_horse_6_3.setMinimumSize(QSize(40, 40))
        self.btn_horse_6_3.setMaximumSize(QSize(40, 40))
        self.btn_horse_6_3.setFont(font2)
        self.btn_horse_6_3.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_6_3, 6, 3, 1, 1)

        self.btn_horse_5_3 = QPushButton(self.groupBox_2)
        self.btn_horse_5_3.setObjectName(u"btn_horse_5_3")
        self.btn_horse_5_3.setMinimumSize(QSize(40, 40))
        self.btn_horse_5_3.setMaximumSize(QSize(40, 40))
        self.btn_horse_5_3.setFont(font2)
        self.btn_horse_5_3.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_5_3, 5, 3, 1, 1)

        self.btn_horse_5_2 = QPushButton(self.groupBox_2)
        self.btn_horse_5_2.setObjectName(u"btn_horse_5_2")
        self.btn_horse_5_2.setMinimumSize(QSize(40, 40))
        self.btn_horse_5_2.setMaximumSize(QSize(40, 40))
        self.btn_horse_5_2.setFont(font2)
        self.btn_horse_5_2.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_5_2, 5, 2, 1, 1)

        self.btn_horse_3_2 = QPushButton(self.groupBox_2)
        self.btn_horse_3_2.setObjectName(u"btn_horse_3_2")
        self.btn_horse_3_2.setMinimumSize(QSize(40, 40))
        self.btn_horse_3_2.setMaximumSize(QSize(40, 40))
        self.btn_horse_3_2.setFont(font2)
        self.btn_horse_3_2.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_3_2, 3, 2, 1, 1)

        self.btn_horse_4_0 = QPushButton(self.groupBox_2)
        self.btn_horse_4_0.setObjectName(u"btn_horse_4_0")
        self.btn_horse_4_0.setMinimumSize(QSize(40, 40))
        self.btn_horse_4_0.setMaximumSize(QSize(40, 40))
        self.btn_horse_4_0.setFont(font2)
        self.btn_horse_4_0.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_4_0, 4, 0, 1, 1)

        self.btn_horse_4_2 = QPushButton(self.groupBox_2)
        self.btn_horse_4_2.setObjectName(u"btn_horse_4_2")
        self.btn_horse_4_2.setMinimumSize(QSize(40, 40))
        self.btn_horse_4_2.setMaximumSize(QSize(40, 40))
        self.btn_horse_4_2.setFont(font2)
        self.btn_horse_4_2.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_4_2, 4, 2, 1, 1)

        self.btn_horse_7_3 = QPushButton(self.groupBox_2)
        self.btn_horse_7_3.setObjectName(u"btn_horse_7_3")
        self.btn_horse_7_3.setMinimumSize(QSize(40, 40))
        self.btn_horse_7_3.setMaximumSize(QSize(40, 40))
        self.btn_horse_7_3.setFont(font2)
        self.btn_horse_7_3.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_7_3, 7, 3, 1, 1)

        self.btn_horse_1_4 = QPushButton(self.groupBox_2)
        self.btn_horse_1_4.setObjectName(u"btn_horse_1_4")
        self.btn_horse_1_4.setMinimumSize(QSize(40, 40))
        self.btn_horse_1_4.setMaximumSize(QSize(40, 40))
        self.btn_horse_1_4.setFont(font2)
        self.btn_horse_1_4.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_1_4, 1, 4, 1, 1)

        self.btn_horse_6_0 = QPushButton(self.groupBox_2)
        self.btn_horse_6_0.setObjectName(u"btn_horse_6_0")
        self.btn_horse_6_0.setMinimumSize(QSize(40, 40))
        self.btn_horse_6_0.setMaximumSize(QSize(40, 40))
        self.btn_horse_6_0.setFont(font2)
        self.btn_horse_6_0.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_6_0, 6, 0, 1, 1)

        self.btn_horse_2_2 = QPushButton(self.groupBox_2)
        self.btn_horse_2_2.setObjectName(u"btn_horse_2_2")
        self.btn_horse_2_2.setMinimumSize(QSize(40, 40))
        self.btn_horse_2_2.setMaximumSize(QSize(40, 40))
        self.btn_horse_2_2.setFont(font2)
        self.btn_horse_2_2.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_2_2, 2, 2, 1, 1)

        self.btn_horse_3_6 = QPushButton(self.groupBox_2)
        self.btn_horse_3_6.setObjectName(u"btn_horse_3_6")
        self.btn_horse_3_6.setMinimumSize(QSize(40, 40))
        self.btn_horse_3_6.setMaximumSize(QSize(40, 40))
        self.btn_horse_3_6.setFont(font2)
        self.btn_horse_3_6.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_3_6, 3, 6, 1, 1)

        self.btn_horse_1_6 = QPushButton(self.groupBox_2)
        self.btn_horse_1_6.setObjectName(u"btn_horse_1_6")
        self.btn_horse_1_6.setMinimumSize(QSize(40, 40))
        self.btn_horse_1_6.setMaximumSize(QSize(40, 40))
        self.btn_horse_1_6.setFont(font2)
        self.btn_horse_1_6.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_1_6, 1, 6, 1, 1)

        self.btn_horse_2_6 = QPushButton(self.groupBox_2)
        self.btn_horse_2_6.setObjectName(u"btn_horse_2_6")
        self.btn_horse_2_6.setMinimumSize(QSize(40, 40))
        self.btn_horse_2_6.setMaximumSize(QSize(40, 40))
        self.btn_horse_2_6.setFont(font2)
        self.btn_horse_2_6.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_2_6, 2, 6, 1, 1)

        self.btn_horse_7_5 = QPushButton(self.groupBox_2)
        self.btn_horse_7_5.setObjectName(u"btn_horse_7_5")
        self.btn_horse_7_5.setMinimumSize(QSize(40, 40))
        self.btn_horse_7_5.setMaximumSize(QSize(40, 40))
        self.btn_horse_7_5.setFont(font2)
        self.btn_horse_7_5.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_7_5, 7, 5, 1, 1)

        self.btn_horse_7_1 = QPushButton(self.groupBox_2)
        self.btn_horse_7_1.setObjectName(u"btn_horse_7_1")
        self.btn_horse_7_1.setMinimumSize(QSize(40, 40))
        self.btn_horse_7_1.setMaximumSize(QSize(40, 40))
        self.btn_horse_7_1.setFont(font2)
        self.btn_horse_7_1.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_7_1, 7, 1, 1, 1)

        self.btn_horse_4_4 = QPushButton(self.groupBox_2)
        self.btn_horse_4_4.setObjectName(u"btn_horse_4_4")
        self.btn_horse_4_4.setMinimumSize(QSize(40, 40))
        self.btn_horse_4_4.setMaximumSize(QSize(40, 40))
        self.btn_horse_4_4.setFont(font2)
        self.btn_horse_4_4.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_4_4, 4, 4, 1, 1)

        self.btn_horse_4_3 = QPushButton(self.groupBox_2)
        self.btn_horse_4_3.setObjectName(u"btn_horse_4_3")
        self.btn_horse_4_3.setMinimumSize(QSize(40, 40))
        self.btn_horse_4_3.setMaximumSize(QSize(40, 40))
        self.btn_horse_4_3.setFont(font2)
        self.btn_horse_4_3.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_4_3, 4, 3, 1, 1)

        self.btn_horse_3_5 = QPushButton(self.groupBox_2)
        self.btn_horse_3_5.setObjectName(u"btn_horse_3_5")
        self.btn_horse_3_5.setMinimumSize(QSize(40, 40))
        self.btn_horse_3_5.setMaximumSize(QSize(40, 40))
        self.btn_horse_3_5.setFont(font2)
        self.btn_horse_3_5.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_3_5, 3, 5, 1, 1)

        self.btn_horse_5_5 = QPushButton(self.groupBox_2)
        self.btn_horse_5_5.setObjectName(u"btn_horse_5_5")
        self.btn_horse_5_5.setMinimumSize(QSize(40, 40))
        self.btn_horse_5_5.setMaximumSize(QSize(40, 40))
        self.btn_horse_5_5.setFont(font2)
        self.btn_horse_5_5.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_5_5, 5, 5, 1, 1)

        self.btn_horse_1_2 = QPushButton(self.groupBox_2)
        self.btn_horse_1_2.setObjectName(u"btn_horse_1_2")
        self.btn_horse_1_2.setMinimumSize(QSize(40, 40))
        self.btn_horse_1_2.setMaximumSize(QSize(40, 40))
        self.btn_horse_1_2.setFont(font2)
        self.btn_horse_1_2.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_1_2, 1, 2, 1, 1)

        self.btn_horse_3_7 = QPushButton(self.groupBox_2)
        self.btn_horse_3_7.setObjectName(u"btn_horse_3_7")
        self.btn_horse_3_7.setMinimumSize(QSize(40, 40))
        self.btn_horse_3_7.setMaximumSize(QSize(40, 40))
        self.btn_horse_3_7.setFont(font2)
        self.btn_horse_3_7.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_3_7, 3, 7, 1, 1)

        self.btn_horse_1_5 = QPushButton(self.groupBox_2)
        self.btn_horse_1_5.setObjectName(u"btn_horse_1_5")
        self.btn_horse_1_5.setMinimumSize(QSize(40, 40))
        self.btn_horse_1_5.setMaximumSize(QSize(40, 40))
        self.btn_horse_1_5.setFont(font2)
        self.btn_horse_1_5.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_1_5, 1, 5, 1, 1)

        self.btn_horse_4_6 = QPushButton(self.groupBox_2)
        self.btn_horse_4_6.setObjectName(u"btn_horse_4_6")
        self.btn_horse_4_6.setMinimumSize(QSize(40, 40))
        self.btn_horse_4_6.setMaximumSize(QSize(40, 40))
        self.btn_horse_4_6.setFont(font2)
        self.btn_horse_4_6.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_4_6, 4, 6, 1, 1)

        self.btn_horse_0_5 = QPushButton(self.groupBox_2)
        self.btn_horse_0_5.setObjectName(u"btn_horse_0_5")
        self.btn_horse_0_5.setMinimumSize(QSize(40, 40))
        self.btn_horse_0_5.setMaximumSize(QSize(40, 40))
        self.btn_horse_0_5.setFont(font2)
        self.btn_horse_0_5.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_0_5, 0, 5, 1, 1)

        self.btn_horse_1_1 = QPushButton(self.groupBox_2)
        self.btn_horse_1_1.setObjectName(u"btn_horse_1_1")
        self.btn_horse_1_1.setMinimumSize(QSize(40, 40))
        self.btn_horse_1_1.setMaximumSize(QSize(40, 40))
        self.btn_horse_1_1.setFont(font2)
        self.btn_horse_1_1.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_1_1, 1, 1, 1, 1)

        self.btn_horse_1_0 = QPushButton(self.groupBox_2)
        self.btn_horse_1_0.setObjectName(u"btn_horse_1_0")
        self.btn_horse_1_0.setMinimumSize(QSize(40, 40))
        self.btn_horse_1_0.setMaximumSize(QSize(40, 40))
        self.btn_horse_1_0.setFont(font2)
        self.btn_horse_1_0.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_1_0, 1, 0, 1, 1)

        self.btn_horse_2_5 = QPushButton(self.groupBox_2)
        self.btn_horse_2_5.setObjectName(u"btn_horse_2_5")
        self.btn_horse_2_5.setMinimumSize(QSize(40, 40))
        self.btn_horse_2_5.setMaximumSize(QSize(40, 40))
        self.btn_horse_2_5.setFont(font2)
        self.btn_horse_2_5.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_2_5, 2, 5, 1, 1)

        self.btn_horse_0_2 = QPushButton(self.groupBox_2)
        self.btn_horse_0_2.setObjectName(u"btn_horse_0_2")
        self.btn_horse_0_2.setMinimumSize(QSize(40, 40))
        self.btn_horse_0_2.setMaximumSize(QSize(40, 40))
        self.btn_horse_0_2.setFont(font2)
        self.btn_horse_0_2.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_0_2, 0, 2, 1, 1)

        self.btn_horse_7_4 = QPushButton(self.groupBox_2)
        self.btn_horse_7_4.setObjectName(u"btn_horse_7_4")
        self.btn_horse_7_4.setMinimumSize(QSize(40, 40))
        self.btn_horse_7_4.setMaximumSize(QSize(40, 40))
        self.btn_horse_7_4.setFont(font2)
        self.btn_horse_7_4.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_7_4, 7, 4, 1, 1)

        self.btn_horse_3_4 = QPushButton(self.groupBox_2)
        self.btn_horse_3_4.setObjectName(u"btn_horse_3_4")
        self.btn_horse_3_4.setMinimumSize(QSize(40, 40))
        self.btn_horse_3_4.setMaximumSize(QSize(40, 40))
        self.btn_horse_3_4.setFont(font2)
        self.btn_horse_3_4.setStyleSheet(u"background-color: rgb(192, 191, 188); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_3_4, 3, 4, 1, 1)

        self.btn_horse_6_6 = QPushButton(self.groupBox_2)
        self.btn_horse_6_6.setObjectName(u"btn_horse_6_6")
        self.btn_horse_6_6.setMinimumSize(QSize(40, 40))
        self.btn_horse_6_6.setMaximumSize(QSize(40, 40))
        self.btn_horse_6_6.setFont(font2)
        self.btn_horse_6_6.setStyleSheet(u"background-color: rgb(255, 255, 255); border:  1px solid grey")

        self.gridLayout_2.addWidget(self.btn_horse_6_6, 6, 6, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.horse)
        self.wordle = QWidget()
        self.wordle.setObjectName(u"wordle")
        self.gridLayout_8 = QGridLayout(self.wordle)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_6 = QGroupBox(self.wordle)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(320, 420))
        self.groupBox_6.setMaximumSize(QSize(320, 420))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_score = QLabel(self.groupBox_6)
        self.label_score.setObjectName(u"label_score")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_score.setFont(font3)
        self.label_score.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_score)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.btn_wordle_4_1 = QPushButton(self.groupBox_6)
        self.btn_wordle_4_1.setObjectName(u"btn_wordle_4_1")
        self.btn_wordle_4_1.setEnabled(False)
        self.btn_wordle_4_1.setMinimumSize(QSize(50, 50))
        self.btn_wordle_4_1.setMaximumSize(QSize(50, 50))
        self.btn_wordle_4_1.setFont(font2)
        self.btn_wordle_4_1.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_4_1, 4, 1, 1, 1)

        self.btn_wordle_2_0 = QPushButton(self.groupBox_6)
        self.btn_wordle_2_0.setObjectName(u"btn_wordle_2_0")
        self.btn_wordle_2_0.setEnabled(False)
        self.btn_wordle_2_0.setMinimumSize(QSize(50, 50))
        self.btn_wordle_2_0.setMaximumSize(QSize(50, 50))
        self.btn_wordle_2_0.setFont(font2)
        self.btn_wordle_2_0.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_2_0, 2, 0, 1, 1)

        self.btn_wordle_4_3 = QPushButton(self.groupBox_6)
        self.btn_wordle_4_3.setObjectName(u"btn_wordle_4_3")
        self.btn_wordle_4_3.setEnabled(False)
        self.btn_wordle_4_3.setMinimumSize(QSize(50, 50))
        self.btn_wordle_4_3.setMaximumSize(QSize(50, 50))
        self.btn_wordle_4_3.setFont(font2)
        self.btn_wordle_4_3.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_4_3, 4, 3, 1, 1)

        self.btn_wordle_1_2 = QPushButton(self.groupBox_6)
        self.btn_wordle_1_2.setObjectName(u"btn_wordle_1_2")
        self.btn_wordle_1_2.setEnabled(False)
        self.btn_wordle_1_2.setMinimumSize(QSize(50, 50))
        self.btn_wordle_1_2.setMaximumSize(QSize(50, 50))
        self.btn_wordle_1_2.setFont(font2)
        self.btn_wordle_1_2.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_1_2, 1, 2, 1, 1)

        self.btn_wordle_4_0 = QPushButton(self.groupBox_6)
        self.btn_wordle_4_0.setObjectName(u"btn_wordle_4_0")
        self.btn_wordle_4_0.setEnabled(False)
        self.btn_wordle_4_0.setMinimumSize(QSize(50, 50))
        self.btn_wordle_4_0.setMaximumSize(QSize(50, 50))
        self.btn_wordle_4_0.setFont(font2)
        self.btn_wordle_4_0.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_4_0, 4, 0, 1, 1)

        self.btn_wordle_2_2 = QPushButton(self.groupBox_6)
        self.btn_wordle_2_2.setObjectName(u"btn_wordle_2_2")
        self.btn_wordle_2_2.setEnabled(False)
        self.btn_wordle_2_2.setMinimumSize(QSize(50, 50))
        self.btn_wordle_2_2.setMaximumSize(QSize(50, 50))
        self.btn_wordle_2_2.setFont(font2)
        self.btn_wordle_2_2.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_2_2, 2, 2, 1, 1)

        self.btn_wordle_4_4 = QPushButton(self.groupBox_6)
        self.btn_wordle_4_4.setObjectName(u"btn_wordle_4_4")
        self.btn_wordle_4_4.setEnabled(False)
        self.btn_wordle_4_4.setMinimumSize(QSize(50, 50))
        self.btn_wordle_4_4.setMaximumSize(QSize(50, 50))
        self.btn_wordle_4_4.setFont(font2)
        self.btn_wordle_4_4.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_4_4, 4, 4, 1, 1)

        self.btn_wordle_0_3 = QPushButton(self.groupBox_6)
        self.btn_wordle_0_3.setObjectName(u"btn_wordle_0_3")
        self.btn_wordle_0_3.setEnabled(False)
        self.btn_wordle_0_3.setMinimumSize(QSize(50, 50))
        self.btn_wordle_0_3.setMaximumSize(QSize(50, 50))
        self.btn_wordle_0_3.setFont(font2)
        self.btn_wordle_0_3.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_0_3, 0, 3, 1, 1)

        self.btn_wordle_2_3 = QPushButton(self.groupBox_6)
        self.btn_wordle_2_3.setObjectName(u"btn_wordle_2_3")
        self.btn_wordle_2_3.setEnabled(False)
        self.btn_wordle_2_3.setMinimumSize(QSize(50, 50))
        self.btn_wordle_2_3.setMaximumSize(QSize(50, 50))
        self.btn_wordle_2_3.setFont(font2)
        self.btn_wordle_2_3.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_2_3, 2, 3, 1, 1)

        self.btn_wordle_4_2 = QPushButton(self.groupBox_6)
        self.btn_wordle_4_2.setObjectName(u"btn_wordle_4_2")
        self.btn_wordle_4_2.setEnabled(False)
        self.btn_wordle_4_2.setMinimumSize(QSize(50, 50))
        self.btn_wordle_4_2.setMaximumSize(QSize(50, 50))
        self.btn_wordle_4_2.setFont(font2)
        self.btn_wordle_4_2.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_4_2, 4, 2, 1, 1)

        self.btn_wordle_5_0 = QPushButton(self.groupBox_6)
        self.btn_wordle_5_0.setObjectName(u"btn_wordle_5_0")
        self.btn_wordle_5_0.setEnabled(False)
        self.btn_wordle_5_0.setMinimumSize(QSize(50, 50))
        self.btn_wordle_5_0.setMaximumSize(QSize(50, 50))
        self.btn_wordle_5_0.setFont(font2)
        self.btn_wordle_5_0.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_5_0, 5, 0, 1, 1)

        self.btn_wordle_2_1 = QPushButton(self.groupBox_6)
        self.btn_wordle_2_1.setObjectName(u"btn_wordle_2_1")
        self.btn_wordle_2_1.setEnabled(False)
        self.btn_wordle_2_1.setMinimumSize(QSize(50, 50))
        self.btn_wordle_2_1.setMaximumSize(QSize(50, 50))
        self.btn_wordle_2_1.setFont(font2)
        self.btn_wordle_2_1.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_2_1, 2, 1, 1, 1)

        self.btn_wordle_5_2 = QPushButton(self.groupBox_6)
        self.btn_wordle_5_2.setObjectName(u"btn_wordle_5_2")
        self.btn_wordle_5_2.setEnabled(False)
        self.btn_wordle_5_2.setMinimumSize(QSize(50, 50))
        self.btn_wordle_5_2.setMaximumSize(QSize(50, 50))
        self.btn_wordle_5_2.setFont(font2)
        self.btn_wordle_5_2.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_5_2, 5, 2, 1, 1)

        self.btn_wordle_5_3 = QPushButton(self.groupBox_6)
        self.btn_wordle_5_3.setObjectName(u"btn_wordle_5_3")
        self.btn_wordle_5_3.setEnabled(False)
        self.btn_wordle_5_3.setMinimumSize(QSize(50, 50))
        self.btn_wordle_5_3.setMaximumSize(QSize(50, 50))
        self.btn_wordle_5_3.setFont(font2)
        self.btn_wordle_5_3.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_5_3, 5, 3, 1, 1)

        self.btn_wordle_1_1 = QPushButton(self.groupBox_6)
        self.btn_wordle_1_1.setObjectName(u"btn_wordle_1_1")
        self.btn_wordle_1_1.setEnabled(False)
        self.btn_wordle_1_1.setMinimumSize(QSize(50, 50))
        self.btn_wordle_1_1.setMaximumSize(QSize(50, 50))
        self.btn_wordle_1_1.setFont(font2)
        self.btn_wordle_1_1.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_1_1, 1, 1, 1, 1)

        self.btn_wordle_1_3 = QPushButton(self.groupBox_6)
        self.btn_wordle_1_3.setObjectName(u"btn_wordle_1_3")
        self.btn_wordle_1_3.setEnabled(False)
        self.btn_wordle_1_3.setMinimumSize(QSize(50, 50))
        self.btn_wordle_1_3.setMaximumSize(QSize(50, 50))
        self.btn_wordle_1_3.setFont(font2)
        self.btn_wordle_1_3.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_1_3, 1, 3, 1, 1)

        self.btn_wordle_0_0 = QPushButton(self.groupBox_6)
        self.btn_wordle_0_0.setObjectName(u"btn_wordle_0_0")
        self.btn_wordle_0_0.setEnabled(False)
        self.btn_wordle_0_0.setMinimumSize(QSize(50, 50))
        self.btn_wordle_0_0.setMaximumSize(QSize(50, 50))
        self.btn_wordle_0_0.setFont(font2)
        self.btn_wordle_0_0.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_0_0, 0, 0, 1, 1)

        self.btn_wordle_1_0 = QPushButton(self.groupBox_6)
        self.btn_wordle_1_0.setObjectName(u"btn_wordle_1_0")
        self.btn_wordle_1_0.setEnabled(False)
        self.btn_wordle_1_0.setMinimumSize(QSize(50, 50))
        self.btn_wordle_1_0.setMaximumSize(QSize(50, 50))
        self.btn_wordle_1_0.setFont(font2)
        self.btn_wordle_1_0.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_1_0, 1, 0, 1, 1)

        self.btn_wordle_2_4 = QPushButton(self.groupBox_6)
        self.btn_wordle_2_4.setObjectName(u"btn_wordle_2_4")
        self.btn_wordle_2_4.setEnabled(False)
        self.btn_wordle_2_4.setMinimumSize(QSize(50, 50))
        self.btn_wordle_2_4.setMaximumSize(QSize(50, 50))
        self.btn_wordle_2_4.setFont(font2)
        self.btn_wordle_2_4.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_2_4, 2, 4, 1, 1)

        self.btn_wordle_1_4 = QPushButton(self.groupBox_6)
        self.btn_wordle_1_4.setObjectName(u"btn_wordle_1_4")
        self.btn_wordle_1_4.setEnabled(False)
        self.btn_wordle_1_4.setMinimumSize(QSize(50, 50))
        self.btn_wordle_1_4.setMaximumSize(QSize(50, 50))
        self.btn_wordle_1_4.setFont(font2)
        self.btn_wordle_1_4.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_1_4, 1, 4, 1, 1)

        self.btn_wordle_5_1 = QPushButton(self.groupBox_6)
        self.btn_wordle_5_1.setObjectName(u"btn_wordle_5_1")
        self.btn_wordle_5_1.setEnabled(False)
        self.btn_wordle_5_1.setMinimumSize(QSize(50, 50))
        self.btn_wordle_5_1.setMaximumSize(QSize(50, 50))
        self.btn_wordle_5_1.setFont(font2)
        self.btn_wordle_5_1.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_5_1, 5, 1, 1, 1)

        self.btn_wordle_3_4 = QPushButton(self.groupBox_6)
        self.btn_wordle_3_4.setObjectName(u"btn_wordle_3_4")
        self.btn_wordle_3_4.setEnabled(False)
        self.btn_wordle_3_4.setMinimumSize(QSize(50, 50))
        self.btn_wordle_3_4.setMaximumSize(QSize(50, 50))
        self.btn_wordle_3_4.setFont(font2)
        self.btn_wordle_3_4.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_3_4, 3, 4, 1, 1)

        self.btn_wordle_3_2 = QPushButton(self.groupBox_6)
        self.btn_wordle_3_2.setObjectName(u"btn_wordle_3_2")
        self.btn_wordle_3_2.setEnabled(False)
        self.btn_wordle_3_2.setMinimumSize(QSize(50, 50))
        self.btn_wordle_3_2.setMaximumSize(QSize(50, 50))
        self.btn_wordle_3_2.setFont(font2)
        self.btn_wordle_3_2.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_3_2, 3, 2, 1, 1)

        self.btn_wordle_0_4 = QPushButton(self.groupBox_6)
        self.btn_wordle_0_4.setObjectName(u"btn_wordle_0_4")
        self.btn_wordle_0_4.setEnabled(False)
        self.btn_wordle_0_4.setMinimumSize(QSize(50, 50))
        self.btn_wordle_0_4.setMaximumSize(QSize(50, 50))
        self.btn_wordle_0_4.setFont(font2)
        self.btn_wordle_0_4.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_0_4, 0, 4, 1, 1)

        self.btn_wordle_3_3 = QPushButton(self.groupBox_6)
        self.btn_wordle_3_3.setObjectName(u"btn_wordle_3_3")
        self.btn_wordle_3_3.setEnabled(False)
        self.btn_wordle_3_3.setMinimumSize(QSize(50, 50))
        self.btn_wordle_3_3.setMaximumSize(QSize(50, 50))
        self.btn_wordle_3_3.setFont(font2)
        self.btn_wordle_3_3.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_3_3, 3, 3, 1, 1)

        self.btn_wordle_5_4 = QPushButton(self.groupBox_6)
        self.btn_wordle_5_4.setObjectName(u"btn_wordle_5_4")
        self.btn_wordle_5_4.setEnabled(False)
        self.btn_wordle_5_4.setMinimumSize(QSize(50, 50))
        self.btn_wordle_5_4.setMaximumSize(QSize(50, 50))
        self.btn_wordle_5_4.setFont(font2)
        self.btn_wordle_5_4.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_5_4, 5, 4, 1, 1)

        self.btn_wordle_0_1 = QPushButton(self.groupBox_6)
        self.btn_wordle_0_1.setObjectName(u"btn_wordle_0_1")
        self.btn_wordle_0_1.setEnabled(False)
        self.btn_wordle_0_1.setMinimumSize(QSize(50, 50))
        self.btn_wordle_0_1.setMaximumSize(QSize(50, 50))
        self.btn_wordle_0_1.setFont(font2)
        self.btn_wordle_0_1.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_0_1, 0, 1, 1, 1)

        self.btn_wordle_0_2 = QPushButton(self.groupBox_6)
        self.btn_wordle_0_2.setObjectName(u"btn_wordle_0_2")
        self.btn_wordle_0_2.setEnabled(False)
        self.btn_wordle_0_2.setMinimumSize(QSize(50, 50))
        self.btn_wordle_0_2.setMaximumSize(QSize(50, 50))
        self.btn_wordle_0_2.setFont(font2)
        self.btn_wordle_0_2.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_0_2, 0, 2, 1, 1)

        self.btn_wordle_3_1 = QPushButton(self.groupBox_6)
        self.btn_wordle_3_1.setObjectName(u"btn_wordle_3_1")
        self.btn_wordle_3_1.setEnabled(False)
        self.btn_wordle_3_1.setMinimumSize(QSize(50, 50))
        self.btn_wordle_3_1.setMaximumSize(QSize(50, 50))
        self.btn_wordle_3_1.setFont(font2)
        self.btn_wordle_3_1.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_3_1, 3, 1, 1, 1)

        self.btn_wordle_3_0 = QPushButton(self.groupBox_6)
        self.btn_wordle_3_0.setObjectName(u"btn_wordle_3_0")
        self.btn_wordle_3_0.setEnabled(False)
        self.btn_wordle_3_0.setMinimumSize(QSize(50, 50))
        self.btn_wordle_3_0.setMaximumSize(QSize(50, 50))
        self.btn_wordle_3_0.setFont(font2)
        self.btn_wordle_3_0.setStyleSheet(u"        color: rgb(0, 0, 0);\n"
"        background-color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_7.addWidget(self.btn_wordle_3_0, 3, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_7)


        self.gridLayout_8.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.wordle)

        self.verticalLayout_7.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 400, 23))
        self.mainMenu = QMenu(self.menuBar)
        self.mainMenu.setObjectName(u"mainMenu")
        self.menuGame = QMenu(self.menuBar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuGame.setEnabled(True)
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuUpdate = QMenu(self.menuHelp)
        self.menuUpdate.setObjectName(u"menuUpdate")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.mainMenu.menuAction())
        self.menuBar.addAction(self.menuGame.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.mainMenu.addAction(self.actionMenu)
        self.mainMenu.addAction(self.actionScore)
        self.mainMenu.addSeparator()
        self.mainMenu.addAction(self.actionMine)
        self.mainMenu.addAction(self.actionHorse)
        self.mainMenu.addAction(self.actionWordle)
        self.mainMenu.addSeparator()
        self.mainMenu.addAction(self.actionExit)
        self.menuGame.addAction(self.actionReset)
        self.menuHelp.addAction(self.menuUpdate.menuAction())
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuUpdate.addAction(self.actionCheckRun)
        self.menuUpdate.addAction(self.actionCheckNow)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.btn_horse_6_7.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyClassic Games", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"Acerda de...", None))
        self.actionMenu.setText(QCoreApplication.translate("MainWindow", u"Menu Principal", None))
        self.actionMine.setText(QCoreApplication.translate("MainWindow", u"Buscaminas", None))
        self.actionHorse.setText(QCoreApplication.translate("MainWindow", u"Salto del caballo", None))
        self.actionWordle.setText(QCoreApplication.translate("MainWindow", u"Wordle", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionReset.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.actionFacil.setText(QCoreApplication.translate("MainWindow", u"Facil", None))
        self.actionMedio.setText(QCoreApplication.translate("MainWindow", u"Medio", None))
        self.actionDificil.setText(QCoreApplication.translate("MainWindow", u"Dificil", None))
        self.actionPuntuaci_n.setText(QCoreApplication.translate("MainWindow", u"Puntuaci\u00f3n", None))
        self.actionScore.setText(QCoreApplication.translate("MainWindow", u"Puntuaci\u00f3n", None))
        self.actionCheckRun.setText(QCoreApplication.translate("MainWindow", u"Comprobar en inicio", None))
        self.actionCheckNow.setText(QCoreApplication.translate("MainWindow", u"Comprobar ahora", None))
        self.groupBox.setTitle("")
        self.face_btn.setText(QCoreApplication.translate("MainWindow", u"\U0001f60e", None))
        self.btn_mine_6_0.setText("")
        self.btn_mine_6_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_13_8.setText("")
        self.btn_mine_13_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_12_7.setText("")
        self.btn_mine_12_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_13_4.setText("")
        self.btn_mine_13_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_2_2.setText("")
        self.btn_mine_2_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_12_2.setText("")
        self.btn_mine_12_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_13_3.setText("")
        self.btn_mine_13_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_1.setText("")
        self.btn_mine_3_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_10_0.setText("")
        self.btn_mine_10_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_5_0.setText("")
        self.btn_mine_5_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_7_2.setText("")
        self.btn_mine_7_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_5_6.setText("")
        self.btn_mine_5_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_15_8.setText("")
        self.btn_mine_15_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_3_8.setText("")
        self.btn_mine_3_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_15_1.setText("")
        self.btn_mine_15_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_11_7.setText("")
        self.btn_mine_11_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_1_2.setText("")
        self.btn_mine_1_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_8.setText("")
        self.btn_mine_2_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_12_5.setText("")
        self.btn_mine_12_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_14_7.setText("")
        self.btn_mine_14_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_6_5.setText("")
        self.btn_mine_6_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_11_5.setText("")
        self.btn_mine_11_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_10_2.setText("")
        self.btn_mine_10_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_7.setText("")
        self.btn_mine_2_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_5_1.setText("")
        self.btn_mine_5_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_5_2.setText("")
        self.btn_mine_5_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_6_7.setText("")
        self.btn_mine_6_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_1_8.setText("")
        self.btn_mine_1_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_3_4.setText("")
        self.btn_mine_3_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_3_0.setText("")
        self.btn_mine_3_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_15_5.setText("")
        self.btn_mine_15_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_15_3.setText("")
        self.btn_mine_15_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_14_6.setText("")
        self.btn_mine_14_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_9_4.setText("")
        self.btn_mine_9_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_1.setText("")
        self.btn_mine_4_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_7.setText("")
        self.btn_mine_1_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_14_4.setText("")
        self.btn_mine_14_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_4.setText("")
        self.btn_mine_4_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_7_8.setText("")
        self.btn_mine_7_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_7.setText("")
        self.btn_mine_8_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_5.setText("")
        self.btn_mine_7_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_7_6.setText("")
        self.btn_mine_7_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_6.setText("")
        self.btn_mine_6_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_11_3.setText("")
        self.btn_mine_11_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_6_8.setText("")
        self.btn_mine_6_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_1_6.setText("")
        self.btn_mine_1_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_14_1.setText("")
        self.btn_mine_14_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_8_2.setText("")
        self.btn_mine_8_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_12_1.setText("")
        self.btn_mine_12_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_11_4.setText("")
        self.btn_mine_11_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_3_2.setText("")
        self.btn_mine_3_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_15_4.setText("")
        self.btn_mine_15_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_2_6.setText("")
        self.btn_mine_2_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_8_8.setText("")
        self.btn_mine_8_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_12_0.setText("")
        self.btn_mine_12_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_14_5.setText("")
        self.btn_mine_14_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_4.setText("")
        self.btn_mine_5_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_0.setText("")
        self.btn_mine_4_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_2_5.setText("")
        self.btn_mine_2_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_8_3.setText("")
        self.btn_mine_8_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_9_6.setText("")
        self.btn_mine_9_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_15_2.setText("")
        self.btn_mine_15_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_9_2.setText("")
        self.btn_mine_9_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_14_0.setText("")
        self.btn_mine_14_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_4_7.setText("")
        self.btn_mine_4_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_4_2.setText("")
        self.btn_mine_4_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_14_3.setText("")
        self.btn_mine_14_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_3.setText("")
        self.btn_mine_3_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_10_1.setText("")
        self.btn_mine_10_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_9_5.setText("")
        self.btn_mine_9_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_7.setText("")
        self.btn_mine_5_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_11_1.setText("")
        self.btn_mine_11_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_13_0.setText("")
        self.btn_mine_13_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_1_4.setText("")
        self.btn_mine_1_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_3_5.setText("")
        self.btn_mine_3_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_13_7.setText("")
        self.btn_mine_13_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_4_5.setText("")
        self.btn_mine_4_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_1_0.setText("")
        self.btn_mine_1_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_1_3.setText("")
        self.btn_mine_1_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_2_3.setText("")
        self.btn_mine_2_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_9_0.setText("")
        self.btn_mine_9_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_5_3.setText("")
        self.btn_mine_5_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_8_1.setText("")
        self.btn_mine_8_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_5_8.setText("")
        self.btn_mine_5_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_11_6.setText("")
        self.btn_mine_11_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_7_7.setText("")
        self.btn_mine_7_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_6_2.setText("")
        self.btn_mine_6_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_10_5.setText("")
        self.btn_mine_10_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_4_6.setText("")
        self.btn_mine_4_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_7_1.setText("")
        self.btn_mine_7_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_15_7.setText("")
        self.btn_mine_15_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_10_4.setText("")
        self.btn_mine_10_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_1_1.setText("")
        self.btn_mine_1_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_10_6.setText("")
        self.btn_mine_10_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_4.setText("")
        self.btn_mine_6_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_8_6.setText("")
        self.btn_mine_8_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_3.setText("")
        self.btn_mine_6_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_13_2.setText("")
        self.btn_mine_13_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_11_2.setText("")
        self.btn_mine_11_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_1_5.setText("")
        self.btn_mine_1_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_1_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_14_8.setText("")
        self.btn_mine_14_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_12_6.setText("")
        self.btn_mine_12_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_13_1.setText("")
        self.btn_mine_13_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_12_3.setText("")
        self.btn_mine_12_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_8_4.setText("")
        self.btn_mine_8_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_14_2.setText("")
        self.btn_mine_14_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"14", None))
        self.btn_mine_14_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_4_3.setText("")
        self.btn_mine_4_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_9_7.setText("")
        self.btn_mine_9_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_6_1.setText("")
        self.btn_mine_6_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_6_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_8_0.setText("")
        self.btn_mine_8_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_15_6.setText("")
        self.btn_mine_15_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_8_5.setText("")
        self.btn_mine_8_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_8_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_10_8.setText("")
        self.btn_mine_10_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_12_4.setText("")
        self.btn_mine_12_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_9_1.setText("")
        self.btn_mine_9_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_4_8.setText("")
        self.btn_mine_4_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_4_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_2_4.setText("")
        self.btn_mine_2_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_5_5.setText("")
        self.btn_mine_5_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_5_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_12_8.setText("")
        self.btn_mine_12_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"12", None))
        self.btn_mine_12_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_2_0.setText("")
        self.btn_mine_2_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_9_3.setText("")
        self.btn_mine_9_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_15_0.setText("")
        self.btn_mine_15_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"15", None))
        self.btn_mine_15_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_10_7.setText("")
        self.btn_mine_10_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_3_7.setText("")
        self.btn_mine_3_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_9_8.setText("")
        self.btn_mine_9_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_mine_9_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_7_4.setText("")
        self.btn_mine_7_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_11_0.setText("")
        self.btn_mine_11_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_11_8.setText("")
        self.btn_mine_11_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"11", None))
        self.btn_mine_11_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_2_1.setText("")
        self.btn_mine_2_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_2_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_10_3.setText("")
        self.btn_mine_10_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_mine_10_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_7_3.setText("")
        self.btn_mine_7_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_7_0.setText("")
        self.btn_mine_7_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_7_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_13_5.setText("")
        self.btn_mine_13_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_3_6.setText("")
        self.btn_mine_3_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_3_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_0_8.setText("")
        self.btn_mine_0_8.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_8.setProperty(u"col", QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_mine_0_7.setText("")
        self.btn_mine_0_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_mine_0_6.setText("")
        self.btn_mine_0_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_mine_0_5.setText("")
        self.btn_mine_0_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_mine_0_4.setText("")
        self.btn_mine_0_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mine_0_3.setText("")
        self.btn_mine_0_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_mine_0_2.setText("")
        self.btn_mine_0_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_mine_0_1.setText("")
        self.btn_mine_0_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mine_0_0.setText("")
        self.btn_mine_0_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_0_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_mine_13_6.setText("")
        self.btn_mine_13_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"13", None))
        self.btn_mine_13_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.groupBox_2.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cuenta de saltos", None))
        self.btn_horse_0_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_0_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_3_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_2_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_2_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_0_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_0_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_4_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_5_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_7_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_3_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_4_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_4_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_2_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_2_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_6_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_6_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_2_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_2_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_5_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_6_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_6_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_1_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_6_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_6_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_2_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_2_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_0_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_0_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_7_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_5_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_5_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_6_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_6_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_0_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_0_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_7_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_6_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_6_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_0_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_0_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_0_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_0_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_2_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_2_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_3_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_5_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_6_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_6_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_5_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_5_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_3_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_4_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_4_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_7_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_1_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_6_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_6_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_2_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_2_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_3_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_1_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_2_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_2_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_7_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_7_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_4_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_5_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_1_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_3_7.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_7.setProperty(u"col", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_1_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_4_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_4_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_0_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_0_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_1_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_horse_1_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_2_5.setProperty(u"row", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_2_5.setProperty(u"col", QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_horse_0_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_horse_0_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_horse_7_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_horse_7_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_3_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_horse_3_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_horse_6_6.setProperty(u"row", QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_horse_6_6.setProperty(u"col", QCoreApplication.translate("MainWindow", u"6", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\U0001f4b0", None))
        self.label_score.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.btn_wordle_4_1.setText("")
        self.btn_wordle_4_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_0.setText("")
        self.btn_wordle_2_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_3.setText("")
        self.btn_wordle_4_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_2.setText("")
        self.btn_wordle_1_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_0.setText("")
        self.btn_wordle_4_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_2.setText("")
        self.btn_wordle_2_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_4.setText("")
        self.btn_wordle_4_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_3.setText("")
        self.btn_wordle_0_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_3.setText("")
        self.btn_wordle_2_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_2.setText("")
        self.btn_wordle_4_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_4_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_0.setText("")
        self.btn_wordle_5_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_1.setText("")
        self.btn_wordle_2_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_2.setText("")
        self.btn_wordle_5_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_3.setText("")
        self.btn_wordle_5_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_1.setText("")
        self.btn_wordle_1_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_3.setText("")
        self.btn_wordle_1_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_0.setText("")
        self.btn_wordle_0_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_0.setText("")
        self.btn_wordle_1_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_4.setText("")
        self.btn_wordle_2_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_2_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_4.setText("")
        self.btn_wordle_1_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_1_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_1.setText("")
        self.btn_wordle_5_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_4.setText("")
        self.btn_wordle_3_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_2.setText("")
        self.btn_wordle_3_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_4.setText("")
        self.btn_wordle_0_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_3.setText("")
        self.btn_wordle_3_3.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_3.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_4.setText("")
        self.btn_wordle_5_4.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_5_4.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_1.setText("")
        self.btn_wordle_0_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_2.setText("")
        self.btn_wordle_0_2.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_0_2.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_1.setText("")
        self.btn_wordle_3_1.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_1.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_0.setText("")
        self.btn_wordle_3_0.setProperty(u"row", QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_wordle_3_0.setProperty(u"col", QCoreApplication.translate("MainWindow", u"0", None))
        self.mainMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Juego", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menuUpdate.setTitle(QCoreApplication.translate("MainWindow", u"Actualizaci\u00f3n", None))
    # retranslateUi

