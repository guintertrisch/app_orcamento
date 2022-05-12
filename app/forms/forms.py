from flask_wtf import Form
from wtforms import StringField, TextAreaField


class CadastroForm(Form):
    nome = StringField()
    telefone = StringField()
    data_atendimento = StringField()
    descricao = TextAreaField()


class PesquisaForm(Form):
    nome = StringField()
    data_inicio = StringField()
    data_fim = StringField()
