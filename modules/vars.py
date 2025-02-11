import os

API_ID    = os.environ.get("API_ID", "22812640")
API_HASH  = os.environ.get("API_HASH", "a03d3210acc79992955563c9de77f795")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7868606343:AAEs0pQLKdrMuw-O9FCf7d8IhDkc3_KBg14") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
