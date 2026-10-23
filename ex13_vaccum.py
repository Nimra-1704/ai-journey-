roomsize = input("Enter room size: ")
dirtlevel = input("Enter dirt level: ")
basebattery = 0
if roomsize == "small":
    basebattery = 10
elif roomsize == "medium":
    basebattery = 20
elif roomsize == "large":
    basebattery = 30
else:
    print("Error: Unknown room size")
    exit()
if dirtlevel == "high":
        basebattery = basebattery * 2
else:
        basebattery = basebattery
if basebattery >= 50:
            print("Warning: Battery drain is high!")
print(f" Battery Used: {basebattery}%")