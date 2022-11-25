# TITLE
# Print elements on the same line without commas

# DESCRIPTION
# Write a Python program that prints the elements of a list on the same line.
# The elements should be separated only by a space (not by a comma).
# The output should not include the opening and closing square brackets [ ].

# EXPECTED OUTPUT
# List              | Output
# [3, 4, 5, 6]      | 3 4 5 6
# ["a", "b", "c"]   | a b c

input_list = [3, 4, 5, 6]
#input_list = ["a", "b", "c"]

for i in input_list:
    print(i, end=" ")
