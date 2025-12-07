# Day 4 Program: Student Marks Analyzer

def find_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 45:
        return "D"
    else:
        return "Fail"

# Taking marks (list)
marks = []

print("Enter marks for 5 subjects:")

for i in range(5):
    m = float(input(f"Subject {i+1} mark: "))
    marks.append(m)

# Calculations
total = sum(marks)
average = total / 5

# Output
print("\n--- Result ---")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", find_grade(average))