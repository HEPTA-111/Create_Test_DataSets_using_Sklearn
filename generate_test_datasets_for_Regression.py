# Importing necessary libraries
from sklearn.datasets import make_regression  # Importing make_regression function to generate regression dataset
import matplotlib.pyplot as plt                # Importing pyplot module from matplotlib for plotting

# Generate 1D regression dataset
# n_samples: Total number of data points
# n_features: Number of features (independent variables)
# noise: Standard deviation of Gaussian noise added to the data
# random_state: Seed used by random number generator for reproducibility
X, y = make_regression(n_samples=50, n_features=1, noise=20, random_state=23)

# Plotting the generated dataset
plt.scatter(X, y)  # Scatter plot of X values against y values
plt.show()         # Displaying the plot
