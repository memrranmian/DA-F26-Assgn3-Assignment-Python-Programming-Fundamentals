rows = int(input("Enter number of rows: "))
seats_per_row = int(input("Enter number of seats per row: "))

if rows <= 0 or seats_per_row <= 0:
    print("Error: Rows and seats per row must be positive integers.")
else:
    total_capacity = rows * seats_per_row
    print(f"\n--- Seating Plan (Total Capacity: {total_capacity}) ---")

    seat_num = 1
    for r in range(1, rows + 1):
        row_str = f"Row {r:02d}: "
        for s in range(1, seats_per_row + 1):
            row_str += f"[{seat_num:02d}] "
            seat_num += 1
        print(row_str)

    customers = int(input("\nEnter number of arriving customers: "))
    if customers < 0:
        print("Error: Customer count cannot be negative.")
    elif customers > total_capacity:
        print(f"Error: Customer count ({customers}) exceeds total capacity ({total_capacity}).")
    else:
        unoccupied = total_capacity - customers
        print(f"Reservation Successful: {customers} seated, {unoccupied} unoccupied seats remaining.")