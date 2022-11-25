# TITLE
# Remove matching elements

# DESCRIPTION
# Write a Python program that removes all occurrences of the element elem_to_remove from a list.
# The output of the program should be the new list with the element removed.
# If the element is not found in the list, print the message "Not Found".
# If the list is empty, print "Empty List".

# EXPECTED OUTPUT
# LIST                  | ELEMENT TO REMOVE | OUTPUT
# [1, 2, 3, 4]          | 2                 | [1, 3, 4]
# [3, 3, 2, 1]          | 3                 | [2, 1]
# ["a", "b", "c", "b"]  | "b"               | ["a", "c"]
# [3, 4, 5, 6]          | 7                 | "Not Found"
# []                    | 0                 | "Empty List"

input_list = [1, 2, 3, 4]
# input_list = [3, 3, 2, 1]
# input_list = ["a", "b", "c", "b"]
# input_list = [3, 4, 5, 6] 
# input_list = []

elem_to_remove = 2
# elem_to_remove = 3
# elem_to_remove = "b"
# elem_to_remove = 7
# elem_to_remove = 0

if len(input_list) == 0:
    print("Empty List")
elif elem_to_remove not in input_list:
    print("Not Found")
else:
    while elem_to_remove in input_list:
        input_list.remove(elem_to_remove)
    print(input_list)
