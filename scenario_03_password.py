while True:
    pwd = input("Enter a proposed password (or type 'STOP' to exit): ")
    if pwd == "STOP":
        print("Password check terminated by user.")
        break

    has_len = len(pwd) >= 8
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in pwd:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    print("\n--- Password Requirement Evaluation ---")
    print(f"At least 8 characters: {'Satisfied' if has_len else 'Missing'}")
    print(f"At least one uppercase letter: {'Satisfied' if has_upper else 'Missing'}")
    print(f"At least one lowercase letter: {'Satisfied' if has_lower else 'Missing'}")
    print(f"At least one digit: {'Satisfied' if has_digit else 'Missing'}")

    if has_len and has_upper and has_lower and has_digit:
        print("Status: ACCEPTABLE. Meets all security rules.\n")
        break
    else:
        print("Status: UNACCEPTABLE. Please review missing rules and try again.\n")