my_profile = {
    "name": "nimra",
    "age": 21,
    "city": "burewala"
}
print(my_profile["city"])

sample = {
    "id": "S101",
    "type": "blood",
    "volume": "5.5",
    "status": "pending"
}
print(sample["id"])
print(sample["type"])
print(sample["volume"])
print(sample["status"])

patients = [
    {"name": "Ali", "disease": "Flu"},
    {"name": "Sara", "disease": "Fever"}
]
for char in patients:
    print(char["name"])