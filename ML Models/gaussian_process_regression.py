'''
In this advanced GPR script:

The stock price data is loaded from a CSV file, assuming the file has columns named 'Date' and 'Close'.

The features and target variables are prepared. The features exclude the 'Date' column, and the target is the 'Close' column.

The data is split into training and testing sets using train_test_split from sklearn.model_selection.

The GPR model is defined with a Radial Basis Function (RBF) kernel. The length scale of the RBF kernel is set to 1.0 with bounds between 0.1 and 10.0.

The model is trained using the training data.

Predictions are made for both the training and testing data, along with the associated standard deviations of the predictions.

The model is evaluated using mean squared error (MSE) and R-squared (coefficient of determination) metrics.
'''

import pandas as pd
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the stock price data
df = pd.read_csv('stock_data.csv')

# Prepare the features and target
X = df.drop(['Date', 'Close'], axis=1).values
y = df['Close'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the Gaussian Process Regression model
kernel = RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0))
model = GaussianProcessRegressor(kernel=kernel, alpha=0.1, n_restarts_optimizer=10)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred_train, y_std_train = model.predict(X_train, return_std=True)
y_pred_test, y_std_test = model.predict(X_test, return_std=True)

# Evaluate the model
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)

print('Train Mean Squared Error:', mse_train)
print('Test Mean Squared Error:', mse_test)
print('Train R-squared:', r2_train)
print('Test R-squared:', r2_test)
