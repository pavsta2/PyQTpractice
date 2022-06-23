from PySide2 import QtWidgets
import requests
import psutil


class MyApp(QtWidgets.Qwidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.lineEdit = Q