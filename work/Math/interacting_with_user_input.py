print("Budget breakdown calculator")

Housing = float(input("Enter your rent here:"))
utilities = float(input("Enter the fees for utilites here:"))
groceries = float(input("enter groceries here:"))
transportaion = float(input("enter gas amount here"))
health_care = float(input("Health care fees:"))
personal_care = float(input("Enter your personal fees right here:"))
Clothing = float(input("Enter your clothing fee right here:"))
Debt = float(input("enter how much debt youll pay here:"))
total = Housing+utilities+groceries+transportaion+health_care+personal_care+Clothing+Debt

housing_percent = Housing/total*100 
utilities_percent = utilities/total*100
groceries_percent = groceries/total*100
transportation_percent = transportaion/total*100
healthcare_percent = health_care/total*100
personal_percent = personal_care/total*100
clothing_percent = Clothing/total*100
debt_percent = Debt/total*100

print(f"Your house payment is {housing_percent:.2f}% of your total percent")
print(f"Your utilities percent is {utilities_percent:.2f}% of your total percent")
print(f"Your groceries percent are{groceries_percent:.2f}% of your total percent")
print(f"Your transportation percent is {transportation_percent:.2f}% of your total percent")
print(f"Your health care percent is {healthcare_percent:.2f}% of your total percent")
print(f"Your personal care percent is {personal_care:.2f}% of your total percent")
print(f"Your clothing percent is {clothing_percent:.2f}% of your total percent")
print(f"Your debt payments take up {debt_percent:.2f}% of your total percent")
