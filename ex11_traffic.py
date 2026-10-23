name = input("Enter your name:")
speed = int(input("What is your speed in km/h?"))
school = input("Were you in a school zone?")
licence = input("Do you have licence?")
print(f"Driver {name}")
if licence == "no":
    print(f"Fine: 5000")
    print(f"Action: Car Impounded")
elif licence == "yes" and school == "yes" and speed > 40:
    print(f"Fine: 3000")
    print(f"Action: Licence Checked")
elif licence == "yes" and school == "yes" and speed <= 40:
    print(f"Fine: 1000")
    print(f"Action: Licence Checked")
elif licence == "yes" and school == "no" and speed > 80:
    print(f"Fine: 2000")
    print(f"Action: Licence Checked")
elif licence == "yes" and school == "no" and speed <= 80:
    print(f"Fine: 0 (Warning)")
    print(f"Action: Licence Checked")