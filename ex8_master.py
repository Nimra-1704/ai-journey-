name = input("Enter your name: ")
total = int(input("Enter total number of minutes: "))
hours = total // 60
minutes = total % 60
print(f" {name}, {total} minutes is {hours} hours and {minutes} minutes ")
