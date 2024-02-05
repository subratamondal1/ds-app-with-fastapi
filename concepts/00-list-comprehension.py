"""List Comprehension"""

import random

# Create Random Numbers
random_number_list = [random.randint(0, 11) for i in range(10)]
print(random_number_list)

# Create even numbers
even_number_list = [number for number in random_number_list if number % 2 == 0]
print(even_number_list)