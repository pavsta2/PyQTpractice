from PySide2 import QtWidgets, QtCore
import time


# import requests
# import psutil


class MyApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initUi()

    def initUi(self):
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите колво сек")

        self.pbStart = QtWidgets.QPushButton()
        self.pbStart.setText("Старт")

        self.pbStop = QtWidgets.QPushButton()
        self.pbStop.setText("Стоп")

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.lineEdit)
        main_layout.addWidget(self.pbStart)
        main_layout.addWidget(self.pbStop)

        self.pbStop.setEnabled(False)

        self.setLayout(main_layout)

        self.pbStart.clicked.connect(self.onPBStart)
        self.pbStop.clicked.connect(self.onPBStopClicked)

    def initThreads(self):
        self.timerThread = TimerThread()

        self.timerThread.started.connect(self.timerThreadStarted)
        self.timerThread.finished.connect(self.timerThreadFinish)

        self.timerThread.timerSignal.connect(self.timerSignalEmit)

    def onPBStart(self):
        try:
            # self.timerThread.status = True
            self.timerThread.timeCount = int(self.lineEdit.text())
            self.timerThread.start()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "ошибка", "неверное значение")

    def onPBStopClicked(self):
        self.timerThread.status = False

    def timerThreadStarted(self):
        self.pbStart.setEnabled(False)
        self.pbStop.setEnabled(True)
        self.lineEdit.setEnabled(False)

    def timerThreadFinish(self):
        self.pbStart.setEnabled(True)
        self.pbStop.setEnabled(False)
        self.lineEdit.setEnabled(True)

        self.lineEdit.setText("")

    def timerSignalEmit(self, emit_value):
        self.lineEdit.setText(emit_value)


class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(TimerThread, self).__init__(parent)

        self.timeCount = None

        self.status = True

    def run(self):
        self.status = True

        while self.status:
            time.sleep(1)
            self.timeCount -= 1
            self.timerSignal.emit(str(self.timeCount))

        # for i in range(self.timeCount,0,-1):
        #     # print(i)
        #     self.timerSignal.emit(str(i))
        #     time.sleep(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyApp()
    myapp.show()

    app.exec_()
