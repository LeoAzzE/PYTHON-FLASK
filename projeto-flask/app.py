from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config


app = Flask(__name__)

conexao = MySQL(app)

@app.route("/cursos", methods=['GET'])
def get_cursos():
    try:
        sql = "SELECT codigo, nome, creditos FROM curso"
        cursor = conexao.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursos=[]
        for dado in data:
            curso={'codigo':dado[0], 'nome':dado[1], 'creditos':dado[2]}
            cursos.append(curso)          
        return jsonify({'cursos':cursos, 'mensagem': "cursos listados"})
    
    except Exception as ex:
        return jsonify({'mensagem': "ERROR"})
   
@app.route('/cursos', methods=['POST'])
def registrar_curso():
    try:
        #print(request.json)
        cursor = conexao.connection.cursor()
        sql = """INSERT INTO curso (codigo, nome, creditos)
        VALUES ('{0}','{1}',{2})""".format(request.json['codigo'],
        request.json['nome'],
        request.json['creditos'])
        cursor.execute(sql)
        conexao.connection.commit()
        return jsonify({'mensagem:' "curso registrado"})
    except Exception as ex:
        return jsonify({'mensagem': "ERROR"})

@app.route('/cursos/<codigo>', methods=['DELETE'])
def delete_curso(codigo):
    try:
        #print(request.json)
        cursor = conexao.connection.cursor()
        sql = "DELETE FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        conexao.connection.commit()
        return jsonify({'mensagem:' "curso apagado"})
    except Exception as ex:
        return jsonify({'mensagem': "ERROR"})

def pagina_nao_encontrada(error):
    return "<h1>A pagina que tentou buscar não existe...<h1/>", 404

@app.route('/cursos/<codigo>', methods=['PUT'])
def atualizar_curso(codigo):
    try:
        #print(request.json)
        cursor = conexao.connection.cursor()
        sql = """UPDATE curso SET nome = '{0}', creditos={1} WHERE codigo = '{2}'""".format(
        request.json['nome'],
        request.json['creditos'],codigo)
        cursor.execute(sql)
        conexao.connection.commit()
        return jsonify({'mensagem:' "curso atualizado"})
    except Exception as ex:
        return jsonify({'mensagem': "ERROR"})

@app.route('/cursos/<codigo>', methods=['GET'])
def ler_curso(codigo):
    try:
        cursor = conexao.connection.cursor()
        sql = "SELECT codigo, nome, creditos FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None: 
            curso={'codigo':data[0], 'nome':data[1], 'creditos':data[2]}
            return jsonify({'curso':curso, 'mensagem': "curso encontrado"})
        else:
            return jsonify({'mensagem': "curso nao encontrado"})
    except Exception as ex:
        return jsonify({'mensagem': "cursos listados"})

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_nao_encontrada)
    app.run(debug=True)