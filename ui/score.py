# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'score.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHeaderView,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_Score(object):
    def setupUi(self, Score):
        if not Score.objectName():
            Score.setObjectName(u"Score")
        Score.resize(468, 623)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Score.sizePolicy().hasHeightForWidth())
        Score.setSizePolicy(sizePolicy)
        Score.setMinimumSize(QSize(468, 623))
        Score.setMaximumSize(QSize(468, 623))
        icon = QIcon()
        icon.addFile(u":/logo/icon_128.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Score.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Score)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Score)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout = QGridLayout(self.tab_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 10, 0, 10)
        self.score_mines = QTableWidget(self.tab_1)
        if (self.score_mines.columnCount() < 2):
            self.score_mines.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.score_mines.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.score_mines.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.score_mines.setObjectName(u"score_mines")

        self.gridLayout.addWidget(self.score_mines, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 10, 0, 10)
        self.score_horse = QTableWidget(self.tab_3)
        if (self.score_horse.columnCount() < 2):
            self.score_horse.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.score_horse.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.score_horse.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.score_horse.setObjectName(u"score_horse")

        self.gridLayout_3.addWidget(self.score_horse, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 10, 0, 10)
        self.score_wordle = QTableWidget(self.tab_2)
        if (self.score_wordle.columnCount() < 2):
            self.score_wordle.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.score_wordle.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.score_wordle.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.score_wordle.setObjectName(u"score_wordle")

        self.gridLayout_2.addWidget(self.score_wordle, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.btn_export = QPushButton(Score)
        self.btn_export.setObjectName(u"btn_export")

        self.verticalLayout.addWidget(self.btn_export)

        self.btn_close = QPushButton(Score)
        self.btn_close.setObjectName(u"btn_close")

        self.verticalLayout.addWidget(self.btn_close)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Score)
        self.btn_close.clicked.connect(Score.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Score)
    # setupUi

    def retranslateUi(self, Score):
        Score.setWindowTitle(QCoreApplication.translate("Score", u"Puntuaci\u00f3n", None))
        ___qtablewidgetitem = self.score_mines.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Score", u"Fecha y hora", None));
        ___qtablewidgetitem1 = self.score_mines.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Score", u"Puntuaci\u00f3n", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Score", u"Buscaminas", None))
        ___qtablewidgetitem2 = self.score_horse.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Score", u"Fecha y hora", None));
        ___qtablewidgetitem3 = self.score_horse.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Score", u"Puntuaci\u00f3n", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Score", u"Salto del caballo", None))
        ___qtablewidgetitem4 = self.score_wordle.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Score", u"Fecha y hora", None));
        ___qtablewidgetitem5 = self.score_wordle.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Score", u"Puntuaci\u00f3n", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Score", u"Wordle", None))
        self.btn_export.setText(QCoreApplication.translate("Score", u"Exportar", None))
        self.btn_close.setText(QCoreApplication.translate("Score", u"Cerrar", None))
    # retranslateUi

