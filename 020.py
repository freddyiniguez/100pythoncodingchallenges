# TITLE
# Check if list is empty or not

# DESCRIPTION
# Write a Python program that checks if a list is empty or not.
# If the list is empty, print "Empty". Else, print "Not Empty".

# EXPECTED OUTPUT
# LIST          | OUTPUT
# []            | "Empty"
# [4]           | "Not Empty"
# [4, 5, 6, 7]  | "Not Empty"

input_list = []
# input_list = [4]
# input_list = [4, 5, 6, 7]

print("Empty") if len(input_list) == 0 else print("Not Empty")
