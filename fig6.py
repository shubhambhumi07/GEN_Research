import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define nodes
nodes = {
    "Risk Assessment": (0, 3),
    "Attack Surface": (-2, 2),
    "Threat Likelihood Modeling": (0, 2),
    "Security Posture Definition": (2, 2),
    "Vulnerability Scanning": (-2.5, 1),
    "Penetration Testing": (-1.5, 1),
    "Probability Models": (-0.5, 1),
    "Historical Threat Data": (0.5, 1),
    "Compliance Standards": (1.5, 1),
    "Risk Scores": (2.5, 1),
}

# Add nodes to the graph
for node in nodes:
    G.add_node(node)

# Define edges (connections)
edges = [
    ("Risk Assessment", "Attack Surface"),
    ("Risk Assessment", "Threat Likelihood Modeling"),
    ("Risk Assessment", "Security Posture Definition"),
    ("Attack Surface", "Vulnerability Scanning"),
    ("Attack Surface", "Penetration Testing"),
    ("Threat Likelihood Modeling", "Probability Models"),
    ("Threat Likelihood Modeling", "Historical Threat Data"),
    ("Security Posture Definition", "Compliance Standards"),
    ("Security Posture Definition", "Risk Scores"),
]

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(10, 6))
pos = nodes  # Position nodes using predefined layout
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', 
        node_size=3000, font_size=10, font_weight='bold', arrowsize=12)

plt.title("Risk Assessment Framework for Multi-Cloud Security", fontsize=12)
plt.show()