# DESCRIPTION
# Write a Python program that prints the lenght of a string.

# EXPECTED OUTPUT
# INPUT         | OUTPUT
# ""            | 0
# "H"           | 1
# "Hello"       | 5
# "Amazing"     | 7

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()
    if input_string == "exit":
        is_exit = True
    else:
        print(len(input_string))
