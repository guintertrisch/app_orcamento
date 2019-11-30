from app import db, ma

class Produto(db.Model):
    __tablename__="produtos"
    id = db.Column(db.Integer, primary_key=True)
    nome= db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self,nome):
        self.nome = nome