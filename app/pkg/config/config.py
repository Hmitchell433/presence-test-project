import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_PORT = int(os.getenv("SERVER_PORT", 8080))
