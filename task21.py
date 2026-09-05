import math
def pryklad():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c (має бути більше за -1): "))

    if c <= -1:
        print("Помилка: під коренем не може бути від'ємне число")
        return

    y = (abs(a) + abs(b)) / math.sqrt(c + 1)
    print("Результат y =", y)