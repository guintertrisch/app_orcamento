from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SelectField
from wtforms.validators import DataRequired
from app.models.tables import Cliente


class CadOrcamento(FlaskForm):
    #cliente = StringField("cliente",validators=[DataRequired()])
    #cliente = SelectField("Cliente",choices = [(cli.id, cli.nome) for cli in Cliente.query.all()])
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