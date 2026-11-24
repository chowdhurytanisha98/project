items = ["Notebook", "Pen", "Calculator", "Folder"]
prices = [120.0, 15.0, 850.0, 80.0]
quantities = [2, 5, 1, 3]

subtotal = 0

for i in range(len(items)):
    total = prices[i] * quantities[i]
    print(items[i], "=", total)
    subtotal = subtotal + total

print("Subtotal:", subtotal)

if subtotal >= 1000:
    discount = subtotal * 0.10
elif subtotal >= 500:
    discount = subtotal * 0.05
else:
    discount = 0

after_discount = subtotal - discount

if after_discount >= 1000:
    delivery = 0
else:
    delivery = 60

final_total = after_discount + delivery

print("Discount:", discount)
print("Delivery:", delivery)
print("Final total:", final_total)