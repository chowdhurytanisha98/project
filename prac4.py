numbers = [4, 7, 2, 7, 9, 7, 1]
target = 7

positions = []

for index in range(len(numbers)):
    if numbers[index] == target:
        positions.append(index)

print("Target:", target)
print("Positions:", positions)
print("Number of occurrences:", len(positions))

first_occurrence = None

for index in range(len(numbers)):
    if numbers[index] == target:
        first_occurrence = index
        break

print("First occurrence:", first_occurrence)