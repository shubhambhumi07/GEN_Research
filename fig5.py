import matplotlib.pyplot as plt
import networkx as nx

# Create a Directed Graph
G = nx.DiGraph()

# Define Nodes for Research Methodology
nodes = [
    "Research Design", "Data Collection", "Security Analysis Framework",
    "Tools & Techniques", "Empirical Security Analysis", "Qualitative Analysis",
    "Primary Data", "Secondary Data", "Risk Assessment", "Threat Modeling",
    "Security Policies", "Encryption", "Intrusion Detection", "Zero Trust Security"
]

# Add Nodes
G.add_nodes_from(nodes)

# Define Edges (Connections)
edges = [
    ("Research Design", "Empirical Security Analysis"), ("Research Design", "Qualitative Analysis"),
    ("Data Collection", "Primary Data"), ("Data Collection", "Secondary Data"),
    ("Security Analysis Framework", "Risk Assessment"), ("Security Analysis Framework", "Threat Modeling"),
    ("Security Analysis Framework", "Security Policies"),
    ("Tools & Techniques", "Encryption"), ("Tools & Techniques", "Intrusion Detection"),
    ("Tools & Techniques", "Zero Trust Security")
]

# Add Edges
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)  # Layout for positioning
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2500, font_size=8, font_weight="bold")

# Display the diagram
plt.title("Research Methodology Flowchart")
plt.show()
