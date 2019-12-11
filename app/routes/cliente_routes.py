from app import app
from flask import render_template, request, jsonify
from app.controllers import clientes
from app.models.tables import Cliente, db,ClienteSchema,Contato,Endereco


@app.route("/clientes", methods=["POST"])
def post_cliente():
    return clientes.insert_cliente()


@app.route("/clientes/<id>", methods=["DELETE"])
def delete_cliente(id):
    return clientes.delete_cliente(id)


@app.route("/clientes", methods=["GET"])
def get_cliente():
    return clientes.list_cliente()


@app.route("/clientes", methods=["PUT"])
def put_cliente():
    return clientes.update_cliente()

@app.route("/clientes/<nome>", methods=["GET"])
def pesquisar_cliente(nome):
    return clientes.pesquisar_cliente(nome)