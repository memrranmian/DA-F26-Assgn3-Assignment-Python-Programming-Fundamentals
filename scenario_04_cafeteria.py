customer_name = input("Enter customer name: ")
total_subtotal = 0.0

while True:
    print("\n--- Cafeteria Menu ---")
    print("1. Sandwich    - Rs. 250")
    print("2. Burger      - Rs. 400")
    print("3. Pizza slice - Rs. 300")
    print("4. Juice       - Rs. 120")

    choice = input("Select an item (1-4) or 'done' to finish ordering: ").strip().lower()
    if choice == "done":
        break

    price = 0.0
    item_name = ""
    if choice == "1" or choice == "sandwich":
        price = 250.0
        item_name = "Sandwich"
    elif choice == "2" or choice == "burger":
        price = 400.0
        item_name = "Burger"
    elif choice == "3" or choice == "pizza slice" or choice == "pizza":
        price = 300.0
        item_name = "Pizza slice"
    elif choice == "4" or choice == "juice":
        price = 120.0
        item_name = "Juice"
    else:
        print("Invalid menu selection! Please pick a valid item from the menu.")
        continue

    qty_input = input(f"Enter quantity for {item_name}: ")
    qty = int(qty_input)
    if qty <= 0:
        print("Error: Quantity must be greater than zero.")
        continue

    line_cost = price * qty
    total_subtotal += line_cost
    print(f"Added {qty} x {item_name} = Rs. {line_cost:.2f}. Current Subtotal: Rs. {total_subtotal:.2f}")

discount = 0.0
if total_subtotal >= 1000.0:
    discount = 0.10 * total_subtotal

final_bill = total_subtotal - discount

print(f"\n================ RECEIPT ================")
print(f"Customer Name: {customer_name}")
print(f"Cumulative Subtotal: Rs. {total_subtotal:.2f}")
print(f"Discount (10% if >= Rs. 1000): Rs. {discount:.2f}")
print(f"Final Total Payable: Rs. {final_bill:.2f}")
print(f"=========================================")