import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client


ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)


def init_connection():
    try:
        url = "https://mszwldawekkqpfsszcmy.supabase.co"
        key = "sb_secret_U-SlSZlkPbm9Qc8WnVJ29w_RaxFydeY"

        return create_client(url, key)

    except Exception as e:
        print(f"Erro de conexão com o Supabase: {e}")
        return None


supa = init_connection()
print(supa)