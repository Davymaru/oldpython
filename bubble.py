print("\nIm going to ask you for five names at once")

names = []

for i in range(0, 5):
    name = input("\nPlease enter a nane: ")
    names.append (name)

    swapped = True

for i in range (0,len(names)):
    names[i] = names[i].lower()



print(names)




while swapped:
    swapped = False  
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True  
            names[i], names[i + 1] = names[i + 1], names[i]

print(names)

names.reverse()


print(names)


