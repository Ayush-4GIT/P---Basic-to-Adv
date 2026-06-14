subjects = ["Math", "Science", "English", "Computer", "History"]

total = 0

for subject in subjects:
    marks = int(input(f"Enter {subject} marks (out of 100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks entered!")
        exit()

    total += marks

percentage = total / len(subjects)

print("\nTotal Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("Grade:", grade)