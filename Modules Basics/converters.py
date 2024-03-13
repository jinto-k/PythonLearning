"""
This is a module that is used in IntroToModules
"""

def lb_to_kilo(weight):
    return weight * 0.45


def kilo_to_lb(weight):
    return weight / 0.45


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum
