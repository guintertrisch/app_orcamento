from app import db, ma


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    atendimentos = db.relationship('Atendimentos', backref='clientes', lazy=True)

class Atendimentos(db.Model):
    __tablename__ = 'atendimentos'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(300), nullable=False)
    data_atendimento = db.Column(db.Date, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'),
                           nullable=False)


class ClienteSchema(ma.ModelSchema):
    class Meta:
        model = Cliente



