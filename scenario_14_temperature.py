days = int(input("Enter number of days to monitor: "))

while days <= 0:
    print("Invalid monitoring period. Days must be a positive integer.")
    days = int(input("Enter number of days to monitor: "))

total_temp = 0.0
above_35 = 0
below_10 = 0
between_10_and_35 = 0

highest = 0.0
lowest = 0.0

for day in range(1, days + 1):
    t = float(input(f"Enter temperature for Day {day} (°C): "))
    total_temp += t

    if day == 1:
        highest = t
        lowest = t
    else:
        if t > highest:
            highest = t
        if t < lowest:
            lowest = t

    if t > 35.0:
        above_35 += 1
    elif t < 10.0:
        below_10 += 1
    else:
        between_10_and_35 += 1

avg_temp = total_temp / days

print(f"\n========== TEMPERATURE MONITORING REPORT ==========")
print(f"Monitoring Period: {days} days")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Highest Temperature: {highest:.2f} °C")
print(f"Lowest Temperature: {lowest:.2f} °C")
print(f"Days above 35°C: {above_35}")
print(f"Days below 10°C: {below_10}")
print(f"Days between 10°C and 35°C (inclusive): {between_10_and_35}")
print(f"===================================================")