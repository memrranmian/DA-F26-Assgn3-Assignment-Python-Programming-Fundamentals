name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
distance = float(input("Enter travel distance (in km): "))

if age < 0:
    print("Error: Age cannot be negative.")
elif distance <= 0:
    print("Error: Travel distance must be strictly positive.")
else:
    if distance <= 5.0:
        base_fare = 50.0
    elif distance <= 15.0:
        base_fare = 100.0
    elif distance <= 30.0:
        base_fare = 180.0
    else:
        base_fare = 250.0

    discount = 0.0
    if age >= 60:
        discount = 0.20 * base_fare

    final_fare = base_fare - discount

    print(f"\n--- Public Transport Ticket: {name} ---")
    print(f"Distance: {distance:.2f} km | Age: {age}")
    print(f"Base Fare: Rs. {base_fare:.2f}")
    print(f"Senior Citizen Discount (20%): Rs. {discount:.2f}")
    print(f"Final Fare Payable: Rs. {final_fare:.2f}")