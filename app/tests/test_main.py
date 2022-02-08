from src.view.screen import menu
from src.business.auth import auth
from src.helpers.menu_flow import menu_choosed
from app.main import handler
import io

def test_menu():
    response = handler()
    assert response == "OK"

def test_auth():
    response = auth(True)
    assert response == "OK"

def test_menu_choosed():
    for i in range(2,4):
        response = menu_choosed(str(i))
        assert response == "NOK"