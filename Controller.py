from PyQt5 import QtWidgets, uic
import sys
from Model import Model
import random


class Controller(QtWidgets.QWidget):
    counter = 0

    def __init__(self):
        """
        Methode setzte das button Array zu anfangs
        """
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
        self.new_game()

    def print_random_numbers(self):
        """
        Methode gibt 15 zufällig angeordnete Zahlen an die Buttons aus
        """
        game_list = self.model.get_game_numbers()
        random.shuffle(game_list)

        for button in self.button_list:
            index = self.button_list.index(button)
            number = game_list[index]
            button.setEnabled(True)
            button.setText(str(number))
            button.disconnect()
            button.clicked.connect(lambda checked, nr=number, btn=button: self.button_click_event(nr, btn))

    def button_click_event(self, nr, btn):
        """
        Methode empfängt die Signale wenn ein Button geklickt wird
        """
        if nr == self.counter:
            self.counter += 1
            self.richtig(btn)
            print(self.counter)
            if self.counter == 15:
                self.model.set_spiele(self.model.get_spiele() + 1)
                self.form.label_spiele_punkte.setText(str(self.model.get_spiele()))
                self.new_game()
        else:
            self.falsch()

    def repaint_ui(self):
        """
        Methode setzte alle Labels in der UI neu
        """
        self.form.label_offen_punkte.setText(str(self.model.get_offen()))
        self.form.label_koorekt_punkte.setText(str(self.model.get_korrekt()))
        self.form.label_falsch_punkte.setText(str(self.model.get_falsch()))
        self.form.label_gesamt_punkte.setText(str(self.model.get_gesamt()))
        self.form.label_spiele_punkte.setText(str(self.model.get_spiele()))

    def new_game(self):
        """
        Method wird ausgeführt wenn der User gewinnt oder auf Neues Spiel klickt
        """
        self.counter = 0
        self.model.set_offen(15)
        self.print_random_numbers()
        self.repaint_ui()

    def richtig(self, btn):
        """
        Methode wird ausgeführt wenn die Eingabe richtig war
        """
        btn.setEnabled(False)
        self.model.set_offen(self.model.get_offen() - 1)
        self.model.set_korrekt(self.model.get_korrekt() + 1)
        self.model.set_gesamt(self.model.get_falsch() + self.model.get_korrekt())
        self.repaint_ui()

    def falsch(self):
        """
        Methode wird ausgeführt wenn die Eingabe falsche war
        """
        self.model.set_falsch(self.model.get_falsch() + 1)
        self.model.set_gesamt(self.model.get_falsch() + self.model.get_korrekt())
        self.repaint_ui()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    app.exec()
