import os
import os.path

def error_prone_line_detector(confidence_interval, c_count, err_prone_chars, err_prone_chars_percentages, total_character_count):
	i = 0
	if (total_number_of_characters != 0):
		for character in err_prone_chars:
			occurrance_rate = character_counter[character]/total_character_count
			if((err_prone_chars_percentages[i] >= occurrance_rate*(1-confidence_interval)) and (err_prone_chars_percentages[i] <= occurrance_rate*(1+confidence_interval))):
				return True
			i = i + 1
	return False		


ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
git_project_txt = "git_urls.txt"
confidence_interval = 0.0025
error_prone_characters = {'n','a','t','e'}
error_prone_characters_percentages = [.0965079365, .0679365079, .0825396825, .1168253968]

with open(git_project_txt, 'r') as myfile:
	data = myfile.read()

projectURLs = data.split("\n")

#Each project must go under the following steps
#	Clone the project
#	Find All java files
#	For each line find the rate of occurrance of characters and compare with
#		expected estimates
#	Store all lines that meet the above requirements
for projectURL in projectURLs:
	print (projectURL)

	project_clone ="git clone " + projectURL
	project_split = projectURL.split("/")
	project_folder = project_split[len(project_split) - 1].split(".")[0]

	if not os.path.isdir(os.path.join(os.getcwd(), project_folder)):
		os.system(project_clone)
count = 0
#Appears as though all of the java files are found through the below 3 lines of code
for dirpath, dirnames, filenames in os.walk("."):
	for filename in [f for f in filenames if f.endswith(".java")]:
		#Open the java file
		java_file = os.path.join(dirpath, filename)
		with open(java_file, encoding="utf8") as java_file_in:
			lines = java_file_in.readlines()
			q = 0
			for line in lines:
				from collections import Counter
				character_counter = Counter(line)
				total_number_of_characters = 0
				for character in ascii_letters:
					total_number_of_characters = total_number_of_characters + character_counter[character]
				if(error_prone_line_detector(confidence_interval, character_counter, error_prone_characters, error_prone_characters_percentages, total_number_of_characters)):
					with open("defective_java_files.txt", "a") as out_file:
						out_file.write(str(count))				
						count = count + 1
						out_file.write(" ")
						out_file.write(os.path.join(dirpath, filename))
						out_file.write(" ")
						out_file.write(str(q))
						out_file.write(" ")
						out_file.write(line)
						out_file.write("\n")
				q = q + 1

				
