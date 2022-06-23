from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSettings
import psutil
import requests
from ui import p3_form_design
import time


class P3_Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(P3_Form, self).__init__(parent)
        self.ui = p3_form_design.Ui_Form()
        self.ui.setupUi(self)

        self.initThreads()
        self.ui.pushButtonTimerStart.clicked.connect(self.timerStart)




    def initThreads(self):
        self.timerThread = TimerThread()

        self.timerThread.timerSignal.connect(self.updateLineEditTimeLeft, QtCore.Qt.AutoConnection)
        self.timerThread.finished.connect(self.timerFinished)

        self.urlChacker = UrlThread()

        self.urlChacker.urlSignal.connect(self.updateUrlCheck)




    def timerStart(self):
        if self.ui.pushButtonTimerStart.isChecked():
            self.ui.lineEditTimerEnd.setText(str(self.ui.spinBoxTimerCount.value()))
            self.timerThread.timeCount = self.ui.spinBoxTimerCount.value()
            self.timerThread.start()
            self.ui.pushButtonTimerStart.setText("Стоп")
        else:
            self.timerFinished()

    def timerFinished(self):
        self.ui.pushButtonTimerStart.setText("Начать отсчет")
        self.ui.pushButtonTimerStart.setChecked(False)
        self.timerThread.status = False

    def updateLineEditTimeLeft(self, emit_value):
        self.ui.lineEditTimerEnd.setText(emit_value)

    def updateUrlCheck(self, emit_value):
        self.ui.plainTextEditUrlCheckLog.appendPlainText(f"{time.ctime()} - Статус {emit_value}")






class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(TimerThread, self).__init__(parent)

        self.timeCount = None

        self.status = True

    def run(self):
        while self.status:
            time.sleep(1)
            self.timeCount -= 1
            self.timerSignal.emit(str(self.timeCount))


class UrlThread(QtCore.QThread):
    urlSignal = QtCore.Signal(int)

    def setUrl(self, url):
        self.__url = url

    def setDelay(self, delay):
        self.__delay = delay

    def run(self):
        self.status = True

        while self.status:
            responce = requests.get(self.__url)
            self.urlSignal.emit(responce.status_code)
            time.sleep(self.__delay)





if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = P3_Form()
    myapp.show()

    app.exec_()