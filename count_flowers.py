# список цветов в букете и соответствующих им количеств
bouquet = {"роза": 0, "орхидея": 0, "тюльпан": 0, "ирис": 0, "нарцисс": 0, "гвоздика": 0, "пион": 0, "лилия": 0, "сирень": 0}

# запрос количества каждого типа цветов от пользователя
for flower in bouquet:
    bouquet[flower] = int(input(f"Сколько {flower} в букете? "))

# подсчет общего количества цветов в букете
total_flowers = sum(bouquet.values())

# вывод общего количества цветов в букете
print(f"Ваш букет состоит из {total_flowers} цветов.")
