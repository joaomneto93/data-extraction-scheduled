from src.helpers.messages import Messages as Msg
from src.business.auth import auth
import time

def exit_option(message: str) -> None:
    print(message)
    time.sleep(1.5)
    return


def menu_chosen(user_option: str) -> str:
    response = "NOK"
    if user_option.__eq__("1"):
        response = auth(False)

    if user_option.__eq__("2"):
        exit_option(str(Msg.NOT_IMPLEMETED))
        response = "OK"

    if user_option.__eq__("3"):
        exit_option(str(Msg.EXITING))
        response = "OK"

    return response