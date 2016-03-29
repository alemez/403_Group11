import os
import os.path

git_project_txt = "git_urls.txt"
with open(git_project_txt, 'r') as myfile:
	data = myfile.read()

print (data)
projectURLs = data.split("\n")

for projectURL in projectURLs:
	print (projectURL)

	project_clone ="git clone " + projectURL
	project_split = projectURL.split("/")
	project_folder = project_split[len(project_split) - 1]

	if not os.path.isdir(os.path.join(os.getcwd(), project_folder)):
		os.system(project_clone)

	#Appears as though all of the java files are found through the below 3 lines of code
	for dirpath, dirnames, filenames in os.walk("."):
		for filename in [f for f in filenames if f.endswith(".java")]:
			print (os.path.join(dirpath, filename))

