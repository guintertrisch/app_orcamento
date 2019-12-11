from app import db, ma
from marshmallow import fields


class OrcamentoDetalhe(db.Model):
    __tablename__ = 'orcamento_detalhes'
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    #valor = db.Column(db.Float(5,2), nullable=False)
    valor = db.Column(db.String, nullable=False)
    acao = db.Column(db.String(60), nullable=False)
    produto_servico = db.Column(db.String(15), nullable=False)
    orcamento_id = db.Column(db.Integer, db.ForeignKey('orcamentos.id'), nullable=False)

    def __init__(self,quantidade,produto_servico, acao,valor,orcamento_id):
        self.quantidade = quantidade
        self.produto_servico = produto_servico
        self.acao = acao
        self.valor = valor
        self.orcamento_id = orcamento_id


class OrcamentoDetalheSchema(ma.ModelSchema):
    class Meta:
        model = OrcamentoDetalhe