from enum import Enum

class Messages(Enum):
    PUT_USER = 'Insira seu usuário: '
    PUT_PASS = 'Insira sua senha: '
    PUT_OPTION = 'Insira sua opção: '
    OPTION_WARNING = '\nVocê deve inserir 1,2 ou 3!'
    NOT_IMPLEMETED = '\nFunção ainda será implementada!'
    EXITING = '\nSaindo do programa....'
    SUCCESS_MSG = 'Programa executado com sucesso!'
    FAILED_MSG = 'Programa executado com falha!'

    def __str__(self):
        return '%s' % self.value