from src.helpers.messages import Messages as Msg
from src.business.content.values import get_locals, \
    get_provider, get_subsection, get_month


def check_generic_input(message, items: dict) -> str:
    retry = True
    while retry:
        chosen_local = str(input(str(message))).upper()

        for item in items:
            if item == chosen_local:
                return chosen_local


def check_menu_input(user_option: str) -> bool:
    options_to_validate = any([
        user_option.__eq__("1"),
        user_option.__eq__("2")
    ])

    return options_to_validate


class CheckInput:

    def __init__(self):
        self.local = get_locals()
        self.provider = get_provider()
        self.subsection = get_subsection()
        self.month = get_month()

    def local_data(self) -> str:
        message = Msg.INSERT_LOCAL
        return check_generic_input(message, self.local)

    def provider_data(self) -> str:
        message = Msg.INSERT_PROVIDER
        return check_generic_input(message, self.provider)

    def subsection_data(self) -> str:
        message = Msg.INSERT_SUBSECTION
        return check_generic_input(message, self.subsection)

    def month_data(self, cont) -> str:
        message = Msg.INSERT_MONTH % str(cont)
        return check_generic_input(message, self.month)
