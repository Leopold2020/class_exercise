

class Fordon:
    def __init__(self, namn: str, ljud: str, färg: str, ålder: int):
        self.namn = namn
        self.ljud = ljud
        self.färg = färg
        self.ålder = ålder

        def låta(self):
            for _ in range(3):
                print(self.ljud)

        def ändra_färg(self, ny_färg: str):
            self.färg = ny_färg


class Bil(Fordon):
    def __init__(self, namn: str, ljud: str, färg: str, ålder: int, \
        bränsle: str, hästkraft: int, besiktigad: bool, utsläpp: int):
        super().__init__(namn, ljud, färg, ålder)
        self.bränsle = bränsle
        self.hästkraft = hästkraft
        self.besiktigad = besiktigad
        self.utsläpp = utsläpp

    def tanka(self, mängd: int):
        pass

    def kör(self, sträcka) -> float:
        return self.utsläpp*sträcka