from app import app
from app.controllers import produtos


@app.route("/produtos", methods=["POST"])
def post_produto():
    return produtos.insert_produto()

@app.route("/produtos/<id>", methods=["PUT"])
def put_produto(id):
    return produtos.update_produto(id)

@app.route("/produtos/<id>", methods=["DELETE"])
def delete_produto(id):
    return produtos.delete_produto(id)

@app.route("/produtos",methods=["GET"])
def get_produto():
    return produtos.list_produto()

@app.route("/produtos/<nome>",methods=["GET"])
def pesquisar_produto(nome):
    return produtos.pesquisa_produto(nome)