from app import db


class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    contato = db.Column(db.String)
    local = db.Column(db.String)
    data = db.Column(db.String)
    descricao = db.Column(db.String)
    orcamento = db.relationship('Orcamento',backref='cliente')


    def __init__(self,nome, contato,local,data,descricao):
        self.nome = nome
        self.contato = contato
        self.local = local
        self.data = data
        self.descricao = descricao


    def __repr__(self):
        return "<Nome %r>" % self.nome


class Orcamento(db.Model):
    __tablename__ = "orcamentos"
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.String)
    produto = db.Column(db.String)
    detalhe = db.Column(db.String)
    acao = db.Column(db.String)
    valor = db.Column(db.String)
    observacao = db.Column(db.String, nullable=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'),nullable=False)

    def __init__(self,quantidade, produto,detalhe,acao,valor,observacao,cliente_id):
        self.quantidade = quantidade
        self.produto = produto
        self.detalhe = detalhe
        self.acao = acao
        self.valor = valor
        self.observacao = observacao
        self.cliente_id = cliente_id

    def __repr__(self):
        return "<Nome %r>" % self.nome