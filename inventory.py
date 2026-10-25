import json
try:
    with open("inventory.json", "r") as file:
        inventory = json.load(file)
except FileNotFoundError:
    inventory = []
running = True
while running:
    print("---THE INVENTORY TRACKER---")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Exit")
    choice = input("Choose the following options (1-3): ")
    if choice == "1":
        name = input("Enter product's name: ")
        price = input("Enter price's name: ")
        product = {"name": name, "price": price}
        inventory.append(product)
        with open("inventory.json", "w") as file:
            json.dump(inventory, file)
        print("Product saved")
    elif choice == "2":
        if len(inventory) == 0:
            print("No products in inventory")
        else:
            for product in inventory:
                print(f"Name: {product['name']} | Price: {product['price']}")
    elif choice == "3":
        print("Goodbye.")
        running = False
    else:
        print("Invalid Choice.")