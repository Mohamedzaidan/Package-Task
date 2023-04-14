def passing_grades(subjects):
    for subject in subjects:
        passing_grade = input(f"Enter passing grade for {subject['name']}: ")
        try:
            subject['passing_grade'] = int(passing_grade)
            
        except ValueError:
            print("Invalid input. Please enter an integer.")