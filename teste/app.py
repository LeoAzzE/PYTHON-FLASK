from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    lista = [
    {
    "aluno": "leo",
    "professor": "thomas"
    },
    {
        "aluno": "leleco",
        "professor": "alice"
    }
]
    return render_template('home.html', **locals())

@app.route("/usuarios/<nome_usuario>")
def getPerson(nome_usuario):
    return render_template('home.html', nome=nome_usuario)

if __name__ == "__main__":
    app.run(debug=True, port=3333)