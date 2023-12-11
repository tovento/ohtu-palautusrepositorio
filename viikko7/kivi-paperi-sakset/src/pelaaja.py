class Pelaaja:
    def __init__(self):
        self.pisteet = 0

    def lisaa_piste(self):
        self.pisteet += 1

    def __str__(self):
        return f"{self.pisteet}"
