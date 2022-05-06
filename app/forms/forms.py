from flask_wtf import Form
from wtforms import StringField


class CadastroForm(Form):
    nome = StringField()
    telefone = StringField()
    data_atendimento = StringField()


class PesquisaForm(Form):
    nome = StringField()
    data_atendimento = StringField()
    data_inicio = StringField()
    data_fim = StringField()
