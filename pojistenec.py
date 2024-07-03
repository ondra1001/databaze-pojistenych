class Pojistenec:
    # třída vytváří pojištěnce
    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._vek = vek
        self._tel_cislo = tel_cislo


    def vrat_hodnoty_pro_databazi(self):
        # Metoda vrací hodnoty pro vložení pojištěného do databáze.
        return (self._jmeno, self._prijmeni, self._vek, self._tel_cislo)

class TovarnaNaPojistence:
    # Třída na vytvoření objektu Pojistenec.
    def vytvor_pojistence(self, manager_vstupu):
        # Metoda vrátí instanci uživatele, atribut je třída ManagerVstupu.

        # Získání a validace vstupů od uživatele.
        jmeno = manager_vstupu.vrat_jmeno()
        prijmeni = manager_vstupu.vrat_prijmeni()
        vek = manager_vstupu.vrat_vek()
        tel_cislo = manager_vstupu.vrat_tel_cislo()

        # Vytvoření uživatele za pomoci vstupů
        return Pojistenec(jmeno, prijmeni, vek, tel_cislo)
