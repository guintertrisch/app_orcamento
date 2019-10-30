from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class CadOrcamento(FlaskForm):
    cliente = StringField("cliente",validators=[DataRequired()])
    data = StringField("data", validators=[DataRequired()])
    descricao = TextAreaField("descricao", validators=[DataRequired()])
    quantidade = StringField("quantidade", validators=[DataRequired()])
    produto = StringField("produto", validators=[DataRequired()])
    detalhe = StringField("detalhe", validators=[DataRequired()])
    acao = StringField("acao", validators=[DataRequired()])
    valor = StringField("valor", validators=[DataRequired()])
    observacao = TextAreaField("observacao")


class CadCliente(FlaskForm):
    cliente = StringField("cliente", validators=[DataRequired()])
    contato = StringField("contato", validators=[DataRequired()])
    endereco = StringField("endereco", validators=[DataRequired()])