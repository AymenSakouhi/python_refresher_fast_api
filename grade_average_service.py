"""Grade average service func"""

from functools import reduce


def calculate_homework(homework_dict):
    """Using reduce to sum the homework grades"""
    total = reduce(lambda acc, val: acc + val, homework_dict.values())
    total /= len(homework_dict)
    print(round(total, 1))
