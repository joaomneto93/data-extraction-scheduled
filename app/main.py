import schedule
import time
import requests

urladress = input('Enter url adress:\n')


class Extract:
    """Classe utilizada para extração de dados provenientes de determinada url\n\nParâmetros:\nurl: url do site desejado"""

    def __init__(self, url):
        self.url = url
        pass


print('Este algoritmo fará a extração automática de dados')
