from src.business.auth import auth
from src.business.manager import set_connection_properties


def handler():
    driver_authenticated = auth()

    if driver_authenticated is None:
        return None

    set_connection_properties(driver_authenticated)

    return True
