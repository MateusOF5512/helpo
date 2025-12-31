from flask import Flask
import os
import sys

# Configuração do path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, 
            template_folder='app/templates',
            static_folder='app/static')

# Configurações
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HELPO - Cuidado Profissional para Idosos</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen">
    <!-- Header -->
    <header class="bg-white shadow-md">
        <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
                    <span class="text-white font-bold text-2xl">H</span>
                </div>
                <span class="text-3xl font-bold text-gray-900">HELPO</span>
            </div>
            <nav class="hidden md:flex space-x-6">
                <a href="/" class="text-gray-700 hover:text-blue-600 font-medium">Home</a>
                <a href="/planos" class="text-gray-700 hover:text-blue-600 font-medium">Planos</a>
                <a href="#contato" class="text-gray-700 hover:text-blue-600 font-medium">Contato</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <main class="max-w-7xl mx-auto px-6 py-20">
        <div class="text-center mb-16">
            <h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
                Cuidado profissional e confiável<br>
                <span class="text-blue-600">para quem você ama</span>
            </h1>
            <p class="text-xl text-gray-600 mb-10 max-w-3xl mx-auto">
                Conectamos famílias a cuidadores qualificados para proporcionar o melhor atendimento aos idosos
            </p>
            
            <div class="flex flex-col md:flex-row gap-4 justify-center">
                <a href="/cliente" class="bg-blue-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-blue-700 transition transform hover:scale-105">
                    📋 Sou Cliente
                </a>
                <a href="/cuidador" class="bg-green-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-green-700 transition transform hover:scale-105">
                    👨‍⚕️ Sou Cuidador
                </a>
            </div>
        </div>

        <!-- Features -->
        <div class="grid md:grid-cols-3 gap-8 mt-20">
            <div class="bg-white p-8 rounded-xl shadow-lg">
                <div class="text-4xl mb-4">🔒</div>
                <h3 class="text-xl font-bold mb-3">Segurança</h3>
                <p class="text-gray-600">Cuidadores verificados e qualificados</p>
            </div>
            <div class="bg-white p-8 rounded-xl shadow-lg">
                <div class="text-4xl mb-4">📅</div>
                <h3 class="text-xl font-bold mb-3">Flexibilidade</h3>
                <p class="text-gray-600">Agende conforme sua necessidade</p>
            </div>
            <div class="bg-white p-8 rounded-xl shadow-lg">
                <div class="text-4xl mb-4">💙</div>
                <h3 class="text-xl font-bold mb-3">Qualidade</h3>
                <p class="text-gray-600">Atendimento humanizado e profissional</p>
            </div>
        </div>

        <!-- CTA -->
        <div class="text-center mt-20">
            <a href="/planos" class="text-blue-600 hover:text-blue-700 text-lg font-semibold hover:underline">
                Ver Planos e Preços →
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-8 mt-20">
        <div class="max-w-7xl mx-auto px-6 text-center">
            <p>&copy; 2025 HELPO - Todos os direitos reservados</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route("/teste")
def teste():
    return "<h1 style='text-align:center; margin-top:50px; font-family:Arial; color:#1e40af;'>✅ Servidor Flask está FUNCIONANDO!</h1>"

@app.route("/cliente")
def cliente():
    return "<h1 style='text-align:center; margin-top:50px;'>Módulo Cliente (em desenvolvimento)</h1>"

@app.route("/cuidador")
def cuidador():
    return "<h1 style='text-align:center; margin-top:50px;'>Módulo Cuidador (em desenvolvimento)</h1>"

@app.route("/planos")
def planos():
    return "<h1 style='text-align:center; margin-top:50px;'>Planos e Preços (em desenvolvimento)</h1>"

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 HELPO - SERVIDOR INICIANDO...")
    print("📍 Acesse: http://localhost:5000")
    print("="*70 + "\n")
    
    app.run(
        host='localhost',
        port=5000,
        debug=False,
        threaded=True
    )
