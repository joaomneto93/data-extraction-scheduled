from src.view.screen import menu
from src.helpers.messages import Messages as Msg


def main():
    response = menu()
    if response:
        print(Msg.SUCCESS_MSG)
    else:
        print(Msg.FAILED_MSG)


main()
