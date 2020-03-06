from flask import request, jsonify
from app.models.tables import Cliente, db, Contato, Endereco, ClienteSchema


def insert_cliente():
    # adiciona cliente
    cli = Cliente(request.json.get("nome"), request.json.get("cpfcnpj"))
    try:
        db.session.add(cli)
        db.session.commit()

        # adiciona contato
        for contatos in request.json.get("contatos"):
            co = Contato(contatos["nome"], contatos["telefone"], contatos["email"], contatos["principal"],
                         cli.id)
            db.session.add(co)
            db.session.commit()

        # adiciona endereco
        req_end = request.json.get("enderecos")
        end = Endereco(req_end["rua"], req_end["bairro"], req_end["cidade"], req_end["numero"],
                       req_end["complemento"], req_end["estado"], cli.id)
        db.session.add(end)
        db.session.commit()
        return jsonify({'MSG': 'Cliente salvo com sucesso!', 'dado': cli.id}), 201
    except:
        return jsonify({'MSG': 'nao foi possivel salvar', 'dado': {}}), 500


def delete_cliente(id):
    cli = Cliente.query.get(id)
    if not cli:
        return jsonify({'MSG': 'Cliente nao existe', 'dado': id}), 404
    else:
        try:
            Contato.query.filter_by(cliente_id=id).delete()
            Endereco.query.filter_by(cliente_id=id).delete()
            Cliente.query.filter_by(id=id).delete()
            db.session.commit()
            return jsonify({'MSG': 'Cliente deletado com sucesso!', 'dado': id}), 200
        except:
            return jsonify({'MSG': 'nao foi possivel deletar', 'dado': {}}), 500


def list_cliente():
    try:
        cli = ClienteSchema(many=True)
        cliente = Cliente.query.all()
        return cli.dumps(cliente), 200
    except:
        return jsonify({'MSG': 'nao foi possivel listar', 'dado': {}}), 500


def update_cliente():
    id_request = request.json.get("id")
    cli = Cliente.query.get(id_request)
    if not cli:
        return jsonify({'MSG': 'Cliente nao existe', 'dado': id_request}), 404
    else:
        # atualiza cliente
        cli.nome = request.json.get("nome")
        cli.cpfcnpj = request.json.get("cpfcnpj")
        db.session.commit()

        # atualiza endereco
        req_end = request.json.get("enderecos")
        end = Endereco.query.filter_by(cliente_id=id_request).one()
        end.rua = req_end["rua"]
        end.bairro = req_end["bairro"]
        end.cidade = req_end["cidade"]
        end.numero = req_end["numero"]
        end.complemento = req_end["complemento"]
        end.estado = req_end["estado"]
        db.session.commit()

        # atualiza contatos
        co = Contato.query.filter_by(cliente_id=id_request).delete()
        db.session.commit()
        # adiciona contato
        for contatos in request.json.get("contatos"):
            co = Contato(contatos["nome"], contatos["telefone"], contatos["email"], contatos["principal"],
                         id_request)
            db.session.add(co)
            db.session.commit()

        return jsonify({'MSG': 'Cliente atualizado com sucesso', 'dado': id_request}), 201


def pesquisar_cliente(nome):
    try:
        cliente = ClienteSchema(many=True)
        cli = Cliente.query.filter(Cliente.nome.ilike('%' + nome + '%'))
        return cliente.dumps(cli)
    except:
        return jsonify({'MSG': 'Nao foi possivel encontrar cliente'}), 404


def list_cliente_principal():
    try:
        cli = ClienteSchema(many=True)
        cliente = db.session.query(Cliente).join(Contato, Endereco).filter(Contato.principal == False).all()
        print(cliente)
        return cli.dumps(cliente), 200
    except:
        return jsonify({'MSG': 'nao foi possivel listar', 'dado': {}}), 500
