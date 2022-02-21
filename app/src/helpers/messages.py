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

    # Fields to make HTTP Request
    SITE_URL_LOGIN = 'https://fornecedor.extrafarma.com.br/Account/Login'
    SITE_URL_RELATORIO = 'https://fornecedor.extrafarma.com.br/SolicitaRelatorio/'

    TEXT_FIELD_ID_USER = 'txtEmail'
    TEXT_FIELD_ID_PASS = 'txtSenha'
    
    FIELD_NAME_LOCALS = 'idCentroDistribuicao'
    FIELD_NAME_SUPPLIER = 'idFornecedor'
    FIELD_NAME_SUB_DIVISION = 'idSubDivisao'

    
    BUTTON_ID_LOGIN = 'btnLogar'
    BUTTON_ID_GERA_RELAT = 'GerarRelatorio'

    def __str__(self):
        return '%s' % self.value