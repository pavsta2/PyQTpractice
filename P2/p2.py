from PySide2 import QtWidgets, QtCore, QtGui


class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.lineEditSource = QtWidgets.QLineEdit()
        self.lineEditSource.setPlaceholderText("Insert text")

        self.lineEditResult = QtWidgets.QLineEdit()
        self.lineEditResult.setPlaceholderText("Result")

        self.pushButtonHandle = QtWidgets.QPushButton("Revert")

        main_layout = QtWidgets.QVBoxLayout()
        lineedit_layout = QtWidgets.QHBoxLayout()

        lineedit_layout.addWidget(self.lineEditSource)
        lineedit_layout.addWidget(self.lineEditResult)

        self.setLayout(main_layout)

        self.pushButtonHandle.clicked.connect(self.pushButtonHandle)

    # def event(self, event: QtCore.QEvent) -> bool:
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyWidgets()
    myapp.show()

    app.exec_()
