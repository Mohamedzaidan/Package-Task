from Pachage_school import teacher, student

subjects =[{'name': 'Math', 'passing_grade': 0},
{'name': 'Physics', 'passing_grade': 0},
{'name': 'Statistics', 'passing_grade': 0}]

teacher.passing_grades(subjects)

student_grade = [{'name': 'mohamed', 'subject': 'Math', 'grade': 60},
{'name': 'ahmed', 'subject': 'Physics', 'grade': 60},
{'name': 'amr', 'subject': 'Statistics', 'grade': 60}]

for student_gr in student_grade:
    student.check_passed(student_gr, subjects)