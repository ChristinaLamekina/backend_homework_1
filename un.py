# from math import sqrt


# def add_numbers(xou: int, you: int) -> int:
#     return xou + you


# def calculate_square_root(number: float) -> float:
#     return sqrt(number)


# def calc(your_number: float) -> str:
#     if your_number <= 0:
#         return 'Число должно быть положительным.'
#     square_root = calculate_square_root(your_number)
#     return (
#         f'Мы вычислили квадратный корень из введённого вами числа.\n'
#         f'Это будет: {square_root}'
#     )


# xou = 10
# you = 5

# print('Сумма чисел:', add_numbers(xou, you))

# print(calc(25.5))


from math import sqrt
from typing import Optional


def add_numbers(first_number: float, second_number: float) -> float:
    return first_number + second_number


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return 'Число должно быть положительным.'
    root = calculate_square_root(your_number)
    return (
        'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {root}'
    )


first_number: int = 10
second_number: int = 5


print('Сумма чисел: ', add_numbers(first_number, second_number))

print(calc(25.5))
