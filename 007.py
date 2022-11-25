# TITLE
# Remove nth character from a string

# DESCRIPTION
# Write a Python program that prints the string s without the character at index n.

# If the index n is out of range, print the string s intact.

# If the string s is empty, print the string s intact.

# EXPECTED OUTPUT
# Input         | Index | Output
# "Hello"       | 1     | "Hllo"
# "World"       | 3     | "Word"
# "Dog"         | 15    | "Dog"
# ""            | 2     | ""

input_string = ""
input_index = 0
is_exit = False

while not is_exit:
    input_string = input("Enter string: ")

    if input_string == "exit":
        is_exit = True
    else:
        input_index = int(input("Enter index: "))

        if input_index >= len(input_string):
            print(input_string)
        elif len(input_string) == 0:
            print(input_string)
        else:
            new_string = input_string[:input_index] + input_string[input_index + 1:]
            print(new_string)
