import datetime
from datetime import datetime, timedelta

from app.models.cliente import Cliente


def retorna_atendimentos():
    periodo = datetime.now() - timedelta(days=180)
    cliente = Cliente.query.filter(Cliente.data_atendimento.between(periodo, datetime.now().date()))
    return cliente


def retorna_atendimentos_dose_meses():
    periodo = datetime.now() - timedelta(days=365)
    cliente = Cliente.query.filter(Cliente.data_atendimento.between(periodo, datetime.now().date()))
    return cliente
