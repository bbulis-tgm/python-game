from PyQt5 import QtWidgets, uic
import sys
from Model import Model
import random


class Controller(QtWidgets.QWidget):

    def __init__(self):
        super(Controller, self).__init__()
        self.form = uic.loadUi('gui.ui', self)
        self.model = Model(15, 0, 0, 0, 0)
        self.button_list = [self.form.pushButton_0, self.form.pushButton_1,
                           self.form.pushButton_2, self.form.pushButton_3,
                           self.form.pushButton_4, self.form.pushButton_5,
                           self.form.pushButton_6, self.form.pushButton_7,
                           self.form.pushButton_8, self.form.pushButton_9,
                           self.form.pushButton_10, self.form.pushButton_11,
                           self.form.pushButton_12, self.form.pushButton_13,
                           self.form.pushButton_14]
        self.start_game()

    def start_game(self):
        game_list = self.model.get_game_numbers()
        random.shuffle(game_list)

        for button in self.button_list:
            index = self.button_list.index(button)
            number = game_list[index]
            button.setText(str(number))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    app.exec()
