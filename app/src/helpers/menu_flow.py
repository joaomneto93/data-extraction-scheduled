from src.helpers.messages import Messages as Msg
from src.business.auth import auth
from src.business.get_content import get_content
import time


def exit_option(message: str) -> None:
    print(message)
    time.sleep(1.5)
    return


def menu_chosen(user_option: str) -> str:
    response = "NOK"
    if user_option.__eq__("1"):
        authenticated = auth(False)
        if not authenticated:
            return response
        response = get_content(authenticated)

    if user_option.__eq__("2"):
        exit_option(str(Msg.EXITING))
        response = "OK"

    return response
