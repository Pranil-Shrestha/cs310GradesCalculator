#USE AT YOUR OWN RISK
projects = [None] * 4
class_participation = 0.0
midterm = 0.0
final = 0.0

for x in range(3):
    print("Project: ",x + 1)
    projects[x] = float(input())

projects[3] = float(input("Expected P4 grades: "))
midterm = float(input("Midterm grades: "))
class_participation = float(input("Expected class participation: "))
final = float(input("Expected Final: "))

total = (10 * projects[0]/100) + (10 * projects[1]/100) + (10 * projects[2]/100) + (10 * projects[3]/100) + (5 * class_participation/5) + (25 * midterm/100) + (30 * final/100)
print("Expected total ", total)

