customer_name = input("Enter customer name: ")
subtotal = 0.0
total_items = 0

while True:
    item_name = input("Enter product name (or 'finish' to proceed to billing): ").strip()
    if item_name.lower() == "finish":
        break

    price = float(input(f"Enter price for '{item_name}': Rs. "))
    qty = int(input(f"Enter quantity for '{item_name}': "))

    if price < 0 or qty <= 0:
        print("Invalid input: Price cannot be negative and quantity must be at least 1. Item skipped.")
        continue

    subtotal += price * qty
    total_items += qty

discount_rate = 0.0
if subtotal >= 5000.0:
    discount_rate = 0.10
elif subtotal >= 2000.0:
    discount_rate = 0.05

discount_amount = subtotal * discount_rate
final_bill = subtotal - discount_amount

print(f"\n========== CHECKOUT SUMMARY ==========")
print(f"Customer Name: {customer_name}")
print(f"Total Quantity Purchased: {total_items}")
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Discount Rate Applied: {int(discount_rate * 100)}%")
print(f"Discount Amount: Rs. {discount_amount:.2f}")
print(f"Final Bill: Rs. {final_bill:.2f}")
print(f"======================================")