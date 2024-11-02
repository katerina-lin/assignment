import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the cake base (rectangle)
cake_base = plt.Rectangle((0.2, 0.2), 0.6, 0.3, color='saddlebrown', ec='black')
ax.add_patch(cake_base)

# Draw the frosting (top rectangle)
frosting = plt.Rectangle((0.2, 0.5), 0.6, 0.1, color='peru', ec='black')
ax.add_patch(frosting)

# Draw cherries on top (circles)
for x in np.linspace(0.3, 0.7, 5):
    cherry = plt.Circle((x, 0.6), 0.02, color='red')
    ax.add_patch(cherry)

# Set limits and aspect
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

# Show the cake
plt.title("Chocolate Cake")
plt.show()
