student_name = input("Enter student name: ")
book_title = input("Enter book title: ")
days_late = int(input("Enter number of days late: "))

if days_late < 0:
    print("Error: Number of days late cannot be negative.")
elif days_late == 0:
    print(f"\nBook Title: {book_title}")
    print(f"Student: {student_name}")
    print("Days Late: 0")
    print("No fine is due. Book returned on time!")
else:
    if days_late <= 5:
        total_fine = days_late * 10
    elif days_late <= 10:
        total_fine = (5 * 10) + ((days_late - 5) * 20)
    else:
        total_fine = (5 * 10) + (5 * 20) + ((days_late - 10) * 50)

    print(f"\n--- Library Fine Statement ---")
    print(f"Student: {student_name}")
    print(f"Book Title: {book_title}")
    print(f"Days Late: {days_late}")
    print(f"Total Fine Incurred: Rs. {total_fine}")