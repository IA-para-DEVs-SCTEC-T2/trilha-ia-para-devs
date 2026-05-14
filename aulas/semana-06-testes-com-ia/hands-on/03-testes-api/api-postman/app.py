from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    senha = data.get("senha")

    if email == "user@test.com" and senha == "123456":
        return jsonify({
            "token": "abc123",
            "user": {
                "email": email
            }
        }), 200

    return jsonify({
        "error": "Credenciais inválidas"
    }), 401


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify([
        {
            "id": 1,
            "nome": "Notebook",
            "preco": 3500.00
        },
        {
            "id": 2,
            "nome": "Mouse",
            "preco": 80.00
        }
    ]), 200


@app.route("/tickets", methods=["POST"])
def criar_ticket():
    data = request.get_json()

    title = data.get("title")
    category = data.get("category")
    priority = data.get("priority")

    if not title or not category or not priority:
        return jsonify({
            "error": "Campos obrigatórios ausentes"
        }), 400

    return jsonify({
        "id": 42,
        "title": title,
        "category": category,
        "priority": priority,
        "createdAt": "2026-05-12T10:30:00Z"
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=3000)