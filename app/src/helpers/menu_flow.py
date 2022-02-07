from src.business.auth import auth


def menu_choosed(user_option: str) -> None:
    if user_option.__eq__("1"):
        auth()
    else:
        print("Opção não implementada")