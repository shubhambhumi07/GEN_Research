import matplotlib.pyplot as plt
import networkx as nx

# Create graph
G = nx.DiGraph()

# Define nodes
cloud_providers = ["AWS", "Azure", "GCP", "IBM"]
enterprise = "Enterprise Network"

# Add nodes
G.add_node(enterprise, color='red', size=1500)
for provider in cloud_providers:
    G.add_node(provider, color='blue', size=1000)

# Add edges from cloud providers to enterprise network
for provider in cloud_providers:
    G.add_edge(provider, enterprise)

# Define positions
pos = nx.spring_layout(G, seed=42)
node_colors = [G.nodes[n].get('color', 'gray') for n in G.nodes()]
node_sizes = [G.nodes[n].get('size', 500) for n in G.nodes()]

# Draw graph
plt.figure(figsize=(7, 5))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, edge_color='gray', font_size=10, font_weight='bold')
plt.title("MultiCloud Architecture", fontsize=14)
plt.show()
