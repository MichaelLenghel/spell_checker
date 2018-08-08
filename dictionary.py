from levenshtein_algo import lev

class Dictionary:
	def __init__(self, word):
		self.word = word
		with open('words.txt', 'r') as f:
			f_contents = f.read()  # If a very large file, f.readlines() or f.readline() is far more appropriate
			self.find_matches(f_contents)

	def find_matches(self, f_contents):
		# Set the initial min_dis to the distance for first word
		l = lev()
		min_dis = l.edit_distance(self.word, f_contents[0])
		dis = 0
		closest_word = None
		for w in f_contents:
			dis = l.edit_distance(self.word, w)
			if(dis < min_dis):
				min_dis = dis
				closest_word = w

		print("The minimum word is: {} with a distance of: {}".format(closest_word, min_dis))


			

def main():
	needle = input("Enter a word\n")
	d = Dictionary(needle)


main()
