import networkx as nx

# Create an empty graph
G = nx.Graph()

# Add Employee nodes
employees = [
    {'name': 'Alice', 'age': 28, 'is_employed': True, 'working_area': 'Marketing', 'university_grade': 3.8, 'num_skills': 5},
    {'name': 'Bob', 'age': 32, 'is_employed': True, 'working_area': 'Sales', 'university_grade': 3.2, 'num_skills': 3},
    {'name': 'Charlie', 'age': 24, 'is_employed': False, 'working_area': None, 'university_grade': 4.0, 'num_skills': 2},
]
for emp in employees:
    G.add_node(emp['name'], age=emp['age'], is_employed=emp['is_employed'], working_area=emp['working_area'], university_grade=emp['university_grade'], num_skills=emp['num_skills'])

# Add Department nodes
departments = [
    {'name': 'Marketing', 'manager': 'Alice'},
    {'name': 'Sales', 'manager': 'Bob'},
    {'name': 'Engineering', 'manager': None},
]
for dept in departments:
    G.add_node(dept['name'], manager=dept['manager'])

# Add Project nodes
projects = [
    {'name': 'Project X', 'department': 'Marketing'},
    {'name': 'Project Y', 'department': 'Sales'},
    {'name': 'Project Z', 'department': 'Engineering'},
]
for proj in projects:
    G.add_node(proj['name'], department=proj['department'])

# Add edges
G.add_edges_from([
    ('Alice', 'Marketing', {'relation': 'Works in'}),
    ('Bob', 'Sales', {'relation': 'Works in'}),
    ('Charlie', 'Engineering', {'relation': 'Works in'}),
    ('Alice', 'Project X', {'relation': 'Works on'}),
    ('Bob', 'Project Y', {'relation': 'Works on'}),
    ('Charlie', 'Project Z', {'relation': 'Works on'}),
    ('Alice', 'Bob', {'relation': 'Reports to'}),
])

# Print information about Alice
alice = G.nodes['Alice']
print(f"Name: {alice['name']}")
print(f"Age: {alice['age']}")
print(f"Is employed: {alice['is_employed']}")
print(f"Working area: {alice['working_area']}")
print(f"University grade: {alice['university_grade']}")
print(f"Number of skills: {alice['num_skills']}")

# Print information about Marketing department
marketing = G.nodes['Marketing']
print(f"Department: {marketing['name']}")
print(f"Manager: {marketing['manager']}")

# Print information about Project X
proj_x = G.nodes['Project X']
print(f"Project: {proj_x['name']}")
print(f"Department: {proj_x['department']}")


