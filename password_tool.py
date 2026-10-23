import random
letters = ["a", "b", "c", "d", "e", "f"]
numbers = ["1", "2", "3", "4", "5"]
symbols = ["@", "#", "$", "%", "&"]
running = True
while running:
    print("---PASSWORD TOOLKIT---")
    print("1. Generate a Password")
    print("2. Check Password Strength")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        length = int(input("How long do you want the password? "))
        password = ""
        for i in range(length):
            password = password + random.choice(letters + numbers + symbols)
        print(f"Final Password: {password}")
    elif choice == "2":
        password_to_test = input("Enter a password to test: ")
        has_numbers = False
        has_symbols = False
        for char in password_to_test:
            if char in numbers:
                has_numbers = True
            if char in symbols:
                has_symbols = True  
        length = len(password_to_test)
        if length >= 12 and has_numbers and has_symbols:
            print("Very Strong")
        elif length >= 8 and has_numbers:
            print("Strong")
        elif length >= 8:
            print("Medium")
        else:
            print("Weak")