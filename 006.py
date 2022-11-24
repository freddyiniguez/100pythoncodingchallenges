# TITLE
# Check if a string only contains numbers

# DESCRIPTION
# Write a Python program that check if a string only contains numbers.

# If it does, print True. Else, print False.

# EXPECTED OUTPUT
# Input         | Output
# "Hello"       | False
# "4567"        | True
# "Hello59"     | False
# ""            | False

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()

    if input_string == "exit":
        is_exit = True
    else:
        print(input_string.isdigit())
