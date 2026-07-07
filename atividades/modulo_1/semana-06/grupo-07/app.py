from flask import Flask, request, jsonify

app = Flask(__name__)

RECADOS_INICIAIS = [
    {"id": 1, "autor": "Ana", "mensagem": "Reunião às 14h na sala 3", "lido": False},
    {"id": 2, "autor": "Bob", "mensagem": "Favor revisar o relatório", "lido": True},
    {"id": 3, "autor": "Carol", "mensagem": "Pedido de férias aprovado", "lido": False},
]

recados = [r.copy() for r in RECADOS_INICIAIS]
_next_id = len(RECADOS_INICIAIS) + 1


def resetar_recados():
    global _next_id
    recados.clear()
    recados.extend(r.copy() for r in RECADOS_INICIAIS)
    _next_id = len(RECADOS_INICIAIS) + 1


@app.route("/recados", methods=["POST"])
def criar_recado():
    global _next_id
    data = request.get_json(silent=True) or {}

    if not data.get("autor"):
        return jsonify({"error": "autor é obrigatório"}), 400
    if not data.get("mensagem"):
        return jsonify({"error": "mensagem é obrigatória"}), 400

    recado = {
        "id": _next_id,
        "autor": data["autor"],
        "mensagem": data["mensagem"],
        "lido": False,
    }
    _next_id += 1
    recados.append(recado)
    return jsonify(recado), 201


@app.route("/recados", methods=["GET"])
def listar_recados():
    return jsonify(recados), 200


if __name__ == "__main__":
    app.run(debug=True)
