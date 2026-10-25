message = input("Enter your message: ")
with open("messages.txt", "a") as file:
    file.write(f"\n{message}")
    print("Message saved")