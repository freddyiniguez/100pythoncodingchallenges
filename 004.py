# TITLE
# First and last three characters of a string

# DESCRIPTION
# Write a Python program that prints the first and last three characters of the string s as a single string.

# If the string has less than six characters, print an empty string (blank output).

# EXPECTED OUTPUT
# Input         | Output
# "Blue"        | ""
# "Wonderful"   | "Wonful"
# "Amazing"     | "Amaing"

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()

    if input_string == "exit":
        is_exit = True
    else:
        if len(input_string) < 6:
            print("")
        else:
            print(input_string[0:3]+input_string[-3:])
