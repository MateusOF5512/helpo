from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    
    # Desabilitar cache durante desenvolvimento
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/cliente")
    def cliente():
        # UI do módulo cliente (MVP) – futuro backend vai popular dados reais
        return render_template("client.html")

    @app.route("/planos")
    def planos():
        return render_template("pricing.html")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
