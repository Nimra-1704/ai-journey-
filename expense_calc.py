expense1 = float(input("Enter expense 1: "))
expense2 = float(input("Enter expense 2: "))
expense3 = float(input("Enter expense 3: "))
total = expense1 + expense2 + expense3
average = total / 3
print("Total: " + str(total))
print("Average: " + str(round(average, 2)))