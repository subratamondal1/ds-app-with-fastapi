"""Generators"""

import random

# Create Random Numbers
random_number_list = [random.randint(0, 11) for i in range(10)]
even_generator = (number for number in random_number_list if number % 2 == 0)
print(even_generator)
print(list(even_generator))
print(
    list(even_generator)
)  # This will be empty, because generators can only be used once


def generate_even_numbers(max):
    for i in range(0, max + 1):
        if i % 2 == 0:
            yield i
    print("Generator Exhausted Outer")


even = list(generate_even_numbers(10))
print(even)
