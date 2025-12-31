import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

app = create_app()

if __name__ == "__main__":
    print("=" * 50)
    print("SERVIDOR HELPO INICIANDO...")
    print("Acesse: http://localhost:5000")
    print("=" * 50)
    try:
        app.run(host='localhost', port=5000, debug=False, threaded=True)
    except Exception as e:
        print(f"ERRO: {e}")
        import traceback
        traceback.print_exc()
        input("Pressione Enter para sair...")
