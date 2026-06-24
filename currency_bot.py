import requests
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
def get_rates():
    try: 
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        if response.status_code == 200:
            data = response.json()
            rub = data["rates"]["RUB"]
            eur = data["rates"]["EUR"]
            date = data["date"]
            return f"Курсы валют на {date}:\n1$ = {rub} руб.\n1$ = {eur} евро"
        else:
            return "Не удалось получить курсы валют"
    except Exception as error:
        return "Ошибка: " + str(error)

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        response = requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": message
        })
        if response.status_code == 200:
            print("Сообщение отправлено!")
        else:
            print("Ошибка отправки:", response.status_code)

    except Exception as error:
        print("Ошибка:", str(error))

message = get_rates()
send_telegram(message)