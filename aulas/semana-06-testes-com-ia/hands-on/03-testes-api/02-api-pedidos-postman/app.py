from flask import Flask, request, jsonify

app = Flask(__name__)

PRODUTOS = {
    1: {
        "id": 1,
        "nome": "Notebook",
        "preco": 3500.00,
        "estoque": 5
    },
    2: {
        "id": 2,
        "nome": "Mouse",
        "preco": 80.00,
        "estoque": 20
    },
    3: {
        "id": 3,
        "nome": "Teclado",
        "preco": 150.00,
        "estoque": 10
    }
}


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API de pedidos funcionando",
        "endpoints": {
            "produtos": "GET /produtos",
            "pedido": "POST /pedidos"
        }
    }), 200


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(list(PRODUTOS.values())), 200


@app.route("/pedidos", methods=["POST"])
def criar_pedido():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Body JSON obrigatório"
        }), 400

    cliente = data.get("cliente")
    produto_id = data.get("produto_id")
    quantidade = data.get("quantidade")
    cupom = data.get("cupom")

    if not cliente or not produto_id or not quantidade:
        return jsonify({
            "error": "Campos obrigatórios: cliente, produto_id e quantidade"
        }), 400

    if produto_id not in PRODUTOS:
        return jsonify({
            "error": "Produto não encontrado"
        }), 404

    if not isinstance(quantidade, int) or quantidade <= 0:
        return jsonify({
            "error": "Quantidade deve ser um número inteiro maior que zero"
        }), 400

    produto = PRODUTOS[produto_id]

    if quantidade > produto["estoque"]:
        return jsonify({
            "error": "Estoque insuficiente",
            "estoque_disponivel": produto["estoque"]
        }), 400

    subtotal = produto["preco"] * quantidade
    desconto = 0

    if cupom == "DESCONTO10":
        desconto = subtotal * 0.10

    total = subtotal - desconto

    pedido = {
        "id": 101,
        "cliente": cliente,
        "produto": {
            "id": produto["id"],
            "nome": produto["nome"],
            "preco_unitario": produto["preco"]
        },
        "quantidade": quantidade,
        "subtotal": subtotal,
        "desconto": desconto,
        "total": total,
        "status": "criado"
    }

    return jsonify(pedido), 201


if __name__ == "__main__":
    app.run(debug=True, port=3001)