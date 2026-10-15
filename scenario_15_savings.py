name = input("Enter student name: ")
goal = float(input("Enter savings goal (Rs.): "))
initial_savings = float(input("Enter initial savings balance (Rs.): "))

if goal <= 0 or initial_savings < 0:
    print("Error: Goal must be positive and initial savings cannot be negative.")
else:
    current_savings = initial_savings
    weeks = 0

    if current_savings >= goal:
        print(f"\nCongratulations {name}! Your initial balance already meets or exceeds your goal.")
        print(f"Total Saved: Rs. {current_savings:.2f} | Goal: Rs. {goal:.2f} in 0 weeks.")
    else:
        while current_savings < goal:
            choice = input(f"Enter amount saved in Week {weeks + 1} (or 'stop' to halt): ").strip()
            if choice.lower() == "stop":
                print("Savings tracking stopped by user.")
                break

            deposit = float(choice)
            if deposit < 0:
                print("Error: Savings deposit cannot be negative. Entry ignored.")
                continue

            weeks += 1
            current_savings += deposit
            remaining = goal - current_savings

            if remaining > 0:
                print(f"Total Saved: Rs. {current_savings:.2f} | Remaining: Rs. {remaining:.2f}")
            else:
                print(f"Total Saved: Rs. {current_savings:.2f} | Goal reached or exceeded by Rs. {abs(remaining):.2f}!")

        print(f"\n--- Final Savings Summary for {name} ---")
        print(f"Goal Amount: Rs. {goal:.2f}")
        print(f"Total Accumulated: Rs. {current_savings:.2f}")
        print(f"Weeks Tracked: {weeks}")
        if current_savings >= goal:
            print("Status: TARGET ACHIEVED! You can buy the laptop.")
        else:
            print(f"Status: TARGET NOT ACHIEVED. Deficit: Rs. {goal - current_savings:.2f}")