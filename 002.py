# TITLE
# Print the Character at a Specific Index

# DESCRIPTION
# Write a Python program that prints the character at index i in the string s.

# If the index is out of range, the program should print "i is out of range"

# If the string is empty, the program should print "Empty String"

# EXPECTED OUTPUT
# INPUT         | i     | OUTPUT
# "Hello"       | 2     | "l"
# "Pizza"       | 4     | "a"
# ""            | 3     | "Empty String"
# "World"       | 15    | "i is out of range"

input_string = ""
input_index = 0
is_exit = False

while not is_exit:
    input_string = input("Enter the string: ")

    if input_string == "exit":
        is_exit = True
    else:
        input_index = int(input("Enter the index: "))
        
        if len(input_string) == 0:
            print("Empty String")
        elif input_index >= len(input_string):
            print("i is out of range")
        else:
            print(input_string[input_index])
