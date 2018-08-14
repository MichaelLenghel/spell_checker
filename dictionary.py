from levenshtein_algo import lev

class Dictionary:
	def __init__(self, word):
		self.word = word
		self.max_words = 3
		with open('words.txt', 'r') as f:
			f_contents = f.readlines()  # If a very large file, would be better to use a yeild function
			self.find_matches(f_contents)

	def find_matches(self, f_contents):
		# Set the initial min_dis to the distance for first word
		l = lev()

		# List with 5 values, as will return 5 closest words to what the user has entered
		min_dis = [l.edit_distance(self.word, f_contents[0])] * self.max_words
		closest_word = [None] * self.max_words
		dis = 0
	
		for w in f_contents:
			dis = l.edit_distance(self.word, w)

			for i in range(self.max_words):
				if dis < min_dis[i]:		
					min_dis[i] = dis
					closest_word[i] = w
					break
		
		print("Macthes found: ")
		for i, w in enumerate(closest_word):
			print("{}. {}".format(i, w))


			

def main():
	needle = input("Enter a word\n")
	d = Dictionary(needle)


if __name__ == '__main__':
	main()
