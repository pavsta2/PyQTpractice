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

        self.initUi()

    def initUi(self):
        self.ui.pushButtonTimerStart.clicked.connect(self.timerStart)
        self.timerThread.timerSignal.connect(self.updateLineEditTimeLeft, QtCore.Qt.AutoConnection)
        self.timerThread.finished.connect(self.timerFinished)

        self.ui.pushButtonUrlCheckStart.clicked.connect(self.updateUrlCheck)
        self.urlChacker.urlSignal.connect(self.updateUrlCheckSignal)

        self.SMonitor.sysSignal.connect(self.updatySysMonitor)
        self.ui.spinBoxSystemInfoDelay.valueChanged.connect(self.setSystemInfoDelay)


    def initThreads(self):
        self.timerThread = TimerThread()
        self.urlChacker = UrlThread()
        self.SMonitor = SystemMonitor()
        self.SMonitor.start()


    def timerStart(self):
        if self.ui.pushButtonTimerStart.isChecked():
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

    def updateUrlCheck(self):
        # try:
        #     self.urlChacker.setUrl(self.ui.lineEditURL)
        #     self.timerThread.start()
        # except ValueError:
        #     QtWidgets.QMessageBox.warning(self, "ошибка", "неверное значение")

        if self.ui.pushButtonUrlCheckStart.isChecked():
            self.urlChacker.setUrl(self.ui.lineEditURL.text())
            self.urlChacker.setDelay(self.ui.spinBoxUrlCheckTime.value())
            self.urlChacker.start()
            self.ui.pushButtonUrlCheckStart.setText("Стоп")
        else:
            self.ui.pushButtonUrlCheckStart.setText("Начать проверку")
            self.ui.pushButtonUrlCheckStart.setChecked(False)
            self.urlChacker.status = False

    def updateUrlCheckSignal(self, emit_value):

        self.ui.plainTextEditUrlCheckLog.appendPlainText(f"{time.ctime()} - Статус {emit_value}")

    def updatySysMonitor(self, emit_list) -> None:
        self.ui.progressBarCPU.setValue(emit_list[0])
        self.ui.labelCPUPercent.setText(f"{emit_list[0]} %")
        self.ui.progressBarRAM.setValue(emit_list[1])
        self.ui.labelRAMPercent.setText(f"{emit_list[1]} %")

    def setSystemInfoDelay(self):
        self.SMonitor.setMonitorDelay(self.ui.spinBoxSystemInfoDelay.value())


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

class SystemMonitor(QtCore.QThread):
    sysSignal = QtCore.Signal(list)

    def setMonitorDelay(self, mon_delay):
        self.__mon_delay = mon_delay

    def run(self):
        # if self.__mon_delay is None:
        SystemMonitor.setMonitorDelay(self, 1)

        while True:
            ram = psutil.virtual_memory()
            ram_bisy = int(ram.used * 100 / ram.total)
            cpu_value = psutil.cpu_percent()
            self.sysSignal.emit([cpu_value, ram_bisy])
            time.sleep(self.__mon_delay)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = P3_Form()
    myapp.show()

    app.exec_()
