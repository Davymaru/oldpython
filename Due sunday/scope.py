POUNDS_TO_KG = 0.453592

INCHES_TO_METERS = 0.0254



def calculate_bmi(weight, height):


    return weight / (height ** 2)



def get_user_input(prompt):

    while True:
        try:
            user_input = float(input(prompt))
            if user_input <= 0:
                print("enter a positive value.")
                continue
            return user_input
        except ValueError:
            print("enter a valid numerical value.")



def bmi_category(bmi):



    if bmi < 18.5:
        return 
    elif 18.5 <= bmi < 25:
        return
    elif 25 <= bmi < 30:
        return 
    else:
        return 


def main():



    weight_lbs = get_user_input("Enter your weight in pounds: ")

    height_inches = get_user_input("Enter your height in inches: ")

    weight_kg = weight_lbs * POUNDS_TO_KG

    height_m = height_inches * INCHES_TO_METERS

    bmi = calculate_bmi(weight_kg, height_m)

    category = bmi_category(bmi)

    print(f"Your BMI is: {bmi:.2f}")

    print(f"You are categorized as: {category}")

main()
