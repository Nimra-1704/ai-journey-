waiting_room = []
running = True
while running:
    print("---HOSPITAL TRIAGE SYSTEM---")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Exit")
    choice = input("Choose from above options (1-3): ")
    if choice == "1":
        name = input("Enter Patient's name: ")
        severity = int(input("Enter severity score: "))
        patient = {"name": name, "severity": severity}
        waiting_room.append(patient)
        print(f"Patient {name} added to the waiting room.")
    elif choice == "2":
        if len(waiting_room) == 0:
            print("The waiting room is empty.")
        else:
            for patient in waiting_room:
                if patient["severity"] >= 8:
                    print(f"{patient['name']} - Severity: {patient['severity']} (CRITICAL)")
                elif patient["severity"] >= 4 and patient["severity"] <= 7:
                    print(f"{patient['name']} - Severity: {patient['severity']} (URGENT)")
                elif patient["severity"] <= 3:
                    print(f"{patient['name']} - Severity: {patient['severity']} (STABLE)")
    elif choice == "3":
        print("Closing system.")
        running = False
    else:
        print("Invalid choice.")