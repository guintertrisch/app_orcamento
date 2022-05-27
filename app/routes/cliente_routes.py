from flask import render_template
from flask import request

from app import app
from app.controllers import clientes, atendimentos
from app.forms.forms import CadastroForm, PesquisaForm, AtendimentoForm
from app.models.cliente import Cliente


@app.route("/clientes", methods=["POST"])
def post_cliente():
    return clientes.insert_cliente()


@app.route("/clientes/<id>", methods=["DELETE"])
def delete_cliente(id):
    return clientes.delete_cliente(id)


@app.route("/clientes", methods=["GET"])
def get_cliente():
    form = PesquisaForm()
    return render_template('consultar_atendimento.html', form=form)
    # return clientes.list_cliente()


@app.route("/clientes", methods=["PUT"])
def put_cliente():
    return clientes.update_cliente()


@app.route("/clientes/<nome>", methods=["GET"])
def pesquisar_cliente(nome):
    return clientes.pesquisar_cliente(nome)


@app.route("/", methods=["POST"])
def cadastar():
    form = CadastroForm()
    clientes.insert_cliente(form)
    return render_template('home_page.html', form=form)


@app.route("/", methods=["GET"])
def home_page():
    form = CadastroForm()
    form.nome.data = ''
    form.telefone.data = ''
    form.data_atendimento.data = ''
    form.descricao.data = ''
    return render_template('home_page.html', form=form)


@app.route("/atendimentos/cadastrar", methods=["GET"])
def home_atendimentos():
    form = AtendimentoForm()
    return render_template('atendimento.html', form=form)


@app.route("/atendimentos/cadastrar", methods=["POST"])
def busca_cliente():
    form = AtendimentoForm()
    cliente = clientes.pesquisar_cliente(form)
    return render_template('atendimento.html', form=form, cliente=cliente)


@app.route("/atendimentos/cadastrar/novo/<id>", methods=["GET", "POST"])
def cadastrar_novo_atendimento(id):
    form1 = CadastroForm()
    if request.method == 'POST':
        atendimentos.insere_novo_atendimento(form1, id)
        return render_template('novo_atendimento.html', form=form1)
    else:
        cli = Cliente.query.get(id)
        form1.nome.data = cli.nome
        form1.telefone.data = cli.telefone
        return render_template('novo_atendimento.html', form=form1)


@app.route("/atendimentos/consultas", methods=["GET"])
def goto_atendimentos():
    form = PesquisaForm()
    return render_template('consultar_atendimento.html', form=form)


@app.route("/atendimentos/consultas/<periodo>", methods=["GET"])
def consultar_periodo(periodo):
    form = PesquisaForm()
    if periodo == 'seis_meses':
        cliente = atendimentos.retorna_atendimentos_seis_meses()
    elif periodo == 'doze_meses':
        cliente = atendimentos.retorna_atendimentos_dose_meses()
    else:
        print('datas: ' + form.data_fim.data)
        cliente = home_atendimentos.retorna_filtro_periodo(form)
    return render_template('consultar_atendimento.html', cliente=cliente, form=form)


@app.route("/atendimentos/consultas/filtro", methods=["POST", "GET"])
def consultar_periodo_filtro():
    form = PesquisaForm()
    cliente = atendimentos.retorna_filtro_periodo(form)
    return render_template('consultar_atendimento.html', cliente=cliente, form=form)
