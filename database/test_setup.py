from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)

# Test connection
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.all())  # Should print [(1,)]
