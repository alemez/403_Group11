import csv
import string
import os

file_name = "Defective_Line_Container.txt"
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
spread_sheet_file = os.getcwd() + "\counted_characters.csv"
print (spread_sheet_file)

with open(file_name, 'r') as myfile:
	characters_as_string = myfile.read()

from collections import Counter
character_counter = Counter(characters_as_string)

if os.path.isfile(spread_sheet_file):
	os.remove(spread_sheet_file)

iterator = 0
with open(spread_sheet_file, 'a', newline = '') as fp:
	a = csv.writer(fp, delimiter = ',')
	data = [["Character Counter"]]
	a.writerows(data)
	for character in ascii_letters:
		iterator = iterator + character_counter[character]
		data = [character, character_counter[character]],
		a.writerows(data)
	data = ["Total:", iterator],	
	a.writerows(data)