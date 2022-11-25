# TITLE
# Remove spaces from string

# DESCRIPTON
# Write a Python program that prints a copy of the string s without any spaces.
# Words should be connected in the final string.
# If the string doesn't contain spaces, print it intact.

# EXPECTED OUTPUT
# INPUT                 | OUTPUT
# "Hello, World!"       | "HelloWorld!"
# "Have a great day"    | "Haveagreatday"
# "Python"              | "Python"

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()

    if input_string == "exit":
        is_exit = True
    else:
        if " " not in input_string:
            print(input_string)
        else:
            print(input_string.replace(" ", ""))
