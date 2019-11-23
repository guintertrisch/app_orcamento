from app import app
from flask import render_template, request, jsonify
from app.models.tables import Cliente, db, Orcamento, ClienteSchema,Contato,ContatoSchema,Endereco

@app.route("/clientes", methods=["POST"])
def insert_cliente():

    #adiciona cliente
    cli = Cliente(request.json.get("nome"),request.json.get("cpfcnpj"))
    db.session.add(cli)
    db.session.commit()
    id_cliente = Cliente.query.filter_by(nome=cli.nome).first()

    #adiciona contato
    for contatos in request.json.get("contatos"):
        co = Contato(contatos["nome"],contatos["telefone"],contatos["email"],contatos["principal"],
                     id_cliente.id)
        db.session.add(co)
        db.session.commit()

    #adiciona endereco
    for enderecos in request.json.get("enderecos"):
        end = Endereco(enderecos["rua"],enderecos["bairro"],enderecos["cidade"],
                       enderecos["numero"],enderecos["complemento"],enderecos["estado"],
                       id_cliente.id)
        db.session.add(end)
        db.session.commit()

    return {"status":200}


def delete_cliente():
    pass



@app.route("/clientes", methods=["GET"])
def list_cliente():
    cli = ClienteSchema(many=True)
    if request.method == 'GET':
        cliente = Cliente.query.all()
        return cli.dumps(cliente),200

@app.route("/clientes", methods=["PUT"])
def udpdate_cliente():
    cli  = Cliente.query.filter()