from PyQt5 import QtWidgets, uic
import sys
from Model import Model
import random


class Controller(QtWidgets.QWidget):
    def __init__(self):
        super(Controller, self).__init__()
        self.form = uic.loadUi('gui.ui', self)
        self.model = Model(15, 0, 0, 0, 0)

    def start_game(self):
        game_list = self.model.get_game_numbers()
        random.shuffle(game_list)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    app.exec()
