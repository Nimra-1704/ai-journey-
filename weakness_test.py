import json
inventory = [
    {"item": "Bandages", "stock": 50},
    {"item": "Syringes", "stock": 5}
]
with open("meds.json", "w") as file:
    json.dump(inventory, file)
    print("Inventory Saved")
with open("meds.json", "r") as file:
    loaded_inventory = json.load(file)
    print(f"{loaded_inventory[0]['item']}")
found = False
search_item = "Syringes"
for item in loaded_inventory:
    if item["item"] == search_item:
        print(f"Found the {item["item"]}!")
        found = True
        break
if found == False:
    print("Item not found.")
