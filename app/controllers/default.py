from werkzeug.utils import redirect

from app import app
from flask import render_template, request
from app.models.forms import CadOrcamento, CadCliente
from app.models.tables import Cliente, db, Orcamento


'''@app.route("/index")
@app.route("/")
def index():
    return render_template('lista_orcamentos.html')


@app.route("/orcamento", methods=["GET"])
def listOrcamento():
    listOrcamentos = Orcamento.query.all()
    return render_template('lista_orcamentos.html',listOrc=listOrcamentos)


@app.route("/cliente", methods=["GET","POST"])
def cadastroDeCliente():
    formCli = CadCliente()

    if request.method == 'POST':
        novoCliente = Cliente(formCli.cliente.data,
                              formCli.contato.data,
                              formCli.endereco.data)
        db.session.add(novoCliente)
        db.session.commit()
        msg = "Cliente Salvo com Sucesso!!!"
        return render_template("cad_clientes.html",formCli=formCli,msg=msg)
    else:
        return render_template("cad_clientes.html", formCli=formCli)


@app.route("/cadastroOrcamento",methods=["GET","POST"])
def cadastroDeOrcamento():
    form = CadOrcamento()
    listCliente = Cliente.query.all()
    if request.method == 'POST':

        msg = None
        orcamento = Orcamento(form.data.data,
                              form.quantidade.data,
                              form.produto.data,
                              form.detalhe.data,
                              form.acao.data,
                              form.valor.data,
                              form.observacao.data,
                              form.cliente.data)
        db.session.add(orcamento)
        db.session.commit()
        msg = 'Orçamento Salvo com Sucesso!'
        return redirect('/orcamento')
    else:
        return render_template('cad_orcamentos.html',form=form,cliente=listCliente)'''

