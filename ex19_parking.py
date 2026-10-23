total_bill = 0
car_count = 1
while car_count <= 3:
    hours = float(input("Enter hours parked for car [car_count]: "))
    member = input("Is this a VIP member? ")
    price = 100 * hours
    if member == "yes":
        price = price - 50
    if hours > 8:
            price = price + 200
    if price < 150:
                price = 150
    total_bill = total_bill + price
    car_count = car_count + 1
print(f" Total Bill for 3 cars: {total_bill} Rupees")