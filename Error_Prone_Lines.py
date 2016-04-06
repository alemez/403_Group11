import os
import os.path

def error_prone_line_detector(confidence_interval, c_count, err_prone_chars, err_prone_chars_percentages):
	i = 0
	for character in err_prone_chars:
		occurrance_rate = character_counter[character]
		if((err_prone_chars_percentages[i] >= occurrance_rate*(1-confidence_interval)) and (err_prone_chars_percentages[i] <= occurrance_rate*(1+confidence_interval))):
			return True
		i = i + 1
	return False		



git_project_txt = "git_urls.txt"
confidence_interval = .05
error_prone_characters = {'a','b','c','d'}
error_prone_characters_percentages = [.10,.18,.15,.12]

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
				if(error_prone_line_detector(confidence_interval, character_counter, error_prone_characters, error_prone_characters_percentages)):
					with open("defective_java_files.txt", "a") as out_file:
						out_file.write(os.path.join(dirpath, filename))
						out_file.write(" ")
						out_file.write(q)
						out_file.write("\n")

				#Some sort of comparisson for if the line is to count
				#If there is a line that is flagged increase a counter and flag file as defective
