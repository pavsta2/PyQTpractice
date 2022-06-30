# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Notes_client_design_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(625, 516)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_get_all_notes = QPushButton(self.centralwidget)
        self.pushButton_get_all_notes.setObjectName(u"pushButton_get_all_notes")

        self.horizontalLayout.addWidget(self.pushButton_get_all_notes)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labe_window_output = QLabel(self.centralwidget)
        self.labe_window_output.setObjectName(u"labe_window_output")

        self.verticalLayout.addWidget(self.labe_window_output)

        self.textBrowser_window_output = QTextBrowser(self.centralwidget)
        self.textBrowser_window_output.setObjectName(u"textBrowser_window_output")

        self.verticalLayout.addWidget(self.textBrowser_window_output)

        self.label_window_input = QLabel(self.centralwidget)
        self.label_window_input.setObjectName(u"label_window_input")

        self.verticalLayout.addWidget(self.label_window_input)

        self.textEdit_window_input = QTextEdit(self.centralwidget)
        self.textEdit_window_input.setObjectName(u"textEdit_window_input")

        self.verticalLayout.addWidget(self.textEdit_window_input)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 625, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_get_all_notes.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c", None))
        self.labe_window_output.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043d\u043e \u0432\u044b\u0432\u043e\u0434\u0430", None))
        self.label_window_input.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043d\u043e \u0432\u0432\u043e\u0434\u0430", None))
    # retranslateUi

