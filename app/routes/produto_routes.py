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