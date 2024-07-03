from program import program
from manager_vstupu import ManagerVstupu
from manager_pojistencu import ManagerPojistencu
from pojistenec import TovarnaNaPojistence

tovarna_na_pojistence = TovarnaNaPojistence()
manager_pojistenych = ManagerPojistencu("databaze_pojistencu.db")
manager_vstupu = ManagerVstupu()
def main():
    # Hlavní funkce, která spustí program.
    program(manager_vstupu, manager_pojistenych, tovarna_na_pojistence)

main()

