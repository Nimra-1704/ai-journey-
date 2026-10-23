name = input("Enter your name: ")
hours = float(input("How many hours have you used the computer? "))
member = input("Have you purchased the membership: ")
cost = hours * 150
tax = cost + 50
total = tax
if member == "yes":
    total = total - 100
if total < 200:
    total = 200
print(f"Customer: {name}")
print(f" Total Bill: {total} Rupees ")