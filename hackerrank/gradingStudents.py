def gradingStudents(grades):
    rounded_grades = []
    for nota in grades:
        if nota > 37:
            op = int(nota / 5)
            op3 = (op * 5) + 5
            result = op3 - nota

            if result <= 2:
                print(op3)
            else:
                print(nota)
        else:
            print(nota)

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    gradingStudents(grades)