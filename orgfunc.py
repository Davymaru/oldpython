def factorial(n):
   


    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)



def main():
  
    user_input = input("Enter a non-negative integer: ")
    
  
    try:
        n = int(user_input)

        if n < 0:
            print("Please enter a non-negative integer.")
            return
        
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
        return
    

    result = factorial(n)


    print(f"The factorial of {n} is {result}.")
   
main()
