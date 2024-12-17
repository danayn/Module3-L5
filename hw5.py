#Assignments: Python File Handling
'''
1. Exploring Python's OS Module

Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.
Task 1: Directory Inspector:
Problem Statement: Create a Python script that lists all files and subdirectories in a given directory.
Your script should prompt the user for the directory path and then display the contents.
Code Example:
    import os
    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
Handle exceptions for invalid paths or inaccessible directories.
NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks 
the run button at the top, all code executes as intended. For example, if there are if statements, print statements, 
or for loops, they should function correctly and display output in the console as expected. If you have a function, 
make sure the function is called and runs.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

'''
import os

path = str(input("Please Enter the directory path fully then the contents will be displayed: "))
#example_path = "/Users/danielkassaye/Documents/codingtemple-kekambas-142/module3/L5/"

path = path + ""
def list_directory_contents(path):
    # List and print all files and subdirectories in the given path
    d_list = os.listdir(path)
    print("The Files and subdirectories in the'", path, "' directory are:")
    print()
    print(d_list)
    print()

list_directory_contents(path)








        