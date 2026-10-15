child_count = 0
adult_count = 0
senior_count = 0

total_revenue = 0.0

print("--- Cinema Box Office System ---")
while True:
    entry = input("Enter customer age (or 'done' to finish sales): ").strip()
    if entry.lower() == "done":
        break

    age = int(entry)
    if age < 0:
        print("Error: Age cannot be negative.")
        continue

    if age < 12:
        price = 300.0
        child_count += 1
    elif age <= 59:
        price = 600.0
        adult_count += 1
    else:
        price = 400.0
        senior_count += 1

    total_revenue += price

total_tickets = child_count + adult_count + senior_count

print(f"\n========== CINEMA SCREENING REVENUE REPORT ==========")
print(f"Child Tickets Sold (< 12): {child_count} (Rs. {child_count * 300:.2f})")
print(f"Adult Tickets Sold (12-59): {adult_count} (Rs. {adult_count * 600:.2f})")
print(f"Senior Tickets Sold (60+): {senior_count} (Rs. {senior_count * 400:.2f})")
print(f"Total Tickets Sold: {total_tickets}")
print(f"Total Revenue Generated: Rs. {total_revenue:.2f}")

if total_tickets > 0:
    avg_price = total_revenue / total_tickets
    print(f"Average Ticket Price: Rs. {avg_price:.2f}")
else:
    print("Average Ticket Price: N/A (No tickets sold)")
print(f"====================================================")