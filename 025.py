# TITLE
# Find the intersection of two sets

# DESCRIPTION
# Write a Python program that finds the intersection of two sets (set1 and set2).
# Create a new set called intersection with their intersection.
# Print the new set as the output.
# If the intersection is empty, print an empty set.

# EXPECTED OUTPUT
# SET1          | SET2          | OUTPUT
# {1, 2, 3}     | {4, 5, 6}     | {}
# {1, 2, 3}     | {3, 4, 5}     | {3}
# {1, 2, 3, 4}  | {3, 4, 5, 6}  | {3, 4}
# {1, 2, 3, 4}  | {1, 2, 3, 4}  | {1, 2, 3, 4}

set1 = {1, 2, 3}
set2 = {4, 5, 6}

# set1 = {1, 2, 3}
# set2 = {3, 4, 5} 

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 3, 4}

new_set = set1.intersection(set2)
print(new_set)
