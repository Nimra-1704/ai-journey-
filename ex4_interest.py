principal = float(input("Enter principal: "))
rate = float(input("Enter rate (%): "))
time = float(input("Enter time (years): "))
si = principal * rate * time / 100
total_amount = principal + si
print(f"Simple Interest: {si}")
print(f"Total Amount: {total_amount}")