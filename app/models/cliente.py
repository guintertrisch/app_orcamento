from app import db, ma


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    data_atendimento = db.Column(db.Date, nullable=False)

    def __init__(self, nome, telefone, data_atendimento=None):
        self.nome = nome
        self.telefone = telefone
        self.data_atendimento = data_atendimento

    def __repr__(self):
        return "<Nome %r>" % self.nome


class ClienteSchema(ma.ModelSchema):
    class Meta:
        model = Cliente
