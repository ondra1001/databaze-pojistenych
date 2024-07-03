class ManagerVstupu:

    @classmethod
    def zvaliduj_jmeno(cls, zadani):
        # validace vstupu jména nebo příjmení
        jmeno = None
        while jmeno is None or not jmeno.isalpha():
            jmeno = input(zadani).capitalize()

        return jmeno

    @classmethod
    def zvaliduj_tel_cislo(cls):
        # validace telefonního čísla
        tel_cislo = None
        while tel_cislo is None or not tel_cislo.isdigit():
            tel_cislo = input("Zadejte své telefonní číslo: ")
    
        return tel_cislo

    @classmethod
    def zvaliduj_vek(cls):
        # validace věku
        vek = None
        while vek is None or not vek.isdigit():
            vek = input("Zadej svůj věk: ")
    
        return vek

    def vrat_jmeno(self):
        # metoda vrací zvalidované jméno ve formě string

        zadani = "Zadejte Křestní jméno: "
        jmeno = self.zvaliduj_jmeno(zadani)
        return jmeno

    def vrat_prijmeni(self):
        # metoda vrací zvalidované příjmení ve formě string

        zadani = "Zadejte příjmení: "
        prijmeni = self.zvaliduj_jmeno(zadani)
        return prijmeni

    def vrat_vek(self):
        # metoda vrací zvalidovaný věk ve formě string

        vek = self.zvaliduj_vek()
        return vek

    def vrat_tel_cislo(self):
        # metoda vrací zvalidované telefonní číslo ve formě string

        tel_cislo = self.zvaliduj_tel_cislo()
        return tel_cislo
