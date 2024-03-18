# Importing necessary modules
from sklearn.datasets import make_moons  # Importing make_moons function to generate test datasets
from matplotlib import pyplot as plt     # Importing pyplot module from matplotlib for plotting
from matplotlib import style             # Importing style module from matplotlib to set plot style

# Generating test datasets using make_moons function
# n_samples: Total number of data points
# noise: Standard deviation of Gaussian noise added to the data
X, y = make_moons(n_samples=1000, noise=0.1)

# Plotting the generated data points
plt.scatter(X[:, 0], X[:, 1], s=40, color='g')  # Scatter plot of X values against Y values
plt.xlabel("X")                                # Labeling the x-axis
plt.ylabel("Y")                                # Labeling the y-axis

plt.show()  # Displaying the plot
plt.clf()   # Clearing the current figure for the next plot
