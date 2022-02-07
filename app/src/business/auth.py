#import schedule
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# URL do site a ser autenticado
__SITE_URL = "https://fornecedor.extrafarma.com.br/Account/Login?SourceURL=https://fornecedor.extrafarma.com.br/"

# id dos items a serem buscados
__ID_USER = "txtEmail"
__ID_PASS = "txtSenha"
__ID_LOGIN = "btnLogar"

# Usuário e Senha para autenticação
__PASS = "chatubademesquita"
__EMAIL = "teste@chatuba.com"

def put_login(is_default = True) -> dict:
    login = {}

    if is_default:
        login["user"] = __EMAIL
        login["pass"] = __PASS
    else:
        login["user"] = str(input("Insira seu usuário: "))
        login["pass"] = str(input("Insira sua senha: "))

    return login


def auth():

    login = {}
    login = put_login(True)
    username = login["user"]
    password = login["pass"]
    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(__SITE_URL)

    browser.find_element_by_id(__ID_USER).send_keys(username)
    browser.find_element_by_id(__ID_PASS).send_keys(password)
    
    browser.find_element_by_id(__ID_LOGIN ).click()
    # browser.save_screenshot('auth_screen.png')
    time.sleep(2.5)