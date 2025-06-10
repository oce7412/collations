import os
from flask import Flask, render_template

app = Flask(__name__)


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

@app.route("/")
def home():
    return "Bienvenue sur l'app Flask"