import task21
import task22

print("Меню:")
print("1. Обчислити вираз (Модуль 1)")
print("2. Таблиця функції (Модуль 2)")

variant = input("Оберіть дію (введіть 1 або 2): ")

if variant == "1":
    task21.pryklad()
elif variant == "2":
    task22.tablitsa()
else:
    print("Неправильний вибір")