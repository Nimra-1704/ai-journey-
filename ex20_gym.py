total_revenue = 0
member_count = 1
while member_count < 4:
    name = input("Enter your name: ")
    plan = input("Which plan you want to take? ")
    trainer = input("Do you want a personal trainer? ")
    if plan == "basic":
        price = 2000
    elif plan ==  "premium":
        price = 5000
    else:
        price = 0
    if trainer == "yes":
        final = price + 1500
    else:
        final = price
    if plan == "premium" and trainer == "yes":
        final = final - 500
    if final < 2000:
        final = 2000
    total_revenue = total_revenue + final
    member_count = member_count + 1
print(f"Total Revenue: {total_revenue} Rupees ")