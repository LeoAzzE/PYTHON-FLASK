from flask import Flask, request, jsonify
from flask_api import status

app = Flask(__name__)

jogadores = [     
    {  
        "id" : 1,
        "nome": "Renato augusto",
        "clube": "corinthians",
    },
    {
        "id" : 2,
        "nome": "Arrasca",
        "clube": "Flamengo",
    },
    {
        "id" : 3,
        "nome": "valverde",
        "clube": "real madrid",
    }
]

@app.route("/jogadores", methods=['GET'])
def getJogadores():
    return jsonify(jogadores), status.HTTP_200_OK

@app.route("/jogadores/<int:id>", methods=['GET'])
def getUmJogador(id):
    try:
        for jogador in jogadores:
            if(jogador.get('id') == id):
                return jsonify(jogador), status.HTTP_200_OK
            else:
                return jsonify({'mensagem:': "Erro ao buscar"})
    except Exception as ex:
        return jsonify({'mensagem:': "Erro ao buscar"})      

@app.route("/jogadores/<int:id>", methods=['PUT'])
def editPlayer(id):
    try:
        jogadorJson = request.get_json()
        for indice, jogador in enumerate(jogadores):
            if jogador.get('id') == id:
                jogadores[indice].update(jogadorJson)
                return jsonify(jogadores[indice]), status.HTTP_200_OK
    except Exception as ex:
        return jsonify({'mensagem:': "Erro ao atualizar"})

@app.route("/jogadores", methods=['POST'])
def criarJogador():
    try:
        jogadorJson = request.get_json()
        jogadores.append(jogadorJson)
        return jsonify(jogadores), status.HTTP_201_CREATED
    except Exception as ex:
        return jsonify({'mensagem:': "Erro ao criar"})

@app.route("/jogadores/<int:id>", methods=['DELETE'])
def excluirJogador(id):
    try:
        for indice, jogador in enumerate(jogadores):
            if jogador.get('id') == id:
                del jogadores[indice]
                return jsonify(jogadores), status.HTTP_204_NO_CONTENT
            else:
                return jsonify({'mensagem:': "Erro ao deletar"})
    except Exception as ex:
        return jsonify({'mensagem:': "Erro ao deletar"})


if __name__ == "__main__":
    app.run(debug=True)