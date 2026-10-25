import json
user = {"username": "Nimra", "role": "Admin"}
with open("user.json", "w") as file:
    json.dump(user, file)
with open("user.json", "r") as file:
    loaded_user = json.load(file)
    print(f"{loaded_user['role']}")
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25}
]
with open("products.json", "w") as file:
    json.dump(products, file)
with open("products.json", "r") as file:
    json.load(file)
    for product in products:
        print(f"{product['name']}")