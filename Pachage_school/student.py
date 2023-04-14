def check_passed(student, subjects):
    subject = None
    for subj in subjects:
        if subj['name'] == student['subject']:
            subject = subj
            break

    if not subject:
        print(f"{student['name']} is not enrolled in {student['subject']}.")
    try:
        if student['grade'] >= subject['passing_grade']:
            student_passed = student['grade']/subject['passing_grade']*100
            print(f"{student['name']} passed  and his precent is : {student_passed}.")
        else:
            print(f"{student['name']} did not pass {student['subject']}.")
    except ZeroDivisionError:
        print("Passing grade cannot be 0.")