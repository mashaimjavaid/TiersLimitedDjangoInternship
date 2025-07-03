def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

a = [1, 2, 3, 4]
result = sum_of_numbers(a)
print("The sum is:", result)