test_times = ["Morning", "Mid-day", "Afternoon", "Evening"]
heart_rate = []


for time in test_times:
    bpm = int(input(f"Enter your heart rate in the {time}: "))
    heart_rate.append([time, bpm])




total = 0

for hr in heart_rate:
    total += hr[1]


average = total / len(heart_rate)


print(f"Your average BPM today is {average:.2f} BPM.")














