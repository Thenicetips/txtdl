import os

API_ID    = os.environ.get("API_ID", "24825870")
API_HASH  = os.environ.get("API_HASH", "12ab9061b6260f9b91632947331ea0f6")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7092414344:AAGxzU6QmtquQEC1AjwSSgaC9urTszVQydA") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
