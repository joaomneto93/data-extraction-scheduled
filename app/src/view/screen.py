from src.helpers.menu_flow import get_option
from src.helpers.utils import clear_console


def menu_screen():
    print(" ----------------MENU----------------")
    print("|   Escolha uma das opções abaixo    |")
    print("| 1 - Baixar relatório               |")
    print("| 2 - Sair                           |")
    print(" ------------------------------------")


def menu() -> bool:
    response = None
    retry = True

    clear_console()
    menu_screen()

    while retry:
        response = get_option()
        if response or response is None:
            retry = False
    return response
