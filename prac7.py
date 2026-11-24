items = []

while True:
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display the list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.append(item)
        print("Item added")

    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in items:
            items.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    elif choice == "3":
        print("List:", items)

    elif choice == "4":
        break

    else:
        print("Invalid choice")