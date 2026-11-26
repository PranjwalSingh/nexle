import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "backend.env"), override=True)

# Environment
ENV = os.getenv("ENV", "production")

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_PROD_URL")
SUPABASE_PUBLISHABLE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY")
SUPABASE_SECRET_KEY = os.getenv("SUPABASE_SECRET_KEY")
DB_PASSWORD = os.getenv("db_password_supabase_jobscout")

# App
FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "*")
SECRET_KEY = os.getenv("SECRET_KEY")
API_URL = os.getenv("API_URL", "http://localhost:8000")

# LLM
GROQ_API_KEY = os.getenv("GROQ_API_KEY")