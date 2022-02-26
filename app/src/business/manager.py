import time
from selenium.webdriver.support.ui import Select
from src.helpers.browser_helper import get_selet_field
from src.helpers.messages import Messages as Msg


def set_connection_properties(driver_authenticated):
    driver_authenticated.get(str(Msg.SITE_URL_RELATORIO))

    field_selected = get_selet_field(Msg.FIELD_NAME_LOCALS)
    select = Select(driver_authenticated.find_element_by_xpath(field_selected))
    time.sleep(1.5)
    select.select_by_value('10020')

    field_selected = get_selet_field(Msg.FIELD_NAME_PROVIDER)
    select = Select(driver_authenticated.find_element_by_xpath(field_selected))
    time.sleep(1.5)
    select.select_by_value('104574')

    time.sleep(1.5)
    return True
