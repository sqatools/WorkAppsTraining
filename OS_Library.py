import os, shutil, sys

# Get current working directory

cur_dir = os.getcwd()
print(cur_dir)

# Get list of files and folder in target

#data_list = os.listdir("E:\\Filesdata")
#print(data_list)

# Create directory on target location

#os.mkdir("E:\\Filesdata\\SeleniumTraining")

#os.mkdir("Newfolder")

# Remove directory
#os.removedirs("Newfolder")
#os.removedirs("E:\\Filesdata\\SeleniumTraining")
"""
# Join two path
tar_path = "E:\\Filesdata"
filename = "Bi12"

file_path = os.path.join(tar_path, filename)
print(file_path)

output1 = True if os.path.isfile(file_path) else False
print("file :", output1)

output2 = True if os.path.isdir(file_path) else False
print("directory :", output2)
"""

# write a program to get list of files and folder

tar_path = "E:\\Filesdata"
data_list = os.listdir(tar_path)

file_list= []
folder_list = []
for data in data_list:
    print(data)
    data_path = os.path.join(tar_path, data)
    print(data_path)
    if os.path.isfile(data_path):
        file_list.append(data)
    elif os.path.isdir(data_path):
        folder_list.append(data)

print("Folder list:", folder_list)
print("File list:", file_list)



# Execute windows command
#os.system("control")

#os.system("dir")

#os.system("appwiz.cpl")

#os.system("python E:\\Trainings\\PythonSeleniumWorkApp14Nov2022\\OOPS_Concept\\first_program.py")

#print(os.path.isfile("E:\\Filesdata\\count_name.txt"))

