from app import app
from flask import render_template, request, jsonify
from app.models.tables import Cliente, db, Orcamento, ClienteSchema,Contato,ContatoSchema,Endereco


@app.route("/clientes", methods=["POST"])
def insert_cliente():

    #adiciona cliente
    cli = Cliente(request.json.get("nome"),request.json.get("cpfcnpj"))
    db.session.add(cli)
    db.session.commit()

    #adiciona contato
    for contatos in request.json.get("contatos"):
        co = Contato(contatos["nome"],contatos["telefone"],contatos["email"],contatos["principal"],
                     cli.id)
        db.session.add(co)
        db.session.commit()

    #adiciona endereco
    req_end = request.json.get("enderecos")
    end = Endereco(req_end["rua"], req_end["bairro"], req_end["cidade"],req_end["numero"],
                   req_end["complemento"],req_end["estado"],cli.id)
    db.session.add(end)
    db.session.commit()

    return {"status":201,"MSG":"Cliente add com sucesso!","id":cli.id}


@app.route("/clientes/<id>", methods=["DELETE"])
def delete_cliente(id):

    Cliente.query.filter_by(id=id).delete()
    Contato.query.filter_by(cliente_id=id).delete()
    Endereco.query.filter_by(cliente_id=id).delete()
    db.session.commit()

    return {"status":200,"MSG":"Cliente deletado com sucesso!","id":id}


@app.route("/clientes", methods=["GET"])
def list_cliente():
    cli = ClienteSchema(many=True)
    if request.method == 'GET':
        cliente = Cliente.query.all()
        return cli.dumps(cliente),200


@app.route("/clientes", methods=["PUT"])
def udpdate_cliente():
    id = request.json.get("id")
    cli = Cliente.query.filter_by(id=id)

    #pega dados novos cliente
    cli_up = Cliente(request.json.get("nome"),request.json.get("cpfcnpj"))
    cli = cli_up
    db.session.add(cli)
    db.session.commit()

    return {"status":200,"MSG":"Cliente atualizado com sucesso!","id":id}