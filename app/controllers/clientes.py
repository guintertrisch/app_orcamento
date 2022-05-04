import datetime
from datetime import datetime

from flask import request, jsonify

from app.models.cliente import Cliente, db, ClienteSchema


def insert_cliente(form):
    # adiciona cliente
    cli = Cliente(form.nome.data, form.telefone.data,
                  datetime.strptime(form.data_atendimento.data, '%d/%m/%Y').date())
    try:
        db.session.add(cli)
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
        cli.telefone = request.json.get("telefone")
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
    pass
