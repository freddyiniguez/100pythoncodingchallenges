# TITLE
# Remove characters at even indices

# DESCRIPTION
# Write a Python program that prints the string s without the characters located at even indices.

# If the string is empty or only has one character, print it without any changes.

# EXPECTED OUTPUT
# Input         | Output
# "Coding"      | "oig"
# "Pizza"       | "iz"
# "Python"      | "yhn"
# "A"           | "A"
# ""            | ""

input_string = ""
is_exit = False

while not is_exit:
    input_string = input()

    if input_string == "exit":
        is_exit = True
    elif len(input_string) == 1:
        print(input_string)
    else:
        input_without_even_characters = ""
        for i in range(1, len(input_string), 2):
            input_without_even_characters += input_string[i]
        print(input_without_even_characters)
