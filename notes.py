'''
This is a note for Module 3 of Python Intermediate. 
This is a Multi-line String comment. 

Lesson :4 Python File Handling

# There are four collection data types in the Python programming language: List, Tuple, Set, and Dictionary.

https://www.w3schools.com/python/python_file_handling.asp

https://www.tutorialspoint.com/python/file_seek.htm



'''
import os
# File handling is an important part of any web application.

# Python has several functions for creating, reading, updating, and deleting files.

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.write("  Hi Daniel")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

f = open("demofile3.txt", "r")
print(f.read())