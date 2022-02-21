from time import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from src.business.request_itens.http_itens import get_selet_field
from src.helpers.messages import Messages as Msg

import time


def get_content(driver: webdriver):
    driver.get(str(Msg.SITE_URL_RELATORIO))
    field_selected = get_selet_field(Msg.FIELD_NAME_LOCAIS)
    select = Select(driver.find_element_by_xpath(field_selected))
    time.sleep(0.8)
    select.select_by_value('10020')

    field_selected = get_selet_field(Msg.FIELD_NAME_FORNECEDOR)
    select = Select(driver.find_element_by_xpath(field_selected))
    time.sleep(0.8)
    select.select_by_value('104574')

    time.sleep(10)
    return "OK"
