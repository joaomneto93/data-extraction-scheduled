#import schedule
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.helpers.messages import Messages as Msg

import base64
import getpass


# id dos items a serem buscados
__ID_USER = Msg.TEXT_FIELD_ID_USER
__ID_PASS = Msg.TEXT_FIELD_ID_PASS
__ID_LOGIN = Msg.BUTTON_ID_LOGIN

# Usuário e Senha para autenticação
__EMAIL = b'dGVzdGVAY2hhdHViYS5jb20='
__PASS  = b'Y2hhdHViYWRlbWVzcXVpdGE='

def put_login(is_default = True) -> dict:
    login = {}

    if is_default:
        login["user"] = __EMAIL
        login["pass"] = __PASS
    else:
        login["user"] = base64.b64encode(
            bytes(str(input(str(Msg.PUT_USER))), "utf-8"))

        login["pass"] = base64.b64encode(
            bytes(str(getpass.getpass(str(Msg.PUT_PASS))), "utf-8"))
        

    return login


def auth(is_default: bool) -> webdriver:
    login = {}
    login = put_login(is_default)
    username = login["user"]
    password = login["pass"]
    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(str(Msg.SITE_URL_LOGIN))
    
    browser.find_element_by_id(__ID_USER).send_keys(
        base64.b64decode(username).decode("utf-8", "ignore"))
    browser.find_element_by_id(__ID_PASS).send_keys(
        base64.b64decode(password).decode("utf-8", "ignore"))

    # ONLY FOR TEST
    # browser.find_element_by_id(__ID_USER).send_keys('USUARIO')
    # browser.find_element_by_id(__ID_PASS).send_keys('SENHA')

    browser.find_element_by_id(__ID_LOGIN ).click()
    time.sleep(3.5)

    if browser:
        return browser

    return False