items = ["pen", "book", "pen", "bag", "book", "ruler", "pen"]

unique_items = []
repeated_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)
    else:
        repeated_items.append(item)

print("Unique items:", unique_items)
print("Repeated occurrences:", repeated_items)