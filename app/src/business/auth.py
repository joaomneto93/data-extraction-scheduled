import base64
import getpass

from src.helpers.messages import Messages as Msg
from src.helpers.browser_helper import create_driver_connection
from src.connection.session import check_cookie


# id dos items a serem buscados
__ID_USER = Msg.TEXT_FIELD_ID_USER
__ID_PASS = Msg.TEXT_FIELD_ID_PASS
__ID_LOGIN = Msg.BUTTON_ID_LOGIN

# Usuário e Senha para autenticação
__EMAIL = b'dGVzdGVAY2hhdHViYS5jb20='
__PASS = b'Y2hhdHViYWRlbWVzcXVpdGE='


def put_login() -> dict:
    return {
        'user': base64.b64encode(
            bytes(str(input(str(Msg.PUT_USER))), "utf-8")),
        'pass': base64.b64encode(
            bytes(str(getpass.getpass(str(Msg.PUT_PASS))), "utf-8"))
    }


def auth():
    login = put_login()
    username = login["user"]
    password = login["pass"]
    
    browser = create_driver_connection()
    browser.get(str(Msg.SITE_URL_LOGIN))

    browser.find_element_by_id(__ID_USER).send_keys(
        base64.b64decode(username).decode("utf-8", "ignore"))
    browser.find_element_by_id(__ID_PASS).send_keys(
        base64.b64decode(password).decode("utf-8", "ignore"))

    # ONLY FOR TEST
    # browser.find_element_by_id(__ID_USER).send_keys('USUARIO')
    # browser.find_element_by_id(__ID_PASS).send_keys('SENHA')
    browser.find_element_by_id(__ID_LOGIN).click()

    if check_cookie(browser):
        return browser
    else:
        return None
