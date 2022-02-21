from src.view.screen import menu
from src.helpers.messages import Messages as Msg


def process():
    return menu()


def main():
    response = process()
    if response.__eq__('OK'):
        print(Msg.SUCCESS_MSG)
    else:
        print(Msg.FAILED_MSG)


main()
