num_employees = int(input("Enter number of employees in report: "))

if num_employees < 0:
    print("Error: Number of employees cannot be negative.")
elif num_employees == 0:
    print("Zero-employee report safely processed. No sales data to display.")
else:
    total_sales = 0.0
    target_achievers = 0

    max_sales = -1.0
    top_employee = ""
    is_tied = False
    employee_summary_string = ""

    for i in range(1, num_employees + 1):
        emp_name = input(f"\nEnter name for employee {i}: ")
        sales = float(input(f"Enter total sales for {emp_name} (Rs.): "))

        while sales < 0:
            print("Sales cannot be negative. Please enter a valid non-negative amount.")
            sales = float(input(f"Enter total sales for {emp_name} (Rs.): "))

        total_sales += sales
        employee_summary_string += f"- {emp_name}: Rs. {sales:.2f}\n"

        if sales >= 10000.0:
            target_achievers += 1

        if i == 1:
            max_sales = sales
            top_employee = emp_name
            is_tied = False
        else:
            if sales > max_sales:
                max_sales = sales
                top_employee = emp_name
                is_tied = False
            elif sales == max_sales:
                is_tied = True

    avg_sales = total_sales / num_employees

    print(f"\n================ SALES DASHBOARD REPORT ================")
    print("Employee Sales Breakdown:")
    print(employee_summary_string.strip())
    print("-------------------------------------------------------")
    print(f"Total Shop Sales: Rs. {total_sales:.2f}")
    print(f"Average Sales Per Employee: Rs. {avg_sales:.2f}")
    print(f"Employees Achieving Target (>= Rs. 10,000): {target_achievers}")

    if is_tied:
        print(f"Top Performer: Tied for highest sales of Rs. {max_sales:.2f}")
    else:
        print(f"Top Performer: {top_employee} with Rs. {max_sales:.2f}")
    print(f"=======================================================")