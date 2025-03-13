import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes
multicloud = "MultiCloud Computing"
benefits = ["Reliability", "Compliance", "Performance", "Cost Optimization"]
challenges = ["Data Security", "IAM Risks", "Regulatory Compliance", "Vendor Lock-in", "Network Security"]
solutions = ["Encryption", "Zero-Trust", "AI Threat Detection", "Compliance Frameworks"]

# Add nodes
G.add_node(multicloud, color='red', size=1500)
for b in benefits:
    G.add_node(b, color='green', size=1000)
for c in challenges:
    G.add_node(c, color='orange', size=1000)
for s in solutions:
    G.add_node(s, color='blue', size=1000)

# Add edges
for b in benefits:
    G.add_edge(multicloud, b)
for c in challenges:
    G.add_edge(multicloud, c)
for s in solutions:
    for c in challenges:  # Solutions addressing challenges
        G.add_edge(c, s)

# Get positions for nodes
pos = nx.spring_layout(G, seed=42)  

# Extract colors and sizes
node_colors = [G.nodes[n].get('color', 'gray') for n in G.nodes()]
node_sizes = [G.nodes[n].get('size', 500) for n in G.nodes()]

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, edge_color='gray', font_size=9, font_weight='bold')
plt.title("MultiCloud Security Landscape", fontsize=14)
plt.show()
