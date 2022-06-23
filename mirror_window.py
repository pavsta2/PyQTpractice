from mirror_design import Ui_Form
from PySide2 import QtWidgets


class MirrorWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MirrorWindow()
    myapp.show()

    app.exec_()
