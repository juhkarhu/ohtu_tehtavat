import heapq

KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        
        self.kapasiteetti = kapasiteetti

        if kapasiteetti is None or kapasiteetti < 0:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti
        
        if kasvatuskoko is None or kasvatuskoko < 0:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        #self.lukujono = heapq.heapify([])
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.lukujono:
            return True
        return False

    def muuta_alkioiden_maaraa(self, maara):
        self.alkioiden_lkm += maara

    def lisaa(self, lisattava):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = lisattava
            self.muuta_alkioiden_maaraa(1)

        if not self.kuuluu(lisattava):
            self.lukujono[self.alkioiden_lkm] = lisattava
            self.muuta_alkioiden_maaraa(1)
            print(self.alkioiden_lkm % len(self.lukujono), self.alkioiden_lkm, len(self.lukujono))
            if self.alkioiden_lkm == len(self.lukujono):
                self.kopioi_taulukko(self.lukujono)


    def poista(self, poistettava):
        kohta = -1

        for i in range(0, self.alkioiden_lkm):
            if poistettava == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                self.lukujono[j], self.lukujono[j+1] = self.lukujono[j+1], self.lukujono[j]

            self.muuta_alkioiden_maaraa(-1)


    def kopioi_taulukko(self, alkup_taulukko):
        self.kasvata_taulukon_kokoa()
        for i in range(0, len(alkup_taulukko)):
            self.lukujono[i] = alkup_taulukko[i]

    def kasvata_taulukon_kokoa(self):
        self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
