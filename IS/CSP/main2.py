
from constraint import Problem, AllDifferentConstraint

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
times = ["10AM", "11AM", "12PM", "1PM", "2PM"]
locations = ["A", "B", "C", "D", "E"]
courses = ["Math", "Science", "English", "History"]

problem = Problem()

# Add variables
for course in courses:
    problem.addVariable(course, [(day, time, location) for day in days for time in times for location in locations])

# Add constraints
for course in courses:
    for other_course in courses:
        if course != other_course:
            problem.addConstraint(lambda c1, c2: c1[0] != c2[0] or c1[1] != c2[1], (course, other_course))
            problem.addConstraint(lambda c1, c2: c1[2] != c2[2] or c1[1] != c2[1], (course, other_course))

problem.addConstraint(AllDifferentConstraint())

# Get solution
solution = problem.getSolution()
if solution:
    for course, (day, time, location) in solution.items():
        print(f"{course}: {day} {time} {location}")
else:
    print("No solution found")
