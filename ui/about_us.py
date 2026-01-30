# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_us.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QSizePolicy, QWidget)
import resources_rc

class Ui_AboutUs(object):
    def setupUi(self, AboutUs):
        if not AboutUs.objectName():
            AboutUs.setObjectName(u"AboutUs")
        AboutUs.setEnabled(True)
        AboutUs.resize(400, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutUs.sizePolicy().hasHeightForWidth())
        AboutUs.setSizePolicy(sizePolicy)
        AboutUs.setMinimumSize(QSize(400, 550))
        AboutUs.setMaximumSize(QSize(400, 550))
        icon = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.HelpAbout):
            icon = QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout)
        else:
            icon.addFile(u":/logo/icon_128.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        AboutUs.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(AboutUs)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(300, 510, 86, 26))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)
        self.label_name = QLabel(AboutUs)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(20, 9, 157, 26))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_name.setFont(font)
        self.horizontalLayoutWidget = QWidget(AboutUs)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 170, 91, 22))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_version = QLabel(self.horizontalLayoutWidget)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMinimumSize(QSize(0, 20))
        self.label_version.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.label_version)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayoutWidget_2 = QWidget(AboutUs)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 230, 351, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_author = QLabel(self.horizontalLayoutWidget_2)
        self.label_author.setObjectName(u"label_author")
        self.label_author.setMinimumSize(QSize(0, 20))
        self.label_author.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_2.addWidget(self.label_author)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayoutWidget_3 = QWidget(AboutUs)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 200, 150, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 20))
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_3.setStretch(1, 1)
        self.label_8 = QLabel(AboutUs)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 260, 341, 61))
        self.label_8.setTextFormat(Qt.TextFormat.PlainText)
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(AboutUs)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 330, 91, 18))
        self.label_9.setFont(font1)
        self.label_11 = QLabel(AboutUs)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 380, 101, 18))
        self.label_11.setFont(font1)
        self.label_12 = QLabel(AboutUs)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 400, 221, 16))
        self.label_12.setOpenExternalLinks(True)
        self.label_13 = QLabel(AboutUs)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 470, 341, 18))
        self.label_14 = QLabel(AboutUs)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 50, 121, 101))
        self.label_14.setPixmap(QPixmap(u":/logo/icon_128.png"))
        self.horizontalLayoutWidget_4 = QWidget(AboutUs)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 350, 231, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.label_15 = QLabel(self.horizontalLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_15)

        self.label_3 = QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_16 = QLabel(self.horizontalLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_16)

        self.label_5 = QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(4, 1)

        self.retranslateUi(AboutUs)
        self.buttonBox.rejected.connect(AboutUs.close)

        QMetaObject.connectSlotsByName(AboutUs)
    # setupUi

    def retranslateUi(self, AboutUs):
        AboutUs.setWindowTitle(QCoreApplication.translate("AboutUs", u"Acerca de", None))
        self.label_name.setText(QCoreApplication.translate("AboutUs", u"PyClassicGames", None))
        self.label_2.setText(QCoreApplication.translate("AboutUs", u"Versi\u00f3n: ", None))
        self.label_version.setText(QCoreApplication.translate("AboutUs", u"0.0", None))
        self.label_4.setText(QCoreApplication.translate("AboutUs", u"Desarrollado por: ", None))
        self.label_author.setText(QCoreApplication.translate("AboutUs", u"Sergio Trujillo de la Nuez", None))
        self.label_6.setText(QCoreApplication.translate("AboutUs", u"Licencia: ", None))
        self.label_7.setText(QCoreApplication.translate("AboutUs", u"MIT License", None))
        self.label_8.setText(QCoreApplication.translate("AboutUs", u"Aplicaci\u00f3n de escritorio que integra juegos cl\u00e1sicos de estrategia y l\u00f3gica, desarrollada como Ejercicio Final para la asignatura de Desarrollo de Interfaces. ", None))
        self.label_9.setText(QCoreApplication.translate("AboutUs", u"T\u00e9cnologias:", None))
        self.label_11.setText(QCoreApplication.translate("AboutUs", u"Repositorio:", None))
        self.label_12.setText(QCoreApplication.translate("AboutUs", u"<html><head/><body><p><a href=\"https://github.com/TRuHa83/PyClassicGames\"><span style=\" text-decoration: underline; color:#0000ff;\">Ver proyecto en GitHub</span></a></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("AboutUs", u"Copyright \u00a9 2026. Todos los derechos reservados.", None))
        self.label_14.setText("")
        self.label_10.setText(QCoreApplication.translate("AboutUs", u"Python 3.10+", None))
        self.label_15.setText(QCoreApplication.translate("AboutUs", u"\u00b7", None))
        self.label_3.setText(QCoreApplication.translate("AboutUs", u"PySide6", None))
        self.label_16.setText(QCoreApplication.translate("AboutUs", u"\u00b7", None))
        self.label_5.setText(QCoreApplication.translate("AboutUs", u"SQLite", None))
    # retranslateUi

