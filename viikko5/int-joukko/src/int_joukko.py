KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti:
            if type(kapasiteetti) == int and kapasiteetti >= 0:
                self.kapasiteetti = kapasiteetti
            else:
                raise Exception(
                    "Kapasiteetin tulee olla positiivinen kokonaisluku")
        else:
            self.kapasiteetti = KAPASITEETTI

        if kasvatuskoko:
            if type(kasvatuskoko) == int and kasvatuskoko >= 0:
                self.kasvatuskoko = kasvatuskoko
            else:
                raise Exception(
                    "Kasvatuskoon tulee olla positiivinen kokonaisluku")
        else:
            self.kasvatuskoko = OLETUSKASVATUS

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        if luku in self.lukujono:
            return True
        return False

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        self.lukujono[self.alkioiden_lkm] = luku
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        if self.alkioiden_lkm == len(self.lukujono):
            self.luo_suurempi_lista()

        return True

    def luo_suurempi_lista(self):
        taulukko_old = self.lukujono.copy()
        self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.lukujono)


    def poista(self, luku):
        if not self.kuuluu(luku):
            return False

        self.lukujono.remove(luku)
        self.lukujono.append(0)

        self.alkioiden_lkm -= 1

        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdistejoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            yhdistejoukko.lisaa(luku)
        for luku in b_taulu:
            yhdistejoukko.lisaa(luku)

        return yhdistejoukko

    @staticmethod
    def leikkaus(a, b):
        leikkausjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku in b_taulu:
                leikkausjoukko.lisaa(luku)

        return leikkausjoukko

    @staticmethod
    def erotus(a, b):
        erotusjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku not in b_taulu:
                erotusjoukko.lisaa(luku)

        return erotusjoukko

    def __str__(self):
        teksti = ", ".join(map(str, self.lukujono[:self.alkioiden_lkm]))
        return f"{{{teksti}}}"
