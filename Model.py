class Model:

    def __init__(self, offen, korrekt, falsch, gesamt, spiele):
        self.game_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.offen = offen
        self.korrekt = korrekt
        self.falsch = falsch
        self.gesamt = gesamt
        self.spiele = spiele

    def set_offen(self, offen):
        self.offen = offen

    def get_offen(self) -> int:
        return self.offen

    def set_korrekt(self, korrekt):
        self.korrekt = korrekt

    def get_korrekt(self) -> int:
        return self.korrekt

    def set_falsch(self, falsch):
        self.falsch = falsch

    def get_falsch(self) -> int:
        return self.falsch

    def set_gesamt(self, gesamt):
        self.gesamt = gesamt

    def get_gesamt(self) -> int:
        return self.gesamt

    def set_spiele(self, spiele):
        self.spiele = spiele

    def get_spiele(self) -> int:
        return self.spiele

    def get_game_numbers(self) -> list:
        return self.game_numbers

    def set_game_numbers(self, game_numbers):
        self.game_numbers = game_numbers
