from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []
proximo_id = 1


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API de tarefas funcionando",
        "endpoints": {
            "listar_tarefas": "GET /tarefas",
            "criar_tarefa": "POST /tarefas",
            "concluir_tarefa": "POST /tarefas/<id>/concluir"
        }
    }), 200


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas), 200


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    global proximo_id

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Body JSON obrigatório"
        }), 400

    titulo = data.get("titulo")
    responsavel = data.get("responsavel")

    if not titulo or not responsavel:
        return jsonify({
            "error": "Campos obrigatórios: titulo e responsavel"
        }), 400

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "responsavel": responsavel,
        "concluida": False
    }

    tarefas.append(tarefa)
    proximo_id += 1

    return jsonify(tarefa), 201


@app.route("/tarefas/<int:tarefa_id>", methods=["GET"])
def buscar_tarefa(tarefa_id):
    tarefa = next((item for item in tarefas if item["id"] == tarefa_id), None)

    if not tarefa:
        return jsonify({
            "error": "Tarefa não encontrada"
        }), 404

    return jsonify(tarefa), 200


@app.route("/tarefas/<int:tarefa_id>/concluir", methods=["POST"])
def concluir_tarefa(tarefa_id):
    tarefa = next((item for item in tarefas if item["id"] == tarefa_id), None)

    if not tarefa:
        return jsonify({
            "error": "Tarefa não encontrada"
        }), 404

    tarefa["concluida"] = True

    return jsonify(tarefa), 200


if __name__ == "__main__":
    app.run(debug=True, port=3000)