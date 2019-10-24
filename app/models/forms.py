from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired


class Orcamento(FlaskForm):
    cliente = StringField("cliente",validators=[DataRequired()])
    contato = StringField("contato", validators=[DataRequired()])
    local = StringField("local", validators=[DataRequired()])
    data = StringField("data", validators=[DataRequired()])
    descricao = TextAreaField("descricao", validators=[DataRequired()])
    quantidade = StringField("quantidade", validators=[DataRequired()])
    produto = StringField("produto", validators=[DataRequired()])
    detalhe = StringField("detalhe", validators=[DataRequired()])
    acao = StringField("acao", validators=[DataRequired()])
    valor = StringField("valor", validators=[DataRequired()])
    observacao = TextAreaField("observacao")

    '''contato = PasswordField("password",validators=[DataRequired()])
    remember_me = BooleanField("remember_me")'''