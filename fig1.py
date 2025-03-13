import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes
cloud_providers = ["AWS", "Azure", "GCP", "IBM"]
security_aspects = ["Data Security", "IAM", "Compliance", "Threat Detection"]
enterprise = "Enterprise Network"

# Add nodes
G.add_node(enterprise, color='red', size=1500)
for provider in cloud_providers:
    G.add_node(provider, color='blue', size=1000)
for aspect in security_aspects:
    G.add_node(aspect, color='green', size=1000)

# Add edges from cloud providers to enterprise network
for provider in cloud_providers:
    G.add_edge(provider, enterprise)

# Add edges from enterprise network to security aspects
for aspect in security_aspects:
    G.add_edge(enterprise, aspect)

# Get positions for nodes
pos = nx.spring_layout(G, seed=42)  # Layout for better visualization

# Extract colors and sizes
node_colors = [G.nodes[n].get('color', 'gray') for n in G.nodes()]
node_sizes = [G.nodes[n].get('size', 500) for n in G.nodes()]

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, edge_color='gray', font_size=10, font_weight='bold')
plt.title("Multi-Cloud Security Landscape", fontsize=14)
plt.show()
