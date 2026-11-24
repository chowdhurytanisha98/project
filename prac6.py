numbers = [14, 8, 21, 21, 5, 17, 14]

largest = max(numbers)
second_largest = 0

for number in numbers:
    if number < largest:
        if number > second_largest:
            second_largest = number

print("Largest distinct value:", largest)

if second_largest == 0:
    print("There is no second-largest value")
else:
    print("Second-largest distinct value:", second_largest)