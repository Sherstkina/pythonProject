price = 0
tickets = int(input("Введите количество билетов:"))
age = int(input("Введите возраст:"))
for tickets in range(tickets):
    if age < 18:
        price += 0
    elif 18 <= age <= 25:
        price += 990
    elif age > 25:
        price += 1390
if tickets > 3:
    price -= price/100*10
print("К оплате:",price)
