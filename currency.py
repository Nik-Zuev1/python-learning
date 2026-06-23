import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = response.json()

rub = data["rates"]["RUB"]
eur = data["rates"]["EUR"]
gbp = data["rates"]["GBP"]
date = data["date"]

print("Дата:", date)
print("1 доллар =", rub, "рублей")
print("1 доллар =", eur, "евро")
print("1 доллар =", gbp, "фунтов")
