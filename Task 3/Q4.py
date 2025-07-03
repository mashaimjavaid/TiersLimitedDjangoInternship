""" Write a Python program that uses list comprehension to create a new list
containing the squares of all even numbers from 1 to 20. """

numbers = [2,5,8,13,16,19,20,24,27,30]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

