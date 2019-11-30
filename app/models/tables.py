from app import db, ma


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    cpfcnpj = db.Column(db.String)
    contatos = db.relationship('Contato',backref='contato')
    enderecos = db.relationship('Endereco',backref='endereco',uselist=False)

    def __init__(self, nome,cpfcnpj=None):
        self.nome = nome
        self.cpfcnpj = cpfcnpj
        
    def __repr__(self):
        return "<Nome %r>" % self.nome

class Endereco(db.Model):
    __tablename__= 'enderecos'
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String)
    bairro = db.Column(db.String)
    cidade = db.Column(db.String)
    numero = db.Column(db.String)
    complemento = db.Column(db.String)
    estado = db.Column(db.String)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    cliente = db.relationship('Cliente')
    #cliente = db.relationship("Cliente", backref=("enderecos"))

    def __init__(self, rua, bairro, cidade, numero, complemento, estado, cliente_id):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.numero = numero
        self.complemento = complemento
        self.estado = estado
        self.cliente_id = cliente_id

class Contato(db.Model):
    __tablename__ = "contatos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    email = db.Column(db.String)
    principal = db.Column(db.Boolean,default=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    cliente = db.relationship('Cliente')
    #cliente = db.relationship("Cliente", backref=("contatos"))

    def __init__(self,nome, telefone,email,principal,cliente_id):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.principal = principal
        self.cliente_id = cliente_id


class Orcamento(db.Model):
    __tablename__ = "orcamentos"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    quantidade = db.Column(db.String)
    produto = db.Column(db.String)
    detalhe = db.Column(db.String)
    acao = db.Column(db.String)
    valor = db.Column(db.String)
    observacao = db.Column(db.String, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    cliente = db.relationship('Cliente')

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

'''class Produto(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)

class Atendimento(db.Model):
    __tablename__ = "atendimentos"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    cliente = db.relationship('Cliente')

class Item(db.Model):
    __tablename__ = "itens"
    id = db.Column(db.Integer,primary_key=True)
    detalhe = db.Column(db.String)
    acao = db.Column(db.String)
    valor = db.Column(db.Float)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    atendimento_id = db.Column(db.Integer, db.ForeignKey('atendimentos.id'), nullable=False)
    cliente = db.relationship('Cliente')
    atendimento = db.relationship('Atendimento')
    produto = db.relationship('Produto')'''


class ContatoSchema(ma.ModelSchema):
    class Meta:
        model = Contato

class EnderecoSchema(ma.ModelSchema):
    class Meta:
        model = Endereco

class ClienteSchema(ma.ModelSchema):
    contatos = ma.Nested(ContatoSchema,many=True)
    enderecos = ma.Nested(EnderecoSchema)

    class Meta:
        model = Cliente
