def ascii_calculator(word, key_word):
	value = 0
	word, key_word = sorted(word), sorted(key_word)
	for char in word:
		if char in key_word:
			key_word = key_word[1:]
			value += ord(char)
	return value


def read_words():
	with open("/usr/share/dict/words") as f:
		lines = f.read().lower()
		word_list = lines.split('\n')
	return word_list
	

def build_dictionary(input_list):
	word_list = read_words()
	my_dictionary = {}
	for key_word in input_list:
		words = []
		for word in word_list:
			if len(word) == len(key_word) and ascii_calculator(key_word, key_word) == ascii_calculator(word, key_word):
				words.append(word)
		my_dictionary[key_word] = words

	return my_dictionary


if __name__ == "__main__":
	print(build_dictionary(["tefon", "sokik", "niumem", "siconu"]))


