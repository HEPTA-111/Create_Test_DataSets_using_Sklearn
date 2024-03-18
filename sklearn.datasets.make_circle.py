# Importing necessary modules
from sklearn.datasets import make_circles  # Importing make_circles function to generate test datasets
from matplotlib import pyplot as plt       # Importing pyplot module from matplotlib for plotting
from matplotlib import style               # Importing style module from matplotlib to set plot style

# Setting plot style to 'fivethirtyeight'
style.use("fivethirtyeight")

# Generating test datasets using make_circles function
# n_samples: Total number of data points
# noise: Standard deviation of Gaussian noise added to the data
X, y = make_circles(n_samples=100, noise=0.02)

# Plotting the generated data points
plt.scatter(X[:, 0], X[:, 1], s=40, color='g')  # Scatter plot of X values against Y values
plt.xlabel("X")                                # Labeling the x-axis
plt.ylabel("Y")                                # Labeling the y-axis

plt.show()  # Displaying the plot
plt.clf()   # Clearing the current figure for the next plot
