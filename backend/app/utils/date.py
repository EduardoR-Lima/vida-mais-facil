from datetime import date

def weekday_from_date(date_: date):
    """
    Retorna um inteiro represetando o dia da semana de acordo com o
    padrão seguido pelo banco de dados
    """
    # no banco de dados os dias são indexados a partir de 1
    return date_.weekday() + 1
