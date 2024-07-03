import sqlite3
class ManagerPojistencu:

    def __init__(self, databaze):
        self.databaze = databaze
        self._vytvor_tabulku()

    def vytvor_spojeni_db(self):
        return sqlite3.connect(self.databaze)


    def _vytvor_tabulku(self):
        sql_vytvor_tabulku = """
        CREATE TABLE IF NOT EXISTS pojistenci(
            jmeno TEXT,
            prijmeni TEXT,
            vek TEXT,
            telefon TEXT);
            """
        with self.vytvor_spojeni_db() as spojeni:
            spojeni.cursor().execute(sql_vytvor_tabulku)

    def uloz_pojisteneho(self, pojisteny):
        sql_vloz_pojisteneho = """
        INSERT INTO pojistenci(jmeno, prijmeni, vek, telefon)
        VALUES (?, ?, ?, ?);"""

        with self.vytvor_spojeni_db() as spojeni:
            spojeni.cursor().execute(sql_vloz_pojisteneho, pojisteny)
            spojeni.commit()

    def vyhledej_pojisteneho(self, manager_vstupu):
        jmeno = manager_vstupu.vrat_jmeno()
        prijmeni = manager_vstupu.vrat_prijmeni()
        sql_vyber_pojisteneho = """
        SELECT * FROM pojistenci WHERE jmeno = ? AND prijmeni = ?;"""

        with self.vytvor_spojeni_db() as spojeni:
            cursor = spojeni.cursor()
            cursor.execute(sql_vyber_pojisteneho, (jmeno, prijmeni))
            return cursor.fetchall()

    def vrat_vsechny_pojistene(self):
        sql_vyber_vsechny = """
        SELECT * FROM pojistenci"""

        with self.vytvor_spojeni_db() as spojeni:
            cursor = spojeni.cursor()
            cursor.execute(sql_vyber_vsechny)
            return cursor.fetchall()


    def vymaz_pojisteneho(self, manager_vstupu):
        sql_vymaz_pojistence = """
        DELETE * FROM pojisteni WHERE name = ? AND prijmeni = ?;"""

        jmeno = manager_vstupu.vrat_jmeno()
        prijmeni = manager_vstupu.vrat_prijmeni()

        with self.vytvor_spojeni_db() as spojeni:
            cursor = spojeni.cursor()
            cursor.execute(sql_vymaz_pojistence, (jmeno, prijmeni))




