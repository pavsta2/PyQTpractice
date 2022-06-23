# from My_form import Ui_Form
# from PySide2 import QtWidgets, QtCore, QtGui
#
#
# class MyForm(QtWidgets.QWidget):
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#
#         self.ui.pushButton.clicked.connect(self.setPosition)
#         self.ui.pushButton_2.clicked.connect(self.setPosition)
#         self.ui.pushButton_3.clicked.connect(self.setPosition)
#         self.ui.pushButton_4.clicked.connect(self.setPosition)
#         self.ui.pushButton_5.clicked.connect(self.setPosition)
#
#         self.ui.comboBox.addItems(["HEX", "DEC", "OCT", "BIN"])
#
#
#
#     def setPosition(self):
#
#         buttonText = self.sender().text()
#         screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
#         screenHeigth = QtWidgets.QApplication.screenAt(self.pos()).size().height()
#
#         position = {
#             "Лево/Верх":(0,0),
#             "Лево/Низ": (0, screenHeigth - self.height() - 100),
#             "Центр": (screenWidth / 2 - self.width() / 2, screenHeigth / 2 - self.height() / 2),
#             "Право/Верх": (screenWidth - self.width(), 0),
#             "Право/Низ": (screenWidth - self.width(), screenHeigth - self.height() - 100)}
#
#         self.move(position.get(buttonText)[0], position.get(buttonText)[1])
#
#     def getScreenParam(self):
#         pass
#
#     def changeLCDdigits(self):
#         x = {
#             "HEX": self.ui.lcdNumber.setHexMode,
#             "DEC": self.ui.lcdNumber.setDecMode,
#             "OCT": self.ui.lcdNumber.setOctMode,
#             "BIN": self.ui.lcdNumber.setBinMode,
#         }
#
#         x[self.ui.comboBox.currentText()]()
#
#     def changeEvent(self, event: QtCore.QEvent) -> None:
#         # print(event.type())
#         if event.type() == QtCore.QEvent.Type.WindowStateChange:
#             if self.isMinimized():
#                 print("Окно свернуто")
#
#     def moveEvent(self, event: QtGui.QMoveEvent) -> None:
#         print(self.pos())
#
#     def event(self, event: QtCore.QEvent) -> bool:
#         if event.type() == QtCore.QEvent.Resize:
#             print(self.size())
#
#         return QtWidgets.QWidget.event(self, event)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication()
#
#     myapp = MyForm()
#     myapp.show()
#
#     app.exec_()
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSettings
import My_form
import time


class MyForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.ui = My_form.Ui_Form()
        self.ui.setupUi(self)

        self.ui.comboBox.addItems(["HEX", "DEC", "OCT", "BIN"])
        self.ui.pushButton_6.setShortcut("F1")

        self.ui.pushButton.clicked.connect(self.changePosition)
        self.ui.pushButton_2.clicked.connect(self.changePosition)
        self.ui.pushButton_3.clicked.connect(self.changePosition)
        self.ui.pushButton_4.clicked.connect(self.changePosition)
        self.ui.pushButton_5.clicked.connect(self.changePosition)
        self.ui.pushButton_6.clicked.connect(self.screeninfo)
        self.ui.dial.valueChanged.connect(self.lcd)
        self.ui.horizontalSlider.valueChanged.connect(self.lcd)
        self.ui.comboBox.currentIndexChanged.connect(self.lsd_view)

        self.ui.dial.installEventFilter(self)

        self.set = QSettings("test", "My_form_back", self)
        self.loadsettings()

    def loadsettings(self):
        self.ui.lcdNumber.display(self.set.value("lcd_value"))
        # self.ui.comboBox.setCurrentIndex(self.set.value("lcd_mode", "HEX"))

    def savesettings(self):
        self.set.setValue("lcd_value", self.ui.lcdNumber.value())
        self.set.setValue("lcd_mode", self.ui.lcdNumber.mode())


    def changePosition(self):
        buttonText = self.sender().text()
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()

        position = {
            "Лево/Верх": (0, 0),
            "Право/Верх": (screenWidth - self.width(), 0),
            "Центр": (screenWidth / 2 - self.width() / 2, screenHeight / 2 - self.height() / 2 - 100),
            "Лево/Низ": (0, screenHeight - self.height() - 140),
            "Право/Низ": (screenWidth - self.width(), screenHeight - self.height() - 140)

        }

        self.move(position[buttonText][0], position[buttonText][1])

    def screeninfo(self):
        screens_num = QtWidgets.QApplication.screens()
        log = self.ui.plainTextEdit.appendPlainText

        log(time.ctime())
        log("__" * 10)
        log(f"Кол-во экранов:{len(screens_num)}")
        log(f"Основной окно: {QtWidgets.QApplication.primaryScreen().name()}")
        for screen in screens_num:
            log(f"Разрешение экрана '{screen.name()}' составляет: {screen.size().width()} на {screen.size().height()}")
        log(f"Окно находится на экране {QtWidgets.QApplication.screenAt(self.pos()).name()}")
        log(f"Размеры окна: ширина - {self.size().width()}, высота - {self.size().height()}")
        log(f"Минимальные размеры окна: {self.minimumWidth()} на {self.minimumHeight()}")
        log(f"Текущее положение окна: x {self.pos().x()}, y {self.pos().y()}")
        log(f"Координаты центра приложения: X = {self.pos().x() + self.width() / 2}, Y = {self.pos().y() + self.height() / 2}")
        log("__" * 10)
        log("__" * 10)

    def lcd(self):
        if self.sender().objectName() == "dial":
            value = self.ui.dial.value()
            self.ui.horizontalSlider.setValue(value)
        if self.sender().objectName() == "horizontalSlider":
            value = self.ui.horizontalSlider.value()
            self.ui.horizontalSlider.setValue(value)

        self.ui.lcdNumber.display(value)

    def lsd_view(self):
        if self.ui.comboBox.currentText() == "HEX":
            self.ui.lcdNumber.setHexMode()
            print(self.ui.lcdNumber.mode())

        if self.ui.comboBox.currentText() == "DEC":
            self.ui.lcdNumber.setDecMode()
            print(self.ui.lcdNumber.mode())
        if self.ui.comboBox.currentText() == "OCT":
            self.ui.lcdNumber.setOctMode()
            print(self.ui.lcdNumber.mode())
        if self.ui.comboBox.currentText() == "BIN":
            self.ui.lcdNumber.setBinMode()
            print(self.ui.lcdNumber.mode())





    def changeEvent(self, event: QtCore.QEvent) -> None:
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                self.ui.plainTextEdit.appendPlainText(time.ctime() + "window is minimized")
            if self.isMaximized():
                self.ui.plainTextEdit.appendPlainText(time.ctime() + "window is maximized")
        if event.type() == QtCore.QEvent.ActivationChange:
            self.ui.plainTextEdit.appendPlainText(time.ctime() + "window is activated")

        return QtWidgets.QWidget.changeEvent(self, event)

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(time.ctime() + "window is show")

        return QtWidgets.QWidget.showEvent(self, event)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(f"Координаты окна x: {self.pos().x()}, y:{self.pos().y()}")

        return QtWidgets.QWidget.moveEvent(self, event)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(f"Размеры окна - высота: {self.size().height()}, ширина:{self.size().width()}")

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(f"{event.key()} is pressed")

        return QtWidgets.QWidget.keyPressEvent(self, event)

    # def event(self, event: QtCore.QEvent) -> bool:
    #     if event.type() == QtCore.QEvent.KeyPress:
    #         self.ui.plainTextEdit.appendPlainText(f"{event.key()} is pressed")

        # return QtWidgets.QWidget.event(self, event)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.ui.dial and event.type() == QtCore.QEvent.KeyPress:
            if event.text() == "+":
                self.ui.dial.setValue(self.ui.dial.value()+1)
            elif event.text() == "-":
                self.ui.dial.setValue(self.ui.dial.value()-1)

            self.ui.plainTextEdit.appendPlainText("dial pressed")

        return super(MyForm, self).eventFilter(watched, event)

    def closeEvent(self, event):
        self.savesettings()



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyForm()
    myapp.show()

    app.exec_()
