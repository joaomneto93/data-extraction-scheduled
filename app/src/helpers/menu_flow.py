import time
from src.helpers.messages import Messages as Msg
from src.helpers.utils import exit_option
from src.connection.handler import handler
from src.helpers.check_input import check_menu_input


def menu_chosen(user_option: str) -> bool:
    response = False
    if user_option.__eq__("1"):
        response = handler()

    if user_option.__eq__("2"):
        exit_option(str(Msg.EXITING))
        response = True

    return response


def get_option() -> bool:
    response = False
    user_option = input(Msg.PUT_OPTION)

    if check_menu_input(user_option):
        print(f"\nOpção escolhida: {user_option}\n")
        response = menu_chosen(user_option)
    else:
        print(Msg.OPTION_WARNING)
        time.sleep(1.0)
    return response
