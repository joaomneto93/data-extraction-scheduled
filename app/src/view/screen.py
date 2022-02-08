import os
import time
from types import resolve_bases
from src.helpers.menu_flow import menu_choosed

def clearConsole() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def menu_screen() -> str:
    response = ""
    print(" ----------------MENU----------------")
    print("|   Escolha uma das opções abaixo    |")
    print("| 1 - Baixar por uma URL             |")
    print("| 2 - Baixar por uma lista de URL's  |")
    print("| 3 - Sair                           |")
    print(" ------------------------------------")
    response = get_option()
    return response


def check_option(user_option: str) -> bool:
    options_to_validate = any([
        user_option.__eq__("1"),
        user_option.__eq__("2"),
        user_option.__eq__("3")
    ])
    
    return options_to_validate


def get_option() -> str:
    response = ""
    user_option = input('Insira sua opção: ')

    if check_option(user_option):
        print(f"\nOpção escolhida: {user_option}")
        response = menu_choosed(user_option)
    else:
        print("\nVocê deve inserir 1,2 ou 3!")
        time.sleep(2.5)
        menu()
    return response


def menu() -> str:
    response = ""
    clearConsole()
    response = menu_screen()
    return response
