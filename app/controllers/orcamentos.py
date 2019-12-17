from flask import request, jsonify
from app.models.orcamento import Orcamento,OrcamentoSchema
from app.models.orcamento_detalhe import OrcamentoDetalhe
from app.models.tables import Cliente, ClienteSchema
from datetime import datetime
from app import db

def insert_orcamento():
    id_request = request.json.get("cliente_id")
    data_agendamento = datetime.strptime(request.json.get("data_agendamento"), '%d/%m/%Y').date()
    cli = Cliente.query.get(id_request)
    if not cli:
        return jsonify({'MSG': 'Cliente nao existe', 'dado': id_request}), 404
    else:
        orc = Orcamento(data_agendamento, request.json.get("descricao"), id_request)
        db.session.add(orc)
        db.session.commit()

        #adiciona itens do orcamento
        for itens in request.json.get("itens"):
            orc_itens = OrcamentoDetalhe(itens["quantidade"], itens["produto_servico"], itens["acao"], itens["valor"],
                         orc.id)
            db.session.add(orc_itens)
            db.session.commit()
        return jsonify({'MSG': 'Orcamento salvo com sucesso!', 'dado': orc.id}), 201

def list_orcamento():
    orca = OrcamentoSchema(many=True, only=("id",
                                            "descricao",
                                            "data_conclusao",
                                            "data_agendamento",
                                            "data_cancelamento",
                                            "cliente.nome",
                                            "cliente.id")
                           )
    orc = Orcamento.query.all()
    return orca.dumps(orc), 200

def pesquisa_orcamento_cliente(id):
    orca = OrcamentoSchema(many=True)
    orc = Orcamento.query.filter_by(cliente_id=id).all()
    return orca.dumps(orc), 200
