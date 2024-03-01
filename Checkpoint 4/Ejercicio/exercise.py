# Exercise 1

list = [1, 2, 3, 4, 5]

print(list)

tuple = (6, 7, 8, 9, 10)

print(tuple)

float_number = 3.14

print(float_number)

integer = 42

print(integer)

from decimal import Decimal
decimal = Decimal('3.14159')

print(decimal)

dictionary = {'first': 7, 'second': 1, 'third': 4}

print(dictionary)

# Exercise 2

import math

round_up = math.ceil(float_number)

print(round_up)

# Exercise 3

square_number = math.sqrt(float_number)

print(square_number)

# Exercise 4

first_dictionary_element = next(iter(dictionary.items()))

print(first_dictionary_element)

# Exercise 5

second_tuple_element = tuple[1]

print(second_tuple_element)

# Exercise 6

new_list_element = 6

list += [new_list_element]

print(list)

# Exercise 7

new_first_element = 0

list[0] = new_first_element

print(list)

# Exercise 8

sort_list = sorted(list)

print(sort_list)

# Exercise 9

new_tuple_element = 11

new_tuple = tuple + (new_tuple_element,)

print(new_tuple)