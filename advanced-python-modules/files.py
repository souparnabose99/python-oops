import os
import shutil

f_1 = open("sample.txt", "w+")
f_1.write("Some sample text")
f_1.close()

print(os.getcwd())
print(os.listdir())
print(os.listdir("C:\\Users"))

print(shutil.move("sample.txt", r"F:\Data-Structures-Algorithms\advanced-python-modules\output"))

# File deletion functions:
# os.unlink(path) -> deletes file at the path provided
# os.rmdir(path) -> deletes a folder(folder must be empty) at the path provided
# shutil.rmtree(path) -> removed all files and folders in the path
# install & use send2trash module instead

for folders, sub_folders, files in os.walk(r"F:\Data-Structures-Algorithms\advanced-python-modules"):
    print("Current folder : ", folders)
    for sub in sub_folders:
        print("\tSub folder : ", sub)
    for f in files:
        print("\t\tFile : ", f)

# ----- @TODO Console Output -----

# F:\Data-Structures-Algorithms\advanced-python-modules
# ['collections_module.py', 'datetime_module.py', 'files.py', 'math_and_rand.py', 'sample.txt', '__pycache__']
# ['All Users', 'Default', 'Default User', 'desktop.ini', 'Public', 'S.Bose']
# F:\Data-Structures-Algorithms\advanced-python-modules\output\sample.txt
# Current folder :  F:\Data-Structures-Algorithms\advanced-python-modules
# 	Sub folder :  output
# 	Sub folder :  __pycache__
# 		File :  collections_module.py
# 		File :  datetime_module.py
# 		File :  files.py
# 		File :  math_and_rand.py
# Current folder :  F:\Data-Structures-Algorithms\advanced-python-modules\output
# 		File :  sample.txt
# Current folder :  F:\Data-Structures-Algorithms\advanced-python-modules\__pycache__
# 		File :  collections_module.cpython-310.pyc
