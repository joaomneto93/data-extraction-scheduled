#import schedule
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import base64
import getpass

# URL do site a ser autenticado
__SITE_URL = "https://fornecedor.extrafarma.com.br/Account/Login?SourceURL=https://fornecedor.extrafarma.com.br/"

# id dos items a serem buscados
__ID_USER = "txtEmail"
__ID_PASS = "txtSenha"
__ID_LOGIN = "btnLogar"

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
            bytes(str(input("Insira seu usuário: ")), "utf-8"))
        login["pass"] = base64.b64encode(
            bytes(str(getpass.getpass("Insira sua senha: ")), "utf-8"))
        

    return login


def auth():

    login = {}
    login = put_login(False)
    username = login["user"]
    password = login["pass"]
    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(__SITE_URL)

    browser.find_element_by_id(__ID_USER).send_keys(
        base64.b64decode(username).decode("utf-8", "ignore"))
    browser.find_element_by_id(__ID_PASS).send_keys(
        base64.b64decode(password).decode("utf-8", "ignore"))
    
    browser.find_element_by_id(__ID_LOGIN ).click()
    # browser.save_screenshot('auth_screen.png')
    time.sleep(2.5)