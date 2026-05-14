from flask import Flask, request, jsonify

app = Flask(__name__)

recados = []
proximo_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API de recados funcionando",
        "endpoints": {
            "listar_recados": "GET /recados",
            "criar_recado": "POST /recados"
        }
    }), 200


@app.route("/recados", methods=["GET"])
def listar_recados():
    return jsonify(recados), 200


@app.route("/recados", methods=["POST"])
def criar_recado():
    global proximo_id

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Body JSON obrigatório"
        }), 400

    autor = data.get("autor")
    mensagem = data.get("mensagem")

    if not autor or not mensagem:
        return jsonify({
            "error": "Campos obrigatórios: autor e mensagem"
        }), 400

    recado = {
        "id": proximo_id,
        "autor": autor,
        "mensagem": mensagem,
        "lido": False
    }

    recados.append(recado)
    proximo_id += 1

    return jsonify(recado), 201


if __name__ == "__main__":
    app.run(debug=True, port=3000)