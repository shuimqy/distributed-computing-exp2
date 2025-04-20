# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(519, 443)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 501, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_Button = QPushButton(self.verticalLayoutWidget)
        self.main_Button.setObjectName(u"main_Button")

        self.horizontalLayout.addWidget(self.main_Button)

        self.Book_Button = QPushButton(self.verticalLayoutWidget)
        self.Book_Button.setObjectName(u"Book_Button")

        self.horizontalLayout.addWidget(self.Book_Button)

        self.IDQuery_Button = QPushButton(self.verticalLayoutWidget)
        self.IDQuery_Button.setObjectName(u"IDQuery_Button")

        self.horizontalLayout.addWidget(self.IDQuery_Button)

        self.NameQuery_Button = QPushButton(self.verticalLayoutWidget)
        self.NameQuery_Button.setObjectName(u"NameQuery_Button")

        self.horizontalLayout.addWidget(self.NameQuery_Button)

        self.cancel_button = QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_Button.setText(QCoreApplication.translate("Form", u"\u4e3b\u754c\u9762", None))
        self.Book_Button.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u9884\u7ea6", None))
        self.IDQuery_Button.setText(QCoreApplication.translate("Form", u"ID\u67e5\u8be2", None))
        self.NameQuery_Button.setText(QCoreApplication.translate("Form", u"\u60a3\u8005\u67e5\u8be2", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88\u9884\u7ea6", None))
    # retranslateUi

