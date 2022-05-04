from flask_wtf import Form
from wtforms import StringField, DateField


class CadastroForm(Form):
    nome = StringField()
    telefone = StringField()
    data_atendimento = StringField()
