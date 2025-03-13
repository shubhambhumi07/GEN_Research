import networkx as nx
import matplotlib.pyplot as plt

# Define threats and corresponding security solutions
threats = [
    "Data Leakage",
    "Unauthorized Access",
    "Insecure APIs",
    "Misconfigurations",
    "Compliance Gaps"
]

solutions = [
    "Data Encryption",
    "Multi-Factor Authentication",
    "API Security Gateway",
    "Cloud Security Posture Management (CSPM)",
    "Regulatory Compliance Audits"
]

# Create a directed graph
G = nx.DiGraph()

# Add edges from threats to solutions
edges = [
    ("Data Leakage", "Data Encryption"),
    ("Unauthorized Access", "Multi-Factor Authentication"),
    ("Insecure APIs", "API Security Gateway"),
    ("Misconfigurations", "Cloud Security Posture Management (CSPM)"),
    ("Compliance Gaps", "Regulatory Compliance Audits")
]

G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2500, font_size=10, font_weight='bold')
plt.title("Multi-Cloud Security Threats and Solutions Mapping")
plt.show()
