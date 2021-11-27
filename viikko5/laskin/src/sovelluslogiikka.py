class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.tuloslista = [0]

    def tallenna_tulos(self):
        self.tuloslista.append(self.tulos)
        print('tuloslista nyt', self.tuloslista, ' ja sen pituus', len(self.tuloslista))

class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.tulos += self.syote()
        self.sovelluslogiikka.tallenna_tulos()


class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.tulos -= self.syote()
        self.sovelluslogiikka.tallenna_tulos()

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.tulos = 0
        self.sovelluslogiikka.tallenna_tulos()

class Kumoa:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        print(self.sovelluslogiikka.tulos)
        self.sovelluslogiikka.tulos = self.sovelluslogiikka.tuloslista[-2]
        self.sovelluslogiikka.tuloslista.pop()
        print('popin jälkeen', self.sovelluslogiikka.tulos)