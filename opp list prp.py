seats = ["1E", "2E", "3E", "4E", "5E", "1D", "2D", "3D", "4D", "5D", "1C", "2C", "3C", "4C", "5C", "1B", "2B", "3B", "1A", "2A", "3A"]

seat = ""
while seat != "done":
    print ("\n\nyou can even buy multipul tickes so when you are finshed purching please type '0'\nThe following seats are avaible:")
    for seat in seats:
        print (seat)



    seat = input("\nPlease enter the seats you want: ")
    if seat in seats:
        seats.remove(seat)
    elif seat == '0':
        print("Thank you for your purchase!")
        seat = "done"
    else:
        print("Sorry thats not an avaible seat, please try again!")











