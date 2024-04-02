def main():


    valid = False  

    while not valid:
        valid = True  

        print("""Password Requirements:\n
            Between 8 to 20 characters long.\n
            Contains at least one uppercase letter.\n
            Contains at least one lowercase letter.\n
            Includes at least one number.\n
            Includes at least one symbol from the set: !@#$%&*\n""")

        password = input("Please enter a password that meets the criteria: ")

        length = len(password)



        if 7 < length < 21:
            continue
        else:
            valid = False

            print("That password is not the right length")

        is_upper = False 

        has_symbol = False

        symbol = ['!', '@', '#']

        for s in symbol:

            for c in password:
                if s == c:
                    has_symbol == True
        if has_symbol == False:
            
            print("you need to include a symbol")

            valid = False

            continue
main()








