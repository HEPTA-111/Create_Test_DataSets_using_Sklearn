# Importing necessary libraries
from sklearn.datasets import make_sparse_uncorrelated  # Importing make_sparse_uncorrelated function to generate dataset
import matplotlib.pyplot as plt                        # Importing pyplot module from matplotlib for plotting

# Generate a sparse uncorrelated dataset
# n_samples: Total number of data points
# n_features: Number of features (independent variables)
# random_state: Seed used by random number generator for reproducibility
X, y = make_sparse_uncorrelated(n_samples=100, n_features=4, random_state=23)

# Plotting the generated datasets
plt.figure(figsize=(12, 10))  # Setting figure size

# Looping over each feature for plotting
for i in range(4):
    plt.subplot(2, 2, i + 1)             # Creating subplots
    plt.scatter(X[:, i], y)              # Scatter plot of X values against y values
    plt.xlabel('X' + str(i + 1))         # Labeling x-axis
    plt.ylabel('Y')                      # Labeling y-axis

plt.show()  # Displaying the plot
