import json
try:
    with open("employees.json", "r") as file:
        employees = json.load(file)
except FileNotFoundError:
    employees = []
running = True
while running:
    print("---THE EMPLOYEES DATBASE---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Give Raise")
    print("4. Exit")
    choice = input("Select the options from 1 to 4: ")
    if choice == "1":
        name = input("Enter your name: ")
        salary = float(input("Enter your salary: "))
        employee = {"name": name, "salary": salary}
        employees.append(employee)
        with open("employees.json", "w") as file:
            json.dump(employees, file)
        print("Employee added")
    elif choice == "2":
        if len(employees) == 0:
            print("No employees found")
        else:
            for employee in employees:
                print(f"Name: {employee['name']} | Salary: {employee['salary']}")
    elif choice == "3":
        raisename = input("Enter name of the employee to give raise: ")
        raiseamount = float(input("Enter raise amount: "))
        found = False
        for employee in employees:
            if employee['name'] == raisename:
                newsalary = raiseamount + employee['salary']
                employee['salary'] = newsalary
                print(f"{raisename}'s new salary is {newsalary}.")
                found = True
                break
            
        if found == False:
            print("Employee not found.")
        with open("employees.json", "w") as file:
            json.dump(employees, file)
    elif choice == "4":
        print("Goodbye")
        running = False