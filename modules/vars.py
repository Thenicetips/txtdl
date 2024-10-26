import os

API_ID    = os.environ.get("API_ID", "23728809")
API_HASH  = os.environ.get("API_HASH", "5d7165501181e2ef8000f333fe529678")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7764340374:AAH4xgZO5f0OGbtMR2C9koVWXeqP-vAi9LY") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
