from flask import Flask, render_template, request
from cpf_validator import cpf_valido
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        cpf = request.form.get("cpf")

        if cpf_valido(cpf):
            resultado = "CPF válido"
        else:
            resultado = "CPF inválido!"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)