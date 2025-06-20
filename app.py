from flask import Flask
from config import Config
from extensions import mysql, mail, bootstrap

from controllers.sistema_controller import sistema_bp
from controllers.carga_controller import carga_bp

app = Flask(__name__)
app.config.from_object(Config)

mysql.init_app(app)
mail.init_app(app)
bootstrap.init_app(app)

app.register_blueprint(sistema_bp)
app.register_blueprint(carga_bp)

from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
