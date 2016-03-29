import csv
import string

file_name = "Defective_Line_Container.txt"
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open(file_name, 'r') as myfile:
	characters_as_string = myfile.read()

from collections import Counter
character_counter = Counter(characters_as_string)

with open('counted_characters.csv', 'a', newline = '') as fp:
	a = csv.writer(fp, delimiter = ',')
	data = [["Character Counter"]]
	a.writerows(data)
	for character in ascii_letters:
		data = [character, character_counter[character]],
		a.writerows(data)