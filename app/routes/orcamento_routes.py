from app import app
from app.controllers import orcamentos


@app.route("/orcamentos", methods=["POST"])
def post_orcamento():
    return orcamentos.insert_orcamento()


@app.route("/orcamentos", methods=["PUT"])
def put_orcamento():
    pass


@app.route("/orcamentos/<id>", methods=["DELETE"])
def delete_orcamento(id):
    return orcamentos.delete_orcamento(id)


@app.route("/orcamentos", methods=["GET"])
def get_orcamento():
    return orcamentos.list_orcamento()


@app.route("/orcamentos/<id>", methods=["GET"])
def pesquisar_orcamento(id):
    return orcamentos.pesquisa_orcamento_cliente(id)
