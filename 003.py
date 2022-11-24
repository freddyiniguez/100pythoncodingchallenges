# TITLE
# Reverse a string

# DESCRIPTION
# Write a Python Program that prints the reversed version of a string.

# The program must preserve uppercase and lowercase letters.

# If the string is empty, print it intact.

# EXPECTED OUTPUT
# Input     | Output
# "Hello"   | olleH
# "Wo"      | oW
# ""        | ""

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()
    
    if input_string == "exit":
        is_exit = True
    else:
        print(input_string[:: -1])
