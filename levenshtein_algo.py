import numpy as np

class lev:
	distance = 0
	@staticmethod
	def min(num1, num2, num3):
		if num1 < num2:
			if num1 < num3:
				return num1
		elif num2 < num3:
			return num2
		else:
			return num3

	def edit_distance(self, needle, haystack):
		rows, cols = len(needle) + 1, len(haystack) + 1;
		# Sets order for 2D matrix
		self.m = np.zeros((rows, cols))
		
		# Initialise edges of array
		index = 0
		for n in range(0, rows):
			self.m[index][0] = index
			index += 1
		index = 0
		for n in range(0, cols):
			self.m[0][index] = index
			index += 1

		# Use levenshtein algorithm to calculate minimum distance between two strings
		# ie if [row - 1] == [col - 1] for strings, set to diagonal, otherwise find min from 3 appropriate matrices
		for row in range(1, rows):
			for col in range(1, cols):
				if needle[row - 1] == haystack[col - 1]:
					self.m[row][col] = self.m[row - 1][col - 1]
				else:
					self.m[row][col] = min(
								self.m[row - 1][col]
								, self.m[row - 1][col - 1]
								, self.m[row][col - 1]
								) + 1
		self.distance = self.m[-1][-1]
		return self.distance

	def __str__(self):
		if self.distance != 0:
			return 'Distance is: {}'.format(self.distance)
		else:
			return "Strings are the same!"


def main():
	l = lev()
	needle = input("Enter first string to be compared\n")
	haystack = input("Enter second string to be compared\n")
	min_dis = l.edit_distance(needle, haystack)
	print(l)




# This allows us to compile it normally
if __name__ == '__main__':
	main()