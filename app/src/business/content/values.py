def get_locals() -> dict:
    return {
        'LOJAS': '0',
        'AQUIRAZ': '10020',
        'BENEVIDES': '10030',
        'GUARULHOS': "10050",
        'MARANHAO': "10060"
    }


def get_provider() -> dict:
    return {
        'P&G - 104574': '104574',
        'P&G HEALTH - 104218': '104218',
        'PROCTER E GAMBLE - 100680': '100680',
        'PROCTER E GAMBLE - 100148': '100148',
        'PROCTER E GAMBLE INDUSTRIAL E COMERCIAL LTDA - 100569': '100569',
        'PROCTER E GAMBLE INDUSTRIAL E COMERCIAL LTDA - 101494': '101494'
    }


def get_subsection() -> dict:
    return {
        'FRALDA': '17',
        'PERFUMARIA': '31',
        'PERFUMARIA CX': '55',
    }


def get_month() -> dict:
    return {
        'LOJAS': '0',
        'AQUIRAZ': '10020',
        'BENEVIDES': '10030',
        'GUARULHOS': "10050",
        'MARANHAO': "10060"
    }


def get_state() -> dict:
    return {
        'Acre (AC) ': 'AC',
        'Alagoas (AL) ': 'AL',
        'Amapá (AP) ': 'AP',
        'Amazonas (AM) ': 'AM',
        'Bahia (BA) ': 'BA',
        'Ceará (CE) ': 'CE',
        'Distrito Federal (DF) ': 'DF',
        'Espírito Santo (ES) ': 'ES',
        'Goiás (GO) ': 'GO',
        'Maranhão (MA) ': 'MA',
        'Mato Grosso (MT) ': 'MT',
        'Mato Grosso do Sul (MS) ': 'MS',
        'Minas Gerais (MG) ': 'MG',
        'Pará (PA) ': 'PA',
        'Paraíba (PB) ': 'PB',
        'Paraná (PR) ': 'PR',
        'Pernambuco (PE) ': 'PE',
        'Piauí (PI) ': 'PI',
        'Rio de Janeiro (RJ) ': 'RJ',
        'Rio Grande do Norte (RN) ': 'RN',
        'Rio Grande do Sul (RS) ': 'RS',
        'Rondônia (RO) ': 'RO',
        'Roraima (RR) ': 'RR',
        'Santa Catarina (SC) ': 'SC',
        'São Paulo (SP) ': 'SP',
        'Sergipe (SE) ': 'SE',
        'Tocantins (TO)': 'TO'
    }


def get_status() -> dict:
    return {
        'Ativo': 'A',
        'Descontinuado': 'C',
        'Todos': 'A,C'
    }
