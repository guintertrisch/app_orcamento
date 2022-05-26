from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class CadastroForm(Form):
    nome = StringField(validators=[DataRequired()])
    telefone = StringField(validators=[DataRequired()])
    data_atendimento = StringField(validators=[DataRequired()])
    descricao = TextAreaField(validators=[DataRequired()])


class PesquisaForm(Form):
    nome = StringField()
    data_inicio = StringField(validators=[DataRequired()])
    data_fim = StringField(validators=[DataRequired()])


class AtendimentoForm(Form):
    nome = StringField()
    telefone = StringField()
