def obchyslennya():
    # Перевірка чисел
    a = float(input("Введіть a (від 1 до 100): "))
    if a < 1 or a > 100:
        print("Помилка: число a має бути від 1 до 100")
        return  # Зупиняє функцію, якщо є помилка

    b = float(input("Введіть b (від 1 до 100): "))
    if b < 1 or b > 100:
        print("Помилка: число b має бути від 1 до 100")
        return

    # Обчислення x за умовами з таблиці
    if a > b:
        x = a / b + 31
    elif a == b:
        x = -25
    else:
        x = (a * 5 - 1) / a
    print("Результат X =", x)

def pyramida():
    n = int(input("Введіть найбільшу цифру піраміди N (від 1 до 10): "))
    if n < 1 or n > 10:
        print("Помилка: N має бути від 1 до 10")
        return

    # Цикл для побудови рядків
    for i in range(n):
        # Відступ зліва (i - це кількість пробілів)
        print(" " * i, end="")

        # Друк чисел у поточному рядку
        for j in range(1, n - i + 1):
            print(j, end=" ")
        print()  # Перехід на новий рядок

# Запуск функцій
obchyslennya()
pyramida()