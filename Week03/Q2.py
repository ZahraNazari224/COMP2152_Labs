#Question2: Shopping Cart (Lists _ Searching and Removal)
cart =["apple", "banana", "milk", "bread", "apple", "eggs"]

apple_count = cart.count("apple")
print("Numbers of apples: ", apple_count)

milk_position = cart.index("milk")
print("Index of milk: ",milk_position )

cart.remove("apple")
print("Removed item using pop: ",cart.pop())

print("Is banana in the cart?", "banana" in cart)

print("Final Cart ", cart)



