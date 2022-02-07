import os
import time
from src.helpers.menu_flow import menu_choosed

def clearConsole() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def menu_screen() -> None:
    print(" ----------------MENU----------------")
    print("|   Escolha uma das opções abaixo    |")
    print("| 1 - Baixar por uma URL             |")
    print("| 2 - Baixar por uma lista de URL's  |")
    print("| 3 - Sair                           |")
    print(" ------------------------------------")
    get_option()


def check_option(user_option: str) -> bool:
    options_to_validate = any([
        user_option.__eq__("1"),
        user_option.__eq__("2"),
        user_option.__eq__("3")
    ])
    
    return options_to_validate


def get_option() -> None:
    user_option = input('Insira sua opção: ')

    if check_option(user_option):
        print(f"Opção escolhida {user_option}")
        menu_choosed(user_option)
    else:
        print("Você deve inserir 1,2 ou 3!")
        time.sleep(2.5)
        menu()


def menu():
    clearConsole()
    menu_screen()
