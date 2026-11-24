
prices = {
    "rice": 75,
    "oil": 185,
    "sugar": 120,
    "milk": 95,
    "egg": 12,
    "flour": 65,
    "salt": 40,
    "lentil": 130,
    "potato": 45,
    "onion": 80,
    "tea": 250,
    "coffee": 450,
    "biscuit": 50,
    "soap": 70,
    "shampoo": 180
}

print("Available Products:")

for item in prices:
    print(item, ":", prices[item], "Tk")

order = {}

n = int(input("How many order entries? "))

for i in range(n):

    item = input("Enter product: ").lower()
    quantity = int(input("Enter quantity: "))

    if item not in prices:
        print(item, "is not available.")
        continue

    if quantity <= 0:
        print("Invalid quantity.")
        continue

    order[item] = order.get(item, 0) + quantity


print("Final Combined Order")
print("Final order:", order)


bill = {}

subtotal = 0

for item in order:

    quantity = order[item]
    unit_price = prices[item]

    total = quantity * unit_price

    bill[item] = {
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    }

    subtotal = subtotal + total

if subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0

vat = (subtotal - discount) * 0.02

final_amount = subtotal - discount + vat

print("\n================ GROCERY SHOP BILL ================")
print("Item       Quantity   Unit Price   Total")
print("----------------------------------------------------")

for item in bill:
    print(item, "   ",
          bill[item]["quantity"], "       ",
          format(bill[item]["unit_price"], ".2f"), "     ",
          format(bill[item]["total"], ".2f"))

print("----------------------------------------------------")
print("Subtotal: Tk", format(subtotal, ".2f"))
print("Discount (5%): Tk", format(discount, ".2f"))
print("VAT (2%): Tk", format(vat, ".2f"))
print("----------------------------------------------------")
print("Final amount: Tk", format(final_amount, ".2f"))
print("====================================================")
