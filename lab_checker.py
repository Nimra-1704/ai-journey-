total_tests = 0
running = True
while running:
    print("---BIOCHEMISTRY LAB CHECKER---")
    print("1. Check Blood Glucose")
    print("2. Check Total Cholesterol")
    print("3. Check Hemoglobin")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "4":
        print("Closing Lab Checker. Have a good day.")
        print(f"You checked {total_tests} patients today.")
        running = False
    elif choice == "1":
        name = input("Enter your name: ")
        glucose = float(input("Enter Glucose (mg/dL): "))
        if glucose > 99:
            print(f"Result for {name}: {glucose} mg/dL is High")
        elif glucose < 70:
            print(f"Result for {name}: {glucose} mg/dL is Low")
        else:
            print(f"Result for {name}: {glucose} mg/dL is Normal")
        total_tests = total_tests + 1
    elif choice == "2":
        name = input("Enter your name: ")
        cholesterol = float(input("Enter Cholesterol (mg/dL): "))
        if cholesterol >= 200:
            print(f"Result for {name}: {cholesterol} mg/dL is High")
        else:
            print(f"Result for {name}: {cholesterol} mg/dL is Normal")
        total_tests = total_tests + 1
    elif choice == "3":
        name = input("Enter your name: ")
        hemoglobin = float(input("Enter Hemoglobin (g/dL): "))
        if hemoglobin > 17.5:
            print(f"Result for {name}: {hemoglobin} g/dL is High")
        elif hemoglobin < 12.0:
            print(f"Result for {name}: {hemoglobin} g/dL is Low")
        else:
            print(f"Result for {name}: {hemoglobin} g/dL is Normal")
        total_tests = total_tests + 1
    else:
        print(f"Invalid choice. Please pick a number from 1 to 4.")
    print("\n")