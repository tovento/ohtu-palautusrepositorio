from kivi_paperi_sakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, *args):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto
