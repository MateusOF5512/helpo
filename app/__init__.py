from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    # Configurações anti-cache para desenvolvimento
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.route("/")
    def index(): # type: ignore
        try:
            return render_template("home.html")
        except Exception as e:
            # Se falhar, retorna HTML direto
            return f"""
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>HELPO - Cuidado Profissional</title>
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-gray-50">
                <div class="min-h-screen flex items-center justify-center">
                    <div class="text-center">
                        <h1 class="text-6xl font-bold text-blue-600 mb-4">HELPO</h1>
                        <p class="text-2xl text-gray-700 mb-8">Cuidado profissional e confiável para quem você ama</p>
                        <div class="space-x-4">
                            <a href="/cliente" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700">Sou Cliente</a>
                            <a href="/cuidador" class="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700">Sou Cuidador</a>
                        </div>
                        <div class="mt-8">
                            <a href="/planos" class="text-blue-600 hover:underline">Ver Planos</a>
                        </div>
                        <p class="mt-4 text-red-500">Debug: Erro ao carregar template - {str(e)}</p>
                    </div>
                </div>
            </body>
            </html>
            """
    
    @app.route("/teste")
    def teste():
        return "<h1>TESTE - Se você vê isso, o Flask está funcionando!</h1>"

    @app.route("/cliente")
    def cliente():
        return render_template("client.html")

    @app.route("/planos")
    def planos():
        return render_template("pricing.html")

    @app.route("/cuidador")
    def cuidador():
        return render_template("caregiver.html")

    return app
