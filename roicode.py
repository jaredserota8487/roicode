import re
from numbersdict import number_dict

def change_string(sentence):
	words = list(sentence.split())
	for index, word in enumerate(words):
		for key in number_dict:
			for item in number_dict[key]:
				if re.search(item, word, re.IGNORECASE):
					new_word = number_dict[key + 1][0]
					string_size = (len(word)-1) - len(item)
					if len(word) != len(item):
						words[index]= new_word + word[string_size:]
					else:
						words[index]= new_word
					#words.insert(index, word)
	words = map(str, words)
	words = " ".join(words)
	return words

