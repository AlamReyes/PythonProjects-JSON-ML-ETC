data_valid = False

while data_valid == False:
    grade1 = input("Type the grade of the first test: ")
    try:
        grade1 = float(grade1)
    except:
        print("invalid input. Only numbers are accepted. Separate decimals with a dot.")
        continue
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = input("Type the grade of the second test: ")
    try:
        grade2 = float(grade2)
    except:
        print("invalid input. Only numbers are accepted. Separate decimals with a dot.")
        continue
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    total_classes = input("Type the number of classes: ")
    try:
        total_classes = float(total_classes)
    except:
        print("invalid input. Only numbers are accepted.")
        continue
    if total_classes <= 0:
        print("The number of classes cant be zero or less than zero")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = input("Type the number of absences: ")
    try:
        absences = float(absences)
    except:
        print("invalid input. Only numbers are accepted.")
        continue
    if absences < 0 or absences > total_classes:
        print("The number of absences cant be less than zero or greater than the total of classes")
        continue
    else:
        data_valid = True

avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absences)/total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round((attendance*100), 2)) + '%')

if (avg_grade >= 6 and attendance >= 0.8):
    print("The student has been approved")
elif avg_grade < 6 and attendance < 0.8:
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%")
elif attendance >= 0.8:
    print("The student has failed due to an average grade lower than 6.0")
else:    print("The student has failed due to an attendance rate lower than 80%")

