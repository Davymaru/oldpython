from datetime import datetime

def main():

    print("\n\n")
    try:

        today = datetime.today()

        birth_year = int(input("What year were you born?  "))

        month = int(input("What Month were you born (as a number. May would be 5)  "))

        day = int(input("What day of the month were you born?  "))
        
        # creating a datetime object representing users birthday
        birthday = datetime(birth_year, month, day)
        
        # printing the users birthday
        print("Your birthday is: ")

        birthday_output = birthday.strftime("%Y-%m-%d")

        print(birthday_output) 

        # calculating the differences
        delta = today - birthday
        
        # extracting years from the difference in days

        delta_years = delta.days // 365.2425
        # remaining days after calculating years
        remaining_days = delta.days % 365.2425
        # extracting months from the remaining days
        delta_months = remaining_days // 30.41
        # remaining days after calculating months
        remaining_days %= 30.41
        # extracting weeks from the remaining days
        delta_weeks = remaining_days // 7
        # remaining days after calculating weeks
        remaining_days %= 7

        # print
        print(f"You are {int(delta_years)} years, {int(delta_months)} months, {int(delta_weeks)} weeks, and {int(remaining_days)} days old.")

    except Exception as e:

        print(f"ooooops!!!:  {e}") 
        
        main()


main()
