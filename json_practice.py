order = {
    "id": 12345,
    "status": "оплачен",
    "customer": {
        "name": "Никита",
        "phone": "+79001234567",
        "city": "Москва"
    },
    "items": [
        {"name": "Сайт", "price": 10000},
        {"name": "Логотип", "price": 5000},
        {"name": "Тексты", "price": 3000}
    ],
    "total": 18000
}
print(order["customer"]["name"])
print(order["items"][0]["name"])
print(order["items"][1]["price"])

total = 0
for item in order["items"]:
    total = total + item["price"]
print("Итого:", total, "руб.")