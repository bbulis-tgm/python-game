from PyQt5 import QtWidgets, uic
import sys
from Model import Model
import random


class Controller(QtWidgets.QWidget):

    counter = 0

    def __init__(self):
        self.counter = 0
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
        self.form.pushButton_new.clicked.connect(self.new_game)
        self.print_random_numbers()



    def print_random_numbers(self):
        game_list = self.model.get_game_numbers()
        random.shuffle(game_list)

        for button in self.button_list:
            index = self.button_list.index(button)
            number = game_list[index]
            button.setText(str(number))
            button.clicked.connect(lambda checked, nr=number: self.button_click_event(nr))

    def button_click_event(self, nr):
        if nr == self.counter:
            self.counter += 1

        else:
            self.model.set_falsch(self.model.get_falsch() + 1)

    def repaint_ui(self):
        self.form.label_offen_punkte.setText(str(self.model.get_offen()))
        self.form.label_koorekt_punkte.setText(str(self.model.get_korrekt()))
        self.form.label_falsch_punkte.setText(str(self.model.get_falsch()))
        self.form.label_gesamt_punkte.setText(str(self.model.get_gesamt()))
        self.form.label_spiele_punkte.setText(str(self.model.get_spiele()))

    def new_game(self):
        self.counter = 0
        self.model.set_spiele(self.model.get_spiele() + 1)
        self.form.label_spiele_punkte.setText(str(self.model.get_spiele()))
        self.print_random_numbers()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    app.exec()
