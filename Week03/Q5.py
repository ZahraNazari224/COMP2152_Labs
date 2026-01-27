#Contact Book (Dictionaries - Basic Operations)
contacts= {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print("Alice's phone number: ", contacts["Alice"])
contacts["Diana"] = "555-4321"
print("Contacts after Diana: ",contacts)
contacts["Bob"] = "555-0000"
print("Contacts after Bob:", contacts)
del contacts["Charlie"]
print(f"Contacts after Charlie: ", contacts)
print("All names: ", dict.keys(contacts))
print("All numbers: ", dict.values(contacts))
print("Total contacts: ",len(contacts))
