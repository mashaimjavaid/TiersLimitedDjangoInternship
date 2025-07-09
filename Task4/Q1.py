""" Write a Python script to read a text file line by line and print each line to the console. """

file_path = 'textfile.txt'
try:
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print("An error occurred:", e)
