import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add Employee nodes
G.add_node('Alice', age=28, is_employed=True, working_area='Marketing', university_grade=3.8, num_skills=5)
G.add_node('Bob', age=32, is_employed=True, working_area='Sales', university_grade=3.2, num_skills=3)
G.add_node('Charlie', age=24, is_employed=False, working_area=None, university_grade=4.0, num_skills=2)
G.add_node('David', age=29, is_employed=True, working_area='Sales', university_grade=3.6, num_skills=4)
G.add_node('Eve', age=27, is_employed=True, working_area='Marketing', university_grade=3.5, num_skills=3)
G.add_node('Frank', age=35, is_employed=True, working_area='Engineering', university_grade=3.9, num_skills=6)
G.add_node('Grace', age=26, is_employed=True, working_area='Marketing', university_grade=3.7, num_skills=4)
G.add_node('Henry', age=31, is_employed=False, working_area=None, university_grade=3.5, num_skills=2)

G.add_node('Marketing', manager='Alice')
G.add_node('Sales', manager='Bob')
G.add_node('Engineering', manager=None)

G.add_node('Project X', department='Marketing')
G.add_node('Project Y', department='Sales')
G.add_node('Project Z', department='Engineering')
G.add_node('Project W', department='Sales')

G.add_edges_from([
    ('Alice', 'Marketing', {'relation': 'Works in'}),
    ('Bob', 'Sales', {'relation': 'Works in'}),
    ('Charlie', 'Engineering', {'relation': 'Works in'}),
    ('David', 'Sales', {'relation': 'Works in'}),
    ('Eve', 'Marketing', {'relation': 'Works in'}),
    ('Alice', 'Project X', {'relation': 'Works on'}),
    ('Bob', 'Project Y', {'relation': 'Works on'}),
    ('Charlie', 'Project Z', {'relation': 'Works on'}),
    ('David', 'Project W', {'relation': 'Works on'}),
    ('Alice', 'Bob', {'relation': 'Reports to'}),
    ('Bob', 'Sales', {'relation': 'Manages'}),
    ('Marketing', 'Project X', {'relation': 'Manages'}),
    ('Sales', 'Project Y', {'relation': 'Manages'}),
    ('Engineering', 'Project Z', {'relation': 'Manages'}),
    ('Frank', 'Engineering', {'relation': 'Works in'}),
    ('Grace', 'Marketing', {'relation': 'Works in'}),
    ('Frank', 'Project Z', {'relation': 'Works on'}),
    ('Grace', 'Project X', {'relation': 'Works on'}),
    ('Frank', 'Bob', {'relation': 'Reports to'}),
    ('Henry', 'Frank', {'relation': 'Mentor'}),
])


pos = nx.spring_layout(G)  # layout for visualization
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.show()

# Define a function to traverse the graph and find the answer
def traverse_graph(node, attribute, value):
    """Traverses the graph starting from the given node and returns the nodes that match the given attribute and value."""
    result = []
    for n in G.nodes():
        if G.nodes[n].get(attribute) == value and nx.has_path(G, n, node):
            result.append(n)
    return result

# Define the chat function
def chat():
    """Starts an interactive chat with the user."""
    print("Welcome to the knowledge graph chat!")
    while True:
        # Ask the user for the name of a person in the graph
        name = input("Who would you like to know more about? ")

        # Check if the person is in the graph
        if name not in G.nodes():
            print(f"Sorry, I don't know anything about {name}.")
            continue

        # Ask the user for the attribute they want to know about
        attribute = input("What would you like to know about them? (e.g. age, is_employed, working_area, university_grade, num_skills): ")

        # Check if the attribute is valid
        if attribute not in G.nodes[name]:
            print(f"Sorry, {name} doesn't have any information about {attribute}.")
            continue

        # Ask the user for the value of the attribute
        value = input(f"What is {name}'s {attribute}? ")

        # Traverse the graph to find the answer
        result = traverse_graph(name, attribute, value)

        # Check if there are any results
        if len(result) == 0:
            print(f"Sorry, I don't know anyone who matches {name}'s {attribute} of {value}.")
            continue

        # Print the results
        print(f"I found the following people who match {name}'s {attribute} of {value}:")
        for r in result:
            if r != name:
                print(f"- {r}")

        # Ask the user if they want to continue
        choice = input("Would you like to know more? (y/n) ")
        if choice.lower() != "y":
            break

    print("Thank you for using the knowledge graph chat!")

# Start the chat
chat()
