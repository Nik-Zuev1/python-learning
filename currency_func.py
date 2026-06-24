import requests
def get_rate(currency):
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        if response.status_code == 200:
            data = response.json()
            return data["rates"][currency]
        else:
            return "Ошибка сервера: " + str(response.status_code)
    except Exception as e:
        return "Нет соединения: " + str(e)

rub = get_rate("RUB")
eur = get_rate("EUR")
gbp = get_rate("GBP")

print ("1 доллар =", rub, "рублей")
print ("1 доллар =", eur, "евро")
print ("1 доллар =", gbp, "фунтов")