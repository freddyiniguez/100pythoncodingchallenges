# TITLE
# Check if a string starts with a prefix

# DESCRIPTION
# Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.
# If it does, print True. Else, print False.
# This test should be case sensitive. For example, "A" should not be equivalent to "a".
# If the length of the prefix is greater than the length of the string, print False.

# EXPECTED OUTPUT
# INPUT         | PREFIX    | OUTPUT
# "Hello"       | "He"      | True
# "Coding"      | "Con"     | False
# "Nora"        | "Circum"  | False    

input_string = ""
input_prefix = ""
is_exit = False

while not is_exit:
    input_string = input("Enter the string: ")

    if input_string == "exit":
        is_exit = True
    else:
        input_prefix = input("Enter the prefix: ")
        if len(input_prefix) > len(input_string):
            print(False)
        else:
            if input_string.startswith(input_prefix):
                print(True)
            else:
                print(False)