""" Create a NumPy array of 10 random integers between 1 and 100 and compute their mean. """

import numpy as np
numbers = np.random.randint(1, 100, size=10)
mean = np.mean(numbers)
print("10 Random Integers: ", numbers)
print("Mean: ", mean)


