from flask import request, jsonify
from app.models.produto import db, Produto, ProdutoSchema


def insert_produto():
    try:
        produto = Produto(request.json.get("nome"))
        db.session.add(produto)
        db.session.commit()
        return jsonify({'MSG': 'Produto salvo com sucesso!', 'dado': produto.nome}), 201
    except:
        return jsonify({'MSG': 'nao foi possivel salvar produto', 'dado': {}}), 500


def update_produto():
    id_request = request.json.get("id")
    produto = Produto.query.get(id_request)
    if not produto:
        return jsonify({'MSG': 'Produto nao existe', 'dado': id_request}), 404
    else:
        try:
            produto.nome = request.json.get("nome")
            db.session.commit()
            return jsonify({'MSG': 'Produto atualizado com sucesso', 'dado': id_request}), 201
        except:
            return jsonify({'MSG': 'nao foi possivel atualizar produto', 'dado': {}}), 500


def delete_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'MSG': 'Produto nao existe', 'dado': id}), 404
    else:
        try:
            Produto.query.filter_by(id=id).delete()
            db.session.commit()
            return jsonify({'MSG':'Produto deletado com sucesso!','dado':id}), 200
        except:
            return jsonify({'MSG': 'nao foi possivel deletar', 'dado': {}}), 500


def list_produto():
    try:
        prod = ProdutoSchema(many=True)
        produto = Produto.query.all()
        return prod.dumps(produto), 200
    except:
        return jsonify({'MSG': 'Nao foi possivel listar produtos'}),500


def pesquisar_produto(nome):
    try:
        produto = ProdutoSchema(many=True)
        prod = Produto.query.filter(Produto.nome.ilike('%'+nome+'%'))
        return produto.dumps(prod)
    except:
        return jsonify({'MSG': 'Nao foi possivel encontrar produto'}), 404