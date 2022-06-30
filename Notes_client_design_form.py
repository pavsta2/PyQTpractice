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
        MainWindow.resize(719, 733)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_get_all_notes = QPushButton(self.centralwidget)
        self.pushButton_get_all_notes.setObjectName(u"pushButton_get_all_notes")

        self.horizontalLayout.addWidget(self.pushButton_get_all_notes)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

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

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_title = QLineEdit(self.centralwidget)
        self.lineEdit_title.setObjectName(u"lineEdit_title")

        self.horizontalLayout_3.addWidget(self.lineEdit_title)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit_massage = QLineEdit(self.centralwidget)
        self.lineEdit_massage.setObjectName(u"lineEdit_massage")

        self.horizontalLayout_4.addWidget(self.lineEdit_massage)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox_importance = QComboBox(self.centralwidget)
        self.comboBox_importance.setObjectName(u"comboBox_importance")

        self.horizontalLayout_5.addWidget(self.comboBox_importance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.comboBox_condition = QComboBox(self.centralwidget)
        self.comboBox_condition.setObjectName(u"comboBox_condition")

        self.horizontalLayout_6.addWidget(self.comboBox_condition)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.pushButton_login = QPushButton(self.centralwidget)
        self.pushButton_login.setObjectName(u"pushButton_login")

        self.horizontalLayout_8.addWidget(self.pushButton_login)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 21))
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
        self.label_window_input.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\"title\":", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\"message\":", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\"importance\":", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\"condition\":", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043f\u0443\u0431\u043b\u0438\u0430\u0446\u0438\u0438 \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0443\u0439\u0442\u0435\u0441\u044c:", None))
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
    # retranslateUi

