import json
try:
    with open ("student.json", "r") as file:
        gradebook = json.load(file)
except FileNotFoundError:
    gradebook = []
running = True
while running:
    print("---Student Grade Book---")
    print("1. Add a Student")
    print("2. View All Students")
    print("3. Exit")
    choice = input("Choose from 1 to 3: ")
    if choice == "1":
        name = input("Enter student's name: ")
        score = int(input("Enter student's score: "))
        student = {"name": name, "score": score}
        gradebook.append(student)
        with open("student.json", "w") as file:
            json.dump(gradebook, file)
        print(f"Student {name} added.")
    elif choice == "2":
        if len(gradebook) == 0:
            print(f"No students in the book yet.")
        else:
            for student in gradebook:
                if student["score"] >= 50:
                    print(f"{student['name']} scored {student['score']}. Status: PASS")
                else:
                    print(f"{student['name']} scored {student['score']}. Status: FAIL")
    elif choice == "3":
        print("Closing Grade Book.")
        running = False
    else:
        print("Invalid choice.")