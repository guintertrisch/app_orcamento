from werkzeug.utils import redirect

from app import app
from flask import render_template, request, jsonify
from app.models.forms import CadOrcamento, CadCliente
from app.models.tables import Cliente, db, Orcamento, ClienteSchema,Contato,ContatoSchema


def insert_cliente():
    pass

def delete_cliente():
    pass


@app.route("/clientes", methods=["GET"])
def list_cliente():
    cli = ClienteSchema(many=True)
    if request.method == 'GET':
        cliente = Cliente.query.all()
        return cli.dumps(cliente),200


def udpdate_cliente():
    pass