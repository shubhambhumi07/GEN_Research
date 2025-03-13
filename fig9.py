import matplotlib.pyplot as plt
import numpy as np

# Threat categories and their frequency
threats = ["Data Breach", "Unauthorized Access", "Insecure APIs", "Compliance Issues", "DDoS Attacks"]
occurrences = [85, 70, 65, 55, 40]

# Plotting
plt.figure(figsize=(8,5))
plt.bar(threats, occurrences, color=['red', 'blue', 'green', 'orange', 'purple'])
plt.xlabel("Multi-Cloud Security Threats")
plt.ylabel("Occurrences (%)")
plt.title(" ")
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle="--", alpha=0.7)

# Show the plot
plt.show()
