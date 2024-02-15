# buy everything
needed_list= ["Apples", "Lettuce", "Bread", "Milk", "Peanut Butter"]

got_it = "ice cream"
while got_it != "purchased":
    # display list
    for item in needed_list:
        print (item)

    got_it = input("\nPlease enter the item that you have gotten from the list:  ")
    if got_it in needed_list:
        needed_list.remove(got_it)

if len(needed_list) == 0:
    print("you are done!")
    got_it = "done"