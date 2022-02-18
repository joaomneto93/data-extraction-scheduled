import os
import time
from types import resolve_bases
from src.helpers.menu_flow import menu_chosen
from src.helpers.messages import Messages as Msg

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
    response = 'NOK'
    user_option = input(Msg.PUT_OPTION)

    if check_option(user_option):
        print(f"\nOpção escolhida: {user_option}\n")
        response = menu_chosen(user_option)
    else:
        print(Msg.OPTION_WARNING)
        time.sleep(2.5)
        menu()
    return response


def menu() -> str:
    response = 'OK'
    clearConsole()
    response = menu_screen()
    return response
