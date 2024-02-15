gradepercent = int(input("\nEnter your grade: "))





lettergrade = "x"

if gradepercent >= 90:
    lettergrade = "A"
elif gradepercent >= 80:
    lettergrade = "B"
elif gradepercent >= 70:
    lettergrade = "C"
elif gradepercent >= 60:
    lettergrade = "D"
elif gradepercent < 60:
    lettergrade = "F"


print("You got a", lettergrade)