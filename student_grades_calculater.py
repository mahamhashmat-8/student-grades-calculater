print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

python_marks = float(input("Enter Python marks: "))
english_marks = float(input("Enter English marks: "))
math_marks = float(input("Enter Mathematics marks: "))

total = python_marks + english_marks + math_marks
percentage = (total / 300) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print(f"Student: {name}")
print(f"Total Marks: {total} / 300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")