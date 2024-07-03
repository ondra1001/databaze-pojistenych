import sys
import os


def program(manager_vstupu, manager_pojistenych, tovarna_na_pojistence):
        '''Funkce obsahuje celou logiku aplikace, vytvoření databáze, výběr akce a vykonání akce,
        jako parametry se zadávaji objekty tříd: ManagerVstupu, ManagerPojistenych, TovarnaNaPojistence'''

        print(f"""
{20 * "_"}
Evidence pojištěných
{20 * "_"}
            
Vyberte si akci:
            
1 - Pridat noveho pojisteneho
2 - Vypsat vsechny pojistene
3 - Vyhledat pojisteneho
4 - Konec\n""")

        volba = input("Výběr: ")
        while volba not in ["1", "2", "3", "4"]:
            print("Tato volba není v možnostech")
            volba = input("Výběr: ")

        match volba:
            case "1":
                pojistenec = tovarna_na_pojistence.vytvor_pojistence(manager_vstupu)
                manager_pojistenych.uloz_pojisteneho(pojistenec.vrat_hodnoty_pro_databazi())
            case "2":
                pojistenci = manager_pojistenych.vrat_vsechny_pojistene()
                for pojistenec in pojistenci:
                    jmeno, prijmeni, vek, telefon = pojistenec
                    print(f"Jméno a příjmení: {jmeno} {prijmeni} Věk: {vek} let Tel. číslo: {telefon}")
            case "3":
                hledany_pojistenec = manager_pojistenych.vyhledej_pojisteneho(manager_vstupu)
                for pojistenec in hledany_pojistenec:
                    jmeno, prijmeni, vek, telefon = pojistenec
                    print(f"Jméno a příjmení: {jmeno} {prijmeni} Věk: {vek} let Tel. číslo: {telefon}")
            case "4":
                sys.exit()
        pokracovat = input("Pro pokračování zmáčkněte enter.")
        os.system('cls')
        while pokracovat == "":
            program(manager_vstupu, manager_pojistenych, tovarna_na_pojistence)

