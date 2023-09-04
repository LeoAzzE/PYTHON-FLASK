from flask import Flask, jsonify, request

app = Flask(__name__)

listaPessoa = [
    {
        "id": 1,
        "nome": 'Leo',
        "idade": 21,
        "cpf" : '222-222-222-42'
    },
    {
        "id": 2,
        "nome": 'Leona',
        "idade": 26,
        "cpf" : '333-333-333-21'
    },
]

@app.route("/pessoas", methods=['GET'])
def getPessoas():
    return jsonify(listaPessoa)

@app.route("/pessoas/<int:id>", methods=['GET'])
def getPessoasPorId(id):
    for pessoa in listaPessoa:
        if pessoa.get('id') == id:
            return jsonify(pessoa)

@app.route("/pessoas/<int:id>", methods=['PUT'])
def editPessoa(id):
    pessoaEditada = request.get_json()
    for indice, pessoa in enumerate(listaPessoa):
        if pessoa.get('id') == id:
            listaPessoa[indice].update(pessoaEditada)
            return jsonify(listaPessoa[indice])

@app.route("/pessoas", methods=['POST'])
def criarPessoa():
    novaPessoa =  request.get_json()
    listaPessoa.append(novaPessoa)
    return jsonify(listaPessoa)

@app.route("/pessoas/<int:id>", methods=['DELETE'])
def delPessoa(id):
    for indice,pessoa in enumerate(listaPessoa):
        if pessoa.get('id') == id:
            del pessoa[indice]
    return jsonify(listaPessoa)


if __name__ == "__main__":
    app.run(debug=True)