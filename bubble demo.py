# Initialize a list of names
names = ["Bob", "Carol", "Ted", "Alice", "Anna"]

# you should only compare strings of the same case. The numbers behind
# A and a are different.

# change the list to all lower case.

for i in range (0,len(names)):
    names[i]= names[i].lower()

print(names)
# Flag to track if a swap has occurred
swapped = True

# Continue looping until no swaps occur
while swapped:
    swapped = False  # Reset the flag at the start of each iteration
    for i in range(len(names) - 1):
        # Compare adjacent elements
        if names[i] > names[i + 1]:
            swapped = True  # A swap is needed
            # Swap the elements
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list
print(names)

# Reverse the list
names.reverse()

# Print the reversed list
print(names)