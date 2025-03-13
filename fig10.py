import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add main category
G.add_node("Proposed Security Solutions\n& Best Practices", color="red")

# Add subcategories
subcategories = [
    "Zero Trust Architecture",
    "AI & ML-Based Threat Detection",
    "Blockchain for Secure\nMulti-Cloud Operations",
    "Identity Federation &\nAccess Control"
]

for sub in subcategories:
    G.add_node(sub, color="blue")
    G.add_edge("Proposed Security Solutions\n& Best Practices", sub)

# Create layout and draw graph
plt.figure(figsize=(8, 5))
pos = nx.spring_layout(G, seed=42)  # Position nodes

# Get node colors
node_colors = [G.nodes[n].get("color", "gray") for n in G.nodes]

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color="gray", 
        node_size=3000, font_size=10, font_weight="bold", arrows=True)

# Show plot
plt.title("Key Security Solutions for Multi-Cloud Environments")
plt.show()
