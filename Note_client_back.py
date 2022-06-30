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

        self.login = None
        self.password = None

        self.initUi()
        self.initWindows()

    def initUi(self):
        self.ui.comboBox_importance.addItems(["False", "True"])
        self.ui.comboBox_condition.addItems(["Активно", "Отложено", "Выполнено"])
        # сигналы
        self.ui.pushButton_get_all_notes.clicked.connect(self.getNoteList)

        self.ui.pushButton.clicked.connect(self.postNote)

        self.ui.pushButton_login.clicked.connect(self.open_child_window)

    def initWindows(self):
        self.child_window = DroppedWindow()
        self.child_window.send_data.connect(self.setLoginPass)

    def open_child_window(self):
        self.child_window.show()

    # слоты
    def getNoteList(self):
        response = requests.get("http://127.0.0.1:8000/notes/")
        output = response.json()
        self.ui.textBrowser_window_output.setText(str(output))

    def postNote(self):
        auth = HTTPBasicAuth(self.login, self.password)

        condition_index = {
            "Активно": 1,
            "Отложено": 2,
            "Выполнено": 3,
        }

        # data = {
        #
        #     "title": "7000",
        #     "message": "fdgsdgsg",
        #     "importance": True,
        #     "condition": 1,
        #     "date_and_time": "2022-06-03T19:28:00",
        #     "author": "admin"
        #      }

        data = {
            "title": self.ui.lineEdit_title.text(),
            "message": self.ui.lineEdit_massage.text(),
            "importance": self.ui.comboBox_importance.currentText(),
            "condition": condition_index[self.ui.comboBox_condition.currentText()],
        }

        response = requests.post("http://127.0.0.1:8000/notes/", auth=auth, json=data)
        self.ui.textBrowser_window_output.setText(str(response.status_code))

    def setLoginPass(self, emit):

        self.login = emit[0]
        self.password = emit[1]

        print(self.login, self.password)


class DroppedWindow(QtWidgets.QWidget):
    send_data = QtCore.Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.setFixedSize(300, 100)

        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setObjectName("Логин")

        self.lineEditPass = QtWidgets.QLineEdit()
        self.lineEditPass.setObjectName("Пароль")

        pb = QtWidgets.QPushButton("LOG IN")
        pb.clicked.connect(self.setSignal)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditLogin)
        layout.addWidget(self.lineEditPass)
        layout.addWidget(pb)

        self.setLayout(layout)

    def setSignal(self):
        self.send_data.emit((self.lineEditLogin.text(), self.lineEditPass.text()))



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Note_Form()
    myapp.show()

    app.exec_()
