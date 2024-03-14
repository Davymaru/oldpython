
def main():
    import random
    try:
        target_number = random.randint(1, 100)

        while True:
         

            user_number = int(input("guess a number (between 1 and 100): "))

            difference = abs(user_number - target_number)

            if difference <= 5:
                print("very hot")
            elif difference <= 15:
                print("hot")
            elif difference <= 25:
                print("cool")
            else:
                print("cold")

            if user_number == target_number:
                print("you did it! You guessed the correct number:", target_number)
                break  

    except ValueError:
        print("Please enter a valid number.")


main()
