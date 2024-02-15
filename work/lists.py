from functools import total_ordering

week = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]

week.remove("Sunday")
week.remove("Saturday")
steps= []

for day in week:
    day_steps = int(input(f"How many steps did you take on {day}:  "))
    steps.append(day_steps)

index = 0
for day in week:
    print(f"On {day} you took {steps [index]}")
    index += 1

    average = total / len(steps)
print(f"You walked an average of {average:.1f} steps per day.")