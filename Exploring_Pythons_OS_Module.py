# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

# Task 1: Directory Inspector:

#Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

#Code Example:
import os

    
def list_directory_contents(path):

    try:
        contents = os.listdir(path)
        
        if not contents:
            print("\n The directory is empty. No Treasures found!")
        else:
            print("\n The Grand Archives of", path)
            for item in contents:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    print(f" [Dungeon] {item}/")
                else:
                    print(f" [tome] {item}")
    except FileNotFoundError:
        print("The path you entered does not exist! Perhaps its hidden by an illison spell")
    except PermissionError:
        print("\n You lack the permission to enter the mages vault of magic")
    except Exception as e:
        print(f" AN unknown Error has occured: {e}")
  
if __name__ == "__main__":
    print("\n Welcome, adventurer! You seek the knowledge of the Grand Archives. ")
    directory = input("\nEnter the directory path you wish to explore: ")
    list_directory_contents(directory)

  


# List and print all files and subdirectories in the given path
#Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.
#NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.