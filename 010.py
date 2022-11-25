# TITLE
# Check if string contains all letters in the alphabet.

# DESCRIPTION
# Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").

# If it does, print True. Else, print False.

# Before comparing the characters, you should convert the string to lowercase.

# If the string contains spaces, ignore them before finding the result.

# You may assume that the string doesn't contain any other symbols, only spaces (possibly).

# Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'

# EXPECTED OUTPUT
# Input
# "abcdefghijklmnopqrstuvwxyz"                  | True
# "The quick brown fox jumps over the lazy dog" | True
# "Hello"                                       | False

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()

    if input_string == "exit":
        is_exit = True
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        contains_all_letters = True

        for i in alphabet:
            if i not in input_string:
                contains_all_letters = False
                break

        if contains_all_letters:
            print(True)
        else:
            print(False)

