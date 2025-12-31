from app import create_app

# Cria a instância da aplicação
app = create_app()

if __name__ == "__main__":
    print("=" * 70)
    print("🚀 HELPO - SERVIDOR INICIANDO...")
    print("📍 Acesse: http://localhost:5000")
    print("=" * 70)
    app.run(host='localhost', port=5000, debug=True, use_reloader=False)