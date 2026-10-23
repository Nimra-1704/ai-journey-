total_revenue = 0
total_samples = 0
running = True
while running:
    print("---DIADNOSTIC LAB MANAGER---")
    print("1. Process New Sample")
    print("2. Run Daily Summary")
    print("3. Exit")
    choice = input("Choose the above options (1-3): ")
    if choice == "1":
        name = input("Kindly enter your name: ")
        type = input("Enter sample type: ")
        volume = float(input("Enter sample volume in mL: "))
        cost= 0
        if type == "blood":
            cost = 500
        elif type == "urine":
            cost = 300
        if type == "blood" and volume > 10:
            cost = cost + 200
        if volume < 2:
            print("Error: Sample volume too low. Rejected.")
        else:
            total_revenue = total_revenue + cost
            total_samples = total_samples + 1
            print(f"Sample processed. Cost: {cost} Rupees")
    elif choice == "2":
        for i in range(total_samples):
            print("*")
        print(f"Total Revenue: {total_revenue} ")
        print(f"Total Samples: {total_samples} ")
    elif choice == "3":
        print("Closing system.")
        exit()
    else:
        print("Invalid choice.")