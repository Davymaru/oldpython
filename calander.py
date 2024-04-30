import calendar

from datetime import datetime

def main():

    current_year = datetime.now().year


    while True:

        try:

            birth_month = int(input("enter your birth month (1-12): "))

            if 1 <= birth_month <= 12:

                break

            else:

                print("enter a number between 1 and 12.")

        except ValueError:

            print("enter a valid integer.")


    print("\ncalendar for your birth month:")

    cal = calendar.month(current_year, birth_month)

    print(cal)


main()