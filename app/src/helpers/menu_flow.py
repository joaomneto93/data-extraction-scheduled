from src.business.auth import auth
import sys
import time

def exit_option(message: str) -> None:
    print(message)
    time.sleep(1.5)
    return


def menu_choosed(user_option: str) -> str:
    response = "NOK"
    if user_option.__eq__("1"):
        response = auth(False)

    if user_option.__eq__("2"):
        exit_option("\nFunção ainda será implementada!")

    if user_option.__eq__("3"):
        exit_option("\nSaindo do programa....")

    return response