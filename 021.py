# TITLE
# Print the elements and their indices

# DESCRIPTION
# Write a Python program that prints the elements of a list followed their corresponding indices.
# Each element and its index must be on the same line separated by a space.
# If the list is empty, print "Empty List".

# EXPECTED OUTPUT
# LIST              | OUTPUT
# [1, 2, 3, 4]      | 1 0
#                   | 2 1
#                   | 3 2
#                   | 4 3
# ["a", "b", "c"]   | "a" 0
#                   | "b" 1
#                   | "c" 2
# []                | "Empty List"

input_list = [1, 2, 3, 4]
# input_list = ["a", "b", "c"]
# input_list = []

if len(input_list) == 0:
    print("Empty List")
else:
    for index, value in enumerate(input_list):
        print(f'{value} {index}')
