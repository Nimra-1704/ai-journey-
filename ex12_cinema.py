age = int(input("Enter your age:"))
student = input("Are you a student?")
tuesday = input("Is it a Tuesday?")
if age <= 12: 
    baseprice = 500
elif age >= 60:
    baseprice = 600
else:
    baseprice = 1000
if student == "yes" and age < 60:
    baseprice = baseprice - 200
if tuesday == "yes":
    baseprice = baseprice - 100
print(f"Customer Age: {age}")
print(f"Final Ticket Price: {baseprice} Rupees")