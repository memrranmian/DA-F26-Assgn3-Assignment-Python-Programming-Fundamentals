name = input("Enter student name: ")
table_num = int(input("Enter multiplication table number: "))
num_questions = int(input("Enter number of questions: "))

if table_num <= 0 or num_questions <= 0:
    print("Error: Table number and number of questions must be positive integers.")
else:
    correct_count = 0
    incorrect_count = 0

    print(f"\nStarting Table {table_num} Practice for {name}!\n")

    for i in range(1, num_questions + 1):
        expected = table_num * i
        ans = int(input(f"Q{i}: What is {table_num} x {i}? "))

        if ans == expected:
            print("Correct! Good job.")
            correct_count += 1
        else:
            print(f"Incorrect. The correct answer is {expected}.")
            incorrect_count += 1

    score_pct = (correct_count / num_questions) * 100

    print(f"\n--- Performance Report for {name} ---")
    print(f"Total Questions: {num_questions}")
    print(f"Correct Answers: {correct_count}")
    print(f"Incorrect Answers: {incorrect_count}")
    print(f"Final Score: {score_pct:.2f}%")

    if score_pct == 100.0:
        print("Performance Rating: Outstanding! Perfect mastery.")
    elif score_pct >= 80.0:
        print("Performance Rating: Great work! Very strong skills.")
    elif score_pct >= 50.0:
        print("Performance Rating: Passed, but regular practice is recommended.")
    else:
        print("Performance Rating: Needs improvement. Please review this table.")