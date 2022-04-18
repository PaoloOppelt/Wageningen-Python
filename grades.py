grade_str = input('Input a grade:')
grade = float(grade_str)
if grade<6:
    grade = int(grade)
    print('Insufficient', grade)
else:
    grade = int(grade)
    print('sufficient', grade)