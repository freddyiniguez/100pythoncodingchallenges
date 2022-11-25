# TITLE
# Change commas by dots

# DESCRIPTION
# Write a Python program that prints a version of the string s with all commas replaced by dots.

# EXPECTED OUTPUT
# Input             | Output
# "Hello, World!"   | "Hello. World!"
# "3,456,344"       | "3.456.344"

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()

    if input_string == "exit":
        is_exit = True
    else:
        print(input_string.replace(",", "."))
