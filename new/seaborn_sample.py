import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Set Seaborn style
sns.set_style("whitegrid")  # Options: "darkgrid", "whitegrid", "dark", "white", "ticks"

# Create a Matplotlib plot
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label="sin(x)", color="blue")
plt.plot(x, y2, label="cos(x)", color="orange")

# Add labels and title
plt.title("Trigonometric Functions", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)

# Add legend
plt.legend()

# Show the plot
plt.show()