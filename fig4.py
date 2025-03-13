# Import necessary libraries
import matplotlib.pyplot as plt

# Data
challenges = ['Data Security', 'IAM Risks', 'Compliance', 'Vendor Lock-in', 'Network Security']
impact = [80, 75, 70, 65, 85]  # Hypothetical impact scores

# Create bar chart
plt.figure(figsize=(7, 4))
plt.barh(challenges, impact, color=['red', 'blue', 'green', 'purple', 'orange'])
plt.xlabel('Impact Level')
plt.ylabel('Security Challenges')
plt.title('Security Challenges in MultiCloud')
plt.xlim(0, 100)

# Show plot
plt.show()



