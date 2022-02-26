import time
import os


def exit_option(message: str) -> None:
    print(message)
    time.sleep(1.5)
    return


def clear_console() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
