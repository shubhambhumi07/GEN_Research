import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Main categories in 3.4 (Tools and Techniques Used)
categories = [
    "Encryption & Key Management",
    "Intrusion Detection & Prevention",
    "Cloud Security Posture Management (CSPM)",
    "Zero Trust Security"
]

# Subcategories
subcategories = {
    "Encryption & Key Management": ["AES-256", "Homomorphic Encryption", "Cloud KMS"],
    "Intrusion Detection & Prevention": ["AI Anomaly Detection", "Packet Inspection", "Log Monitoring"],
    "Cloud Security Posture Management (CSPM)": ["Automated Config Audits", "Compliance Enforcement"],
    "Zero Trust Security": ["Software-Defined Perimeters", "Micro-Segmentation", "Behavior-Based Authentication"]
}

# Add nodes to the graph
for category in categories:
    G.add_node(category, color='lightblue', size=1500)  # Main categories in blue
    for sub in subcategories[category]:
        G.add_node(sub, color='lightgreen', size=1000)  # Subcategories in green
        G.add_edge(category, sub)  # Connect category to subcategory

# Get node colors and sizes
colors = [G.nodes[n]['color'] for n in G.nodes]
sizes = [G.nodes[n]['size'] for n in G.nodes]

# Draw the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=sizes, edge_color='gray', font_size=10, font_weight='bold')
plt.title("Security Tools and Techniques in Multi-Cloud")
plt.show()
