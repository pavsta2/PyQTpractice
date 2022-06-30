from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSettings
import requests
from requests.auth import HTTPBasicAuth

import time

from Notes_client_design_form import Ui_MainWindow as Form


class Note_Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Note_Form, self).__init__(parent)
        self.ui = Form()
        self.ui.setupUi(self)

        self.initUi()

    def initUi(self):
        # сигналы
        self.ui.pushButton_get_all_notes.clicked.connect(self.getNoteList)

        self.ui.pushButton.clicked.connect(self.postNote)

    # слоты
    def getNoteList(self):
        response = requests.get("http://127.0.0.1:8000/notes/")
        output = response.text
        self.ui.textBrowser_window_output.setText(output)

    def postNote(self):
        username = 'admin'
        password = 'admin'
        auth = HTTPBasicAuth(username, password)

        # data = {
        #
        #     "title": "3000",
        #     "message": "fdgsdgsg",
        #     "importance": True,
        #     "condition": 1,
        #     "date_and_time": "2022-06-03T19:28:00",
        #     "author": "admin"
        #      }

        data = self.ui.textEdit_window_input.toPlainText()
        response = requests.post("http://127.0.0.1:8000/notes/", auth=auth, json=data)
        self.ui.textBrowser_window_output.setText(str(response.status_code))
        print(self.ui.textEdit_window_input.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Note_Form()
    myapp.show()

    app.exec_()
