from PyQt5 import QtWidgets, uic
import sys


class Game(QtWidgets.QWidget):
    def __init__(self):
        super(Game, self).__init__()
        self.form = uic.loadUi('gui.ui', self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Game()
    window.show()
    app.exec()
