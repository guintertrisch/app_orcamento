from flask import render_template

from app import app
from app.controllers import clientes, atendimentos
from app.forms.forms import CadastroForm, PesquisaForm


@app.route("/clientes", methods=["POST"])
def post_cliente():
    return clientes.insert_cliente()


@app.route("/clientes/<id>", methods=["DELETE"])
def delete_cliente(id):
    return clientes.delete_cliente(id)


@app.route("/clientes", methods=["GET"])
def get_cliente():
    form = PesquisaForm()
    return render_template('consulta_atendimento.html', form=form)
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
    return render_template('home1.html', form=form)


@app.route("/", methods=["GET"])
def home_page():
    form = CadastroForm()
    return render_template('home1.html', form=form)


@app.route("/atendimentos", methods=["GET"])
def goto_atendimentos():
    form = PesquisaForm()
    return render_template('consulta_atendimento.html', form=form)


@app.route("/atendimentos/consultas", methods=["GET"])
def get_atendimentos_seis_meses():
    form = PesquisaForm()
    return render_template('consulta_atendimento.html', cliente=atendimentos.retorna_atendimentos(), form=form)


@app.route("/atendimentos/consultas", methods=["GET"])
def get_atendimentos_dose_meses():
    form = PesquisaForm()
    return render_template('consulta_atendimento.html', cliente=atendimentos.retorna_atendimentos_dose_meses(),
                           form=form)
