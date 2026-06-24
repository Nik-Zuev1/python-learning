from dotenv import load_dotenv
import os
load_dotenv()

telegram_token = os.getenv("TELEGRAM_TOKEN")
api_key = os.getenv("API_KEY")

print("Токен: ", telegram_token)
print("API ключ: ", api_key)