'''
In this advanced SVM model:

The stock price data is loaded from a CSV file, assuming the file has columns named 'Date' and 'Close'.

The features and target variables are prepared. The features exclude the 'Date' column, and the target is the 'Close' column.

The features are scaled using MinMaxScaler from sklearn.preprocessing to ensure all values are in the same range.

The data is split into training and testing sets using train_test_split from sklearn.model_selection.

The SVM model is created with a radial basis function (RBF) kernel and specified hyperparameters such as the regularization parameter (C) and epsilon value.

The model is trained using the training data.

Predictions are made for both the training and testing data.

The model is evaluated using mean squared error (MSE) and R-squared (coefficient of determination) metrics.
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# Load the stock price data
df = pd.read_csv('Dataset\Resultant Dataset\\ticker_csvs\ZOMATO.csv')

# Prepare the features and target
X = df.drop(['Date', 'Close'], axis=1).values
y = df['Close'].values

# Scale the features
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build the SVM model
model = SVR(kernel='rbf', C=100, epsilon=0.1)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluate the model
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)

print('Train Mean Squared Error:', mse_train)
print('Test Mean Squared Error:', mse_test)
print('Train R-squared:', r2_train)
print('Test R-squared:', r2_test)
