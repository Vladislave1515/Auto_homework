import math


def square(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Аргумент должен быть числом")
    return math.ceil(side * side)


side_square = int(input("Введите введите сторону квадрата: "))
print(f"Площадь квадрата = {square(side_square)}")
