from app import app
from flask import render_template
from app.models.forms import Orcamento
from app.models.tables import Cliente, db


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/orcamento", methods=["GET","POST"])
def cadastroOrcamento():

    form = Orcamento()

    if form.validate_on_submit():
        msg = None
       #print(form.username.data)
        #print(form.password.data)'''
        orcamento = Cliente(form.cliente.data,
                            form.contato.data,
                            form.local.data,
                            form.data.data,
                            form.descricao.data,
                            form.quantidade.data,
                            form.produto.data,
                            form.detalhe.data,
                            form.acao.data,
                            form.valor.data,
                            form.observacao.data)
        db.session.add(orcamento)
        db.session.commit()
        msg = 'Orçamento Salvo com Sucesso!'
        #return render_template('cadastro_orcamento.html',form=form,frase=msg)
        return '<a href="/orcamento"> Voltar</a>'

    return render_template('cadastro_orcamento.html',form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = Cliente.query.all()
    print(i[2].data)
    return "OK"

@app.route("/cadorcamento")
def orcamento():
    return render_template('cad_orcamento.html')


