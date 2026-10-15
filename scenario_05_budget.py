name = input("Enter student name: ")
allowance = float(input("Enter monthly allowance (Rs.): "))

if allowance < 0:
    print("Error: Monthly allowance cannot be negative.")
else:
    food = float(input("Enter food expenses (Rs.): "))
    transport = float(input("Enter transport expenses (Rs.): "))
    internet = float(input("Enter internet expenses (Rs.): "))
    books = float(input("Enter book expenses (Rs.): "))
    personal = float(input("Enter other personal expenses (Rs.): "))

    if food < 0 or transport < 0 or internet < 0 or books < 0 or personal < 0:
        print("Error: Expense values cannot be negative.")
    else:
        total_exp = food + transport + internet + books + personal
        remaining = allowance - total_exp

        print(f"\n--- Monthly Budget Summary for {name} ---")
        print(f"Monthly Allowance: Rs. {allowance:.2f}")
        print(f"Total Expenditure: Rs. {total_exp:.2f}")
        print(f"Remaining Balance: Rs. {remaining:.2f}")

        if allowance > 0:
            spent_pct = (total_exp / allowance) * 100
            print(f"Percentage of Allowance Spent: {spent_pct:.2f}%")
            if spent_pct > 80.0:
                print("WARNING: You have spent more than 80% of your allowance!")
        else:
            print("Allowance is Rs. 0.00. Percentage calculation skipped.")

        if total_exp < allowance:
            print("Financial Status: Within Budget")
        elif total_exp == allowance:
            print("Financial Status: Budget Exhausted")
        else:
            print("Financial Status: Overspending")