import numpy as np
import matplotlib.pyplot as plt

# Define a function to handle keypress events
def press(event):
   print('You pressed:', event.key)

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Connect the keypress event handler to the figure canvas
cid = fig.canvas.mpl_connect('key_press_event', press)

# Plot sin wave	
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x))

# Display the plot
plt.show()