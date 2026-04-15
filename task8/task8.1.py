world = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин", "Италия": "Рим", "Великобритания": "Лондон", "Япония": "Токио", "Китай": "Пекин", "США": "Вашингтон"}

'''a'''
print(world)

'''b'''
country = input("Введите страну: ")

if country in world:
    capital = world[country]

print(f"Для страны {country} является столица {capital}")

'''c'''
world_list = list(world.keys())
world_list.sort()
for i in world_list:
    print(i)