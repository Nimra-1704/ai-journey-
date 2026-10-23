total = int(input("Enter total seconds: "))
hours = total // 3600
remaining = total % 3600
minutes = remaining // 60
seconds = remaining % 60 
print(f"{total} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")