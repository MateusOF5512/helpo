from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>HELPO - Servidor Funcionando!</h1><p>Se você vê isso, o Flask está OK.</p>"

@app.route("/teste")
def teste():
    return "<h1>Teste OK!</h1>"

if __name__ == "__main__":
    print("\n" + "="*60)
    print("SERVIDOR TESTE INICIANDO...")
    print("Acesse: http://localhost:5000")
    print("="*60 + "\n")
    app.run(host='localhost', port=5000, debug=False, threaded=True)
