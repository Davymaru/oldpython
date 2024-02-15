# Initialize an empty list to store daily blood sugar levels
days = []

# Define the times of day when blood sugar levels will be checked
test_times = ["Breakfast", "Lunch", "Dinner", "Bedtime"]

# Loop through 3 days to collect blood sugar levels
for i in range(3):
    # Initialize an empty list to store blood sugar levels for one day
    sugars = []
    # Loop through each test time in a day
    for time in test_times:
        # Prompt the user to enter their blood sugar level for the current time and convert it to an integer
        level = int(input(f"Enter your blood sugar level for {time}: "))
        # Append the time and the entered blood sugar level as a sublist to the sugars list
        sugars.append([time, level])

    # Print the list of blood sugar levels for the current day
    print(sugars)
    # Add the daily sugars list to the days list, storing all data collected so far
    days.append(sugars)

# Commented out code to print the entire 'days' list - remove the '#' to enable
# print(days)

# Loop through the 'days' list to print blood sugar levels for each day
for i in range(len(days)):
    print(f"Day {i+1}:  ")
    # Loop through the 4 test times to print each time and its corresponding blood sugar level
    for c in range(4): # There are 4 test times
        print(days[i][c])

# Initialize a variable to sum up the blood sugar levels
total = 0

# Loop through the last day's blood sugar levels to calculate the total
for sugar in sugars:
    total += sugar[1] # Add the blood sugar level (second element of each sublist) to the total

# The code to calculate and print the average blood sugar level is commented out - remove the '#' to enable
# average = round(total / len(sugars))
# print("Your average blood sugar level is ", average)
