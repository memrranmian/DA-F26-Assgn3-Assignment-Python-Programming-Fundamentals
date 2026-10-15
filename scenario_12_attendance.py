name = input("Enter employee name: ")
daily_wage = float(input("Enter daily wage (Rs.): "))

if daily_wage < 0:
    print("Error: Daily wage cannot be negative.")
else:
    present_days = 0
    absent_days = 0

    for day in range(1, 27):
        while True:
            status = input(f"Enter attendance for Day {day} (P/A): ").strip().upper()
            if status == "P":
                present_days += 1
                break
            elif status == "A":
                absent_days += 1
                break
            else:
                print("Invalid input! Please enter only 'P' for Present or 'A' for Absent.")

    salary = present_days * daily_wage
    attendance_pct = (present_days / 26) * 100

    print(f"\n--- Monthly Attendance & Salary Report ---")
    print(f"Employee Name: {name}")
    print(f"Days Present: {present_days} / 26")
    print(f"Days Absent: {absent_days} / 26")
    print(f"Attendance Percentage: {attendance_pct:.2f}%")
    print(f"Total Monthly Salary: Rs. {salary:.2f}")

    if attendance_pct < 80.0:
        print("WARNING: Employee attendance is below 80% threshold!")