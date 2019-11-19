from werkzeug.utils import redirect

from app import app
from flask import render_template, request, jsonify
from app.models.forms import CadOrcamento, CadCliente
from app.models.tables import Cliente, db, Orcamento, ClienteSchema


def insert_cliente():
    pass

def delete_cliente():
    pass


@app.route("/", methods=["GET"])
def list_cliente():
    cli = ClienteSchema()
    if request.method == 'GET':
        cliente = Cliente.query.first()
        return cli.dump(cliente),200


def udpdate_cliente():
    pass