from flask import Flask, render_template, request
from Login import Login

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/logar", methods=["POST"])
def logar():
    userName = request.form["userName"]
    password = request.form["password"]

    sistema_login = Login()
    usuario = sistema_login.autenticar(userName, password)
    sistema_login.fechar_conexao()

    if usuario:
        return f"<h1>Bem-vindo, {usuario[3]}!</h1>"
    else:
        return "<h1>Usuário ou senha inválidos!</h1>"

if __name__ == "__main__":
    app.run(debug=True)