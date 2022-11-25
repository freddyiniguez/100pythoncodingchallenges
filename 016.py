# TITLE
# Sort words in alphabetical order

# DESCRIPTION
# Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.
# You may assume that the string only contains letters and spaces to separate the words.
# Spaces should be preserved in the final string.

# EXPECTED OUTPUT
# INPUT             | OUTPUT
# "Hello World"     | "ehllo dlorw"
# "Wonderful World" | "deflnoruw dlorw"

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()

    if input_string == "exit":
        is_exit = True
    else:
        splitted_string = input_string.split(" ")
        new_string = ""

        for word in splitted_string:
            new_word = word.lower()
            new_word = sorted(new_word)
            new_string += "".join(new_word) + " "

        print(new_string)
