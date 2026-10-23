name = input("Enter your name: ")
gpa = float(input("Enter your GPA: "))
income = int(input("Enter your family income: "))
record = input("Do you have any disciplinary record? ")
print(f"Student: {name}")
if record == "yes":
    print(f"Status: Denied")
elif gpa >= 3.5 and income < 60000:
    print(f"Status: Full Scholarship")
elif gpa >= 3.0 and income < 80000:
    print(f"Status: Half Scholarship")
else:
    print("Status: No Scholarship")