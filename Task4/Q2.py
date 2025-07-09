""" Create a custom iterator class that iterates over a list of numbers and returns only the even numbers. """
class evenNumberIterator:
	def __init__(self, number_list):
		self.numbers = number_list
		self.index = 0
	def __iter__(self):
		return self
	def __next__(self):
		while self.index < len(self.numbers):
			current = self.numbers[self.index]
			self.index += 1
			if current % 2 == 0:
				return current
		raise StopIteration

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iterator = evenNumberIterator(num_list)

for val in iterator:
	print(val)