# TITLE
# Check if a string ends with a suffix

# DESCRIPTION
# Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.
# If it does, print True. Else, print False.
# This test should be case sensitive. Therefore, "A" should not be equivalent to "a".
# If the length of the suffix is greater than the length of the string, print False.

# EXPECTED OUTPUT
# INPUT         | SUFFIX    | OUTPUT
# "Hello"       | "ello"    | True
# "Coding"      | "eng"     | False
# "Nora"        | "rowing"  | False

input_string = ""
input_suffix = ""
is_exit = False

while not is_exit:
    input_string = input("Enter the string: ")

    if input_string == "exit":
        is_exit = True
    else:
        input_suffix = input("Enter the suffix: ")

        if len(input_suffix) > len(input_string):
            print(False)
        else:
            if input_string.endswith(input_suffix):
                print(True)
            else:
                print(False)
