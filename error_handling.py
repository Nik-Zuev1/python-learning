import requests
try:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    if response.status_code == 200:
        data = response.json()
        rub = data["rates"]["RUB"]
        print("Курс доллара к рублю:", rub, "рублей")
    else:
        print("сервер ответил с ошибкой", response.status_code)
except Exception as error:
    print("Что-то пошло не так:", error)