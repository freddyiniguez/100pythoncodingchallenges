# TITLE
# Reverse words in a string

# DESCRIPTION
# Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.
# Assume that the string only contains letters and spaces are used to separate words.

# EXPECTED OUTPUT
# INPUT                 | OUTPUT
# "Hello World"         | "OLLEh DLROw"
# "Python is Awesome"   | "NOHTYp SI EMOSEWa"

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()

    if input_string == "exit":
        is_exit = True
    else:
        spllited_string = input_string.split(" ")
        new_string = ""

        for word in spllited_string:
            reversed_word = "".join(reversed(word))
            swapped_case = reversed_word.swapcase()
            new_string += swapped_case + " "

        print(new_string)
