from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def create_driver_connection() -> webdriver:
    return webdriver.Chrome(ChromeDriverManager().install())


def get_selet_field(item):
    return "//select[@name='" + str(item) + "']"
