from flask import Flask, render_template, request
from chatbot import respond
from database import crear_bd

app = Flask(__name__)

crear_bd()


@app.route("/", methods=["GET", "POST"])
def home():

    respuesta = "Sistema listo ⚽"

    if request.method == "POST":
        pregunta = request.form.get("pregunta")
        if pregunta:
            respuesta = respond(pregunta)

    return render_template("index.html", respuesta=respuesta)


if __name__ == "__main__":
    app.run(debug=True)