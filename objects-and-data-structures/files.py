
# Python uses file objects to interact with external files on computer -> like audio, text, emails/excel docs
# Need to install certain libraries & modules, to interact with those various file types

# Opening a file
# file_1 = open("sample.txt")  # Will throw error if file is not located on the same directory as the python script
# FileNotFoundError: [Errno 2] No such file or directory: 'sample.txt'
file_2 = open(r"F:\Data-Structures-Algorithms\Input\sample_2.txt")
print(file_2)
print(file_2.read())
print(file_2.read())  # During this time it will print empty as cursor is already at the end of file
file_2.seek(0)
print(file_2.read())

file_2.seek(0)
print(file_2.readlines())
# Use caution with large files for readlines() method, since everything will be held in memory
file_2.close()

# Writing to a file, w stands for write & w+ means read + write

file_3 = open(r"F:\Data-Structures-Algorithms\Input\sample_2.txt", "w+")
print(file_3.readlines())
file_3.close()
# Note: Opening a file with 'w' or 'w+' truncates the original
# Meaning that anything that was in the original file is deleted!

# Appending to file
file_4 = open(r"F:\Data-Structures-Algorithms\Input\sample.txt", "a+")
file_4.write("\nThis is another line")
file_4.seek(0)
print(file_4.readlines())

# Iterating through a file
for line in open(r"F:\Data-Structures-Algorithms\Input\sample.txt", "r"):
    print(line)
# By not calling .read() on the file, the whole text file was not stored in memory

# ----- @TODO Console Output -----

# <_io.TextIOWrapper name='F:\\Data-Structures-Algorithms\\Input\\sample_2.txt' mode='r' encoding='cp1252'>
# This is a sample python file
# This is line 2
#
# This is a sample python file
# This is line 2
# ['This is a sample python file\n', 'This is line 2']
# []
# ['This is a sample python file\n', 'This is line 2\n', 'This is another line']
# This is a sample python file
#
# This is line 2
#
# This is another line

