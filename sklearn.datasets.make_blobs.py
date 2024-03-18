# Importing necessary modules
from sklearn.datasets import make_blobs  # Importing make_blobs function to generate test datasets
from matplotlib import pyplot as plt     # Importing pyplot module from matplotlib for plotting
from matplotlib import style             # Importing style module from matplotlib to set plot style

# Setting plot style to 'fivethirtyeight'
style.use("fivethirtyeight")

# Generating test datasets using make_blobs function
# n_samples: Total number of data points
# centers: Number of clusters to generate
# cluster_std: Standard deviation of clusters
# n_features: Number of features for each data point
X, y = make_blobs(n_samples=100, centers=3, cluster_std=1, n_features=2)

# Plotting the generated data points
plt.scatter(X[:, 0], X[:, 1], s=40, color='g')  # Scatter plot of X values against Y values
plt.xlabel("X")                                # Labeling the x-axis
plt.ylabel("Y")                                # Labeling the y-axis

plt.show()  # Displaying the plot
plt.clf()   # Clearing the current figure for the next plot
