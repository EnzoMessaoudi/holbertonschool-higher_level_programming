How to open a file
    - In python, we can open file using the open() function. We can choose to open this file with read-only(r) or write-Read(r+).
How to write text in a file
    - We can use write() function. This permits to write inside of text file. We can use "w" or "a" to choose if we want to begin empty or append.
How to read the full content of a file
    - The read() can stock inside of a variable, wich we can print anytime.
How to read a file line by line
    - With the read() function and then looping throught the variable
How to move the cursor in a file
    - The seek() function with the position of the cursor.
How to make sure a file is closed after using it
    - We can use the close() function but it's risky because if an error occurs, it will stay open. We can use `with` instead as: "with open("example.txt", "r") as file:
What is and how to use the with statement
    - We can use the with statement to safely close a file
What is JSON
    - It's a text format that is used to stock and exchange datas. It's stock like dictionnaries in Python but with just text.
What is serialization
    - Convert a Python object in a JSON string. (dict -> str)
What is deserialization
    - Convert a JSON string in a Python object. (str -> dict)
How to convert a Python data structure to a JSON string
    - Using `dumps`, we can convert a dictionnaries in Python to a JSON string and import json. 
How to convert a JSON string to a Python data structure
    - Import json and use `loads` to convert a JSON string to a Python dictionnary.
How to access command line parameters in a Python script
    - Import sys and use sys.argv