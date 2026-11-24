scores = [
    [78, 82, 91],
    [65, 70, 68],
    [90, 88, 94],
    [55, 61, 58]
]

averages = []
passing = 0

for student in scores:
    total = 0

    for score in student:
        total = total + score

    average = total / len(student)
    averages.append(average)

    if average >= 60:
        passing = passing + 1

highest = max(averages)
highest_index = averages.index(highest)

print("Averages:", averages)
print("Passing students:", passing)
print("Highest average:", highest)
print("Student index:", highest_index)