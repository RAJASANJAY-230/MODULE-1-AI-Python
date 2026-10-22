
def analyse_marks(marks):
    average = sum(marks) / len(marks)

    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

    if average >= 50:
        print("Result: Pass")
    else:
        print("Result: Needs improvement")


student_marks = []

for i in range(3):
    mark = float(input(f"Enter mark {i + 1}: "))
    student_marks.append(mark)

analyse_marks(student_marks)
