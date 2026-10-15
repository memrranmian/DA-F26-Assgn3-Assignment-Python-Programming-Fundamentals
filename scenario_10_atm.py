name = input("Enter account holder name: ")
balance = float(input("Enter initial account balance (Rs.): "))

successful_withdrawals = 0
total_withdrawn = 0.0

while True:
    print(f"\nCurrent Balance: Rs. {balance:.2f}")
    choice = input("Enter withdrawal amount (multiple of Rs. 500) or 'exit' to finish: ").strip()

    if choice.lower() == "exit":
        break

    amount = float(choice)

    if amount <= 0:
        print("Transaction Failed: Withdrawal amount must be positive.")
    elif amount % 500 != 0:
        print("Transaction Failed: ATM only dispenses in multiples of Rs. 500.")
    elif amount > balance:
        print("Transaction Failed: Insufficient funds.")
    else:
        balance -= amount
        successful_withdrawals += 1
        total_withdrawn += amount
        print(f"Transaction Successful! Dispensed: Rs. {amount:.2f}")
        print(f"Remaining Balance: Rs. {balance:.2f}")

print("\n========== ATM SESSION SUMMARY ==========")
print(f"Account Holder: {name}")
print(f"Successful Transactions: {successful_withdrawals}")
print(f"Total Cash Withdrawn: Rs. {total_withdrawn:.2f}")
print(f"Final Balance: Rs. {balance:.2f}")
print("=========================================")