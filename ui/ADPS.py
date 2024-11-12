# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ADPS.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_ADPS(object):
    def setupUi(self, ADPS):
        if not ADPS.objectName():
            ADPS.setObjectName(u"ADPS")
        ADPS.resize(800, 600)
        self.centralwidget = QWidget(ADPS)
        self.centralwidget.setObjectName(u"centralwidget")
        ADPS.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ADPS)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        ADPS.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ADPS)
        self.statusbar.setObjectName(u"statusbar")
        ADPS.setStatusBar(self.statusbar)

        self.retranslateUi(ADPS)

        QMetaObject.connectSlotsByName(ADPS)
    # setupUi

    def retranslateUi(self, ADPS):
        ADPS.setWindowTitle(QCoreApplication.translate("ADPS", u"ADPS", None))
    # retranslateUi

