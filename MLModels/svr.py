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

def train_svr_model(data_file, feature_columns, target_column, test_size=0.2, random_state=42, kernel='rbf', C=100, epsilon=0.1):
    # Step 1: Import the necessary libraries
    
    # No need to import the libraries again, as they are already imported in the function definition
    
    # Step 2: Load the dataset
    df = pd.read_csv(data_file)

    # Step 3: Preprocess the data
    X = df[feature_columns].values
    y = df[target_column].values

    # Step 4: Scale the features
    scaler = MinMaxScaler(feature_range=(0, 1))
    X_scaled = scaler.fit_transform(X)

    # Step 5: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=random_state)

    # Step 6: Build the SVR model
    model = SVR(kernel=kernel, C=C, epsilon=epsilon)

    # Step 7: Train the model
    model.fit(X_train, y_train)

    # Step 8: Make predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Step 9: Evaluate the model
    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test, y_pred_test)
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)

    print('Train Mean Squared Error:', mse_train)
    print('Test Mean Squared Error:', mse_test)
    print('Train R-squared:', r2_train)
    print('Test R-squared:', r2_test)