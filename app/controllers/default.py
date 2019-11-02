from app import app
from flask import render_template, request
from app.models.forms import CadOrcamento, CadCliente
from app.models.tables import Cliente, db, Orcamento


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/orcamento", methods=["GET","POST"])
def cadastroDeOrcamento():

    form = CadOrcamento()
    listCliente = Cliente.query.all()
    listOrcamentos = Orcamento.query.all()
    if request.method == 'POST':
        print(request.form.get('inputCliente'))
        if form.validate_on_submit():
            msg = None
            #print(form.username.data)
            #print(form.password.data)'''
            orcamento = Orcamento(form.quantidade.data,
                                  form.produto.data,
                                  form.detalhe.data,
                                  form.acao.data,
                                  form.valor.data,
                                  form.observacao.data,
                                  "5")
            db.session.add(orcamento)
            db.session.commit()
            msg = 'Orçamento Salvo com Sucesso!'
            #return render_template('cad_orcamentos.html',form=form,frase=msg)
            return '<a href="/orcamento"> Voltar</a>'
    else:
      return render_template('cad_orcamentos.html',form=form,cliente=listCliente)
      #return render_template('lista_orcamentos.html',listOrc=listOrcamentos)





@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    i = Cliente.query.all()
    print(i[2].data)
    return "OK"

@app.route("/cadorcamento")
def orcamento():
    return render_template('cad_orcamento.html')

@app.route("/chama",methods =["GET"])
def chamametodo():
    return render_template('metodo.html')

@app.route("/ok",methods =["GET","POST"])
def chamou():
    return "<h>oka</h>"

@app.route("/cliente", methods=["GET","POST"])
def cadastroDeClientes():
    formCli = CadCliente()

    if request.method == 'POST':
        msg = None
        novoCliente = Cliente(formCli.cliente.data,
                              formCli.contato.data,
                              formCli.endereco.data)
        db.session.add(novoCliente)
        db.session.commit()
        msg = 'Cliente Salvo com Sucesso!'
        return '<a href="/cliente"> Voltar</a>'
    else:
        return render_template("cad_clientes.html", formCli=formCli)
