import datetime
from datetime import datetime, timedelta

from app.models.cliente import Cliente


def retorna_atendimentos_seis_meses():
    periodo = datetime.now() - timedelta(days=180)
    cliente = Cliente.query.filter(Cliente.data_atendimento.between(periodo, datetime.now().date()))
    return cliente


def retorna_atendimentos_dose_meses():
    periodo = datetime.now() - timedelta(days=365)
    cliente = Cliente.query.filter(Cliente.data_atendimento.between(periodo, datetime.now().date()))
    return cliente


def retorna_filtro_periodo(form):
    cliente = Cliente.query.filter(
        Cliente.data_atendimento.between(datetime.strptime(form.data_inicio.data, '%d/%m/%Y').date(),
                                         datetime.strptime(form.data_fim.data, '%d/%m/%Y').date()))
    return cliente
