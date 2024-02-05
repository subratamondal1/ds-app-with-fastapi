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
