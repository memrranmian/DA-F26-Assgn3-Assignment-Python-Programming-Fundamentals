name = input("Enter applicant name: ")
inter_obtained = float(input("Enter intermediate marks obtained: "))
inter_total = float(input("Enter intermediate total marks: "))
test_obtained = float(input("Enter entry-test score obtained: "))
test_total = float(input("Enter entry-test total marks: "))

if inter_total <= 0 or test_total <= 0:
    print("Total marks must be greater than zero.")
elif inter_obtained < 0 or inter_obtained > inter_total:
    print("Invalid intermediate marks: obtained marks must be between 0 and total marks.")
elif test_obtained < 0 or test_obtained > test_total:
    print("Invalid entry-test marks: obtained score must be between 0 and total marks.")
else:
    inter_pct = (inter_obtained / inter_total) * 100
    test_pct = (test_obtained / test_total) * 100

    print(f"\n--- Admission Evaluation for {name} ---")
    print(f"Intermediate Percentage: {inter_pct:.2f}%")
    print(f"Entry-Test Percentage: {test_pct:.2f}%")

    if inter_pct >= 60.0 and test_pct >= 50.0:
        print("Preliminary Result: ELIGIBLE")
    else:
        print("Preliminary Result: NOT ELIGIBLE")
        if inter_pct < 60.0 and test_pct < 50.0:
            print("Reason: Failed both Intermediate (required >= 60%) and Entry-Test (required >= 50%) criteria.")
        elif inter_pct < 60.0:
            print("Reason: Failed Intermediate criteria (required >= 60%).")
        else:
            print("Reason: Failed Entry-Test criteria (required >= 50%).")