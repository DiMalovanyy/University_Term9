from constraint import *

problem = Problem()

# Варіанти занять
activities = ['Lecture', 'Practical']

# Варіанти аудиторій
rooms = ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5']

# Варіанти викладачів
teachers = ['Teacher 1', 'Teacher 2', 'Teacher 3', 'Teacher 4']

# Варіанти студентів
students = ['Student 1', 'Student 2', 'Student 3', 'Student 4']

# Дні тижня
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Години
hours = ['8am-10am', '10am-12pm', '12pm-2pm', '2pm-4pm', '4pm-6pm']

# Змінюємо список годин на словник
hours_dict = {}
for i in range(len(hours)):
    hours_dict[hours[i]] = i

# Додаємо змінні для кожного заняття
for activity in activities:
    for day in days:
        for hour in hours:
            problem.addVariable(activity + '_' + day + '_' + hour, rooms)

# Додаємо змінні для кожного викладача
for teacher in teachers:
    for day in days:
        for hour in hours:
            problem.addVariable(teacher + '_' + day + '_' + hour, activities)

# Додаємо змінні для кожного студента
for student in students:
    for day in days:
        for hour in hours:
            problem.addVariable(student + '_' + day + '_' + hour, activities)

# Додаємо обмеження на розмір аудиторії
problem.addConstraint(lambda room, activity: True if room == 'Room 1' and activity == 'Practical' else True,
                      ('Practical_Monday_8am-10am', 'Room 1'))
problem.addConstraint(lambda room, activity: True if room == 'Room 2' and activity == 'Practical' else True,
                      ('Practical_Monday_10am-12pm', 'Room 2'))
problem.addConstraint(lambda room, activity: True if room == 'Room 3' and activity == 'Lecture' else True,
                      ('Lecture_Tuesday_12pm-2pm', 'Room 3'))

# Додаємо обмеження на те, що один викладач не може одночасно проводити різні пари
for teacher in teachers:
    for day in days:
        for hour in hours:
            problem.addConstraint(lambda a1, a2: True if a1 != a2 else False,
                                  (teacher + '_' + day + '_' + hour + '_' + 'Lecture',
                                   teacher + '_' + day + '_' + hour + '_' + 'Practical'))

# Додаємо обмеження на те, що один студент не може бути одночасно присутній на різних парах
for student in students:
    for day in days:
        for hour in hours:
            problem.addConstraint(lambda a1, a2: True if a1 != a2 else False,
(student + '' + day + '' + hour + '' + 'Lecture',
student + '' + day + '' + hour + '' + 'Practical'))


solutions = problem.getSolutions()
for solution in solutions:
    print(solution)

