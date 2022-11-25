# TITLE
# Remove duplicates from a list

# DESCRIPTION
# Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.
# The original list should be mutated (modified).
# The program must print the final version of the list.

# EXPECTED OUTPUT
# LIST                  | OUTPUT
# [1, 1, 2, 3, 4, 4]    | [1, 2, 3, 4]
# ["a", "a", "b", "a"]  | ["a", "b"]
# [1, 2, 3]             | [1, 2, 3]
# []                    | []

input_list = [1, 1, 2, 3, 4, 4]
# input_list = ["a", "a", "b", "a"]
# input_list = [1, 2, 3]
# input_list = []

if len(input_list) == 0:
    print(input_list)
else:
    new_set = set(input_list)
    input_list = sorted(list(new_set))
    print(input_list)
