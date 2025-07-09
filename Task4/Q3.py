""" Implement a generator function that yields the first 10 Fibonacci numbers. """
def generator_fibonacci_numbers():
    a, b = 0, 1
    count = 0
    while count < 10:
        yield a
        a, b = b, a + b
        count += 1

for num in generator_fibonacci_numbers():
    print(num)