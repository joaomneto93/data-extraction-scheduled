import time


def check_cookie(browser):
    time.sleep(5)
    cookies = browser.get_cookies()
    if cookies:
        return True
    else:
        return False
