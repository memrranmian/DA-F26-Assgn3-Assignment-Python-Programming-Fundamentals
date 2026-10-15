name = input("Enter consumer name: ")
units = float(input("Enter monthly units consumed: "))

if units < 0:
    print("Error: Electricity consumption cannot be negative.")
else:
    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100 * 10) + ((units - 100) * 15)
    else:
        bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

    print(f"\n--- Electricity Bill Summary ---")
    print(f"Consumer Name: {name}")
    print(f"Units Consumed: {units:.1f}")
    print(f"Total Bill: Rs. {bill:.2f}")