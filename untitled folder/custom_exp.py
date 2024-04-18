# class InvalidInputError(ValueError):
#     # Custom exception implementation
#     print("Naughty naughty! You were not supposed to do that")


# def main():
#     try:
#         value = int(input("Please enter a number between 0 and 9 "))
#         print(f"You entered: {value}")

#     except ValueError:
#         print("Shame")
#     except Exception as e:
#         print(e.__str__)
#         print("You need to input a whole number.")
#         main()
#     else:
#         print("Thank you for entering a valid number.")
#     finally:
#         print("Thank's for playing!")
9.2

# main()

# 7.2, Meri ValueError


class InvalidInputError(Exception):
    def __init__(self, message="Can't you read the directions? LESS than 10."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


def main():
    try:
        # goal - create a custom error for if you get a float when you want an int
        value = int(input("Please enter a number from 0 to 9: "))
        if value > 9:
            raise InvalidInputError()

    except InvalidInputError as e:
        print(f"error: {e}")
    except Exception as e:
        print(f"The exception is: {e}")
        print("Please enter an integer between 0 and 9")
        main()
    else:
        print(f"Thank you, you entered {value}.")
    finally:
        print("Finally!!!")


main()
