# TITLE
# Replace a character in a string

# DESCRIPTION
# Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

# curr_char and new_char are variables that contain strings with a single character.

# You may assume that new_char will not be an empty string.

# The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

# If no match is found, print the initial string.

# EXPECTED OUTPUT
# Input         | curr_char | new_char  | Output
# "Hello"       | "l"       | "s"       | "Hesso"
# "World"       | "W"       | "A"       | "Aorld"
# "Python"      | "P"       | "x"       | "xython"
# "Python"      | "p"       | "a"       | "Python"

input_string = ""
curr_char = ""
new_char = ""
is_exit = False

while not is_exit:
    input_string = input("Enter string: ")

    if input_string == "exit":
        is_exit = True
    else:
        curr_char = input("Enter current character: ")
        new_char = input("Enter new character: ")

        new_string = ""

        for i in input_string:
            if i == curr_char:
                new_string += new_char
            else:
                new_string += i
        print(new_string)
