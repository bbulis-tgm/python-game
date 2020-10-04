from PyQt5 import QtWidgets, uic
import sys
from Model import Model


class Controller(QtWidgets.QWidget):
    def __init__(self):
        super(Controller, self).__init__()
        self.form = uic.loadUi('gui.ui', self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    app.exec()
