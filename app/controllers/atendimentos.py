import datetime
from datetime import datetime, timedelta

from sqlalchemy import desc

from app.models.cliente import Cliente, Atendimentos, db


def retorna_atendimentos_seis_meses():
    periodo = datetime.now() - timedelta(days=180)
    cliente = db.session.query(Cliente, Atendimentos).filter(Cliente.id == Atendimentos.cliente_id).filter(
        Atendimentos.data_atendimento.between(periodo, datetime.now().date())).order_by(
        desc(Atendimentos.data_atendimento))

    return cliente


def retorna_atendimentos_dose_meses():
    periodo = datetime.now() - timedelta(days=365)
    cliente = db.session.query(Cliente, Atendimentos).filter(Cliente.id == Atendimentos.cliente_id).filter(
        Atendimentos.data_atendimento.between(periodo, datetime.now().date())).order_by(
        desc(Atendimentos.data_atendimento))
    return cliente


def retorna_filtro_periodo(form):
    if form.nome.data:
        cliente = db.session.query(Cliente, Atendimentos) \
            .filter(Cliente.id == Atendimentos.cliente_id).filter(
            Cliente.nome.ilike('%' + form.nome.data + '%')).filter(
            Atendimentos.data_atendimento.between(datetime.strptime(form.data_inicio.data, '%d/%m/%Y').date(),
                                                  datetime.strptime(form.data_fim.data, '%d/%m/%Y').date())).order_by(
            desc(Atendimentos.data_atendimento))
    else:
        cliente = db.session.query(Cliente, Atendimentos).filter(Cliente.id == Atendimentos.cliente_id).filter(
            Atendimentos.data_atendimento.between(datetime.strptime(form.data_inicio.data, '%d/%m/%Y').date(),
                                                  datetime.strptime(form.data_fim.data, '%d/%m/%Y').date())).order_by(
            desc(Atendimentos.data_atendimento))
    return cliente
