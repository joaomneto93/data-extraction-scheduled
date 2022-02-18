from src.view.screen import menu
from src.business.auth import auth
from src.helpers.menu_flow import menu_chosen
from src.helpers.messages import Messages as Msg


def fake_input_right(the_prompt):
    __user_email__ = 'test@test.com'
    prompt_to_return_val = {
        Msg.PUT_OPTION: '1',
        str(Msg.PUT_USER): __user_email__
    }
    val = prompt_to_return_val[the_prompt]
    return val


def test_menu_flow_wrong(mocker):
    mocker.patch('builtins.input', side_effect=['something_wrong', '3'])
    response = menu()
    assert response == "NOK"


def test_menu_flow_1(monkeypatch):
    __user_password__ = 'Str0nGP#$$'
    monkeypatch.setattr('builtins.input', fake_input_right)
    monkeypatch.setattr('getpass.getpass', lambda x: __user_password__)
    response = menu()
    assert response == "OK"



def test_menu_flow_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2")
    response = menu()
    assert response == "OK"


def test_menu_flow_3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3")
    response = menu()
    assert response == "OK"


def test_auth():
    response = auth(True)
    assert response == "OK"


def test_menu_chosen():
    for i in range(2,4):
        response = menu_chosen(str(i))
        assert response == "OK"
