from app import db, ma
from datetime import date
from app.models.tables import ClienteSchema, Cliente
from app.models.orcamento_detalhe import OrcamentoDetalheSchema
from marshmallow import fields



class Orcamento(db.Model):
    __tablename__ = 'orcamentos'
    id = db.Column(db.Integer, primary_key=True)
    data_atual = db.Column(db.Date, nullable=False)
    data_agendamento = db.Column(db.Date, nullable=False)
    data_conclusao = db.Column(db.Date)
    data_cancelamento = db.Column(db.Date)
    descricao = db.Column(db.String(200), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    orcamentoDetalhe = db.relationship('OrcamentoDetalhe',backref='OrcamentoDetalhe')
    cliente = db.relationship('Cliente', backref='orcamento')
    observacao = db.Column(db.String(4000), nullable=True)


    def __init__(self,data_agendamento, descricao, cliente_id, observacao = None):
        self.data_atual = date.today()
        self.data_agendamento = data_agendamento
        self.descricao = descricao
        self.cliente_id = cliente_id
        self.observacao = observacao


class OrcamentoSchema(ma.ModelSchema):
    orcamentoDetalhe = ma.Nested(OrcamentoDetalheSchema, many=True)
    cliente = ma.Nested(ClienteSchema)
    class Meta:
        model = Orcamento



