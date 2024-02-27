def calculate_interest(principal, rate, time):
   
   
    interest = (principal * rate * time) / 100
    
    return interest






principal_amount = float(input("Enter the principal amount: ")) 

interest_rate = float(input("Enter the interest rate (in percentage): "))  

time_period = float(input("Enter the time period (in years): ")) 





simple_interest = calculate_interest(principal_amount, interest_rate, time_period)
print("Simple Interest:", simple_interest)





