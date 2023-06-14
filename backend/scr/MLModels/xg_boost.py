'''
In this advanced XGBoost model:

The stock price data is loaded from a CSV file, assuming the file has columns named 'Date' and 'Close'.

The features and target variables are prepared. The features exclude the 'Date' column, and the target is the 'Close' column.

The data is split into training and testing sets using train_test_split from sklearn.model_selection.

The XGBoost model is created with specified parameters such as the number of estimators (n_estimators), learning rate, maximum depth (max_depth), subsampling rate (subsample), and column subsampling rate (colsample_bytree).

The model is trained using the training data.

Predictions are made for both the training and testing data.

The model is evaluated using mean squared error (MSE) and R-squared (coefficient of determination) metrics.
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor

def train_xgboost_model(data_file, feature_columns, target_column, test_size=0.2, random_state=42,
                        n_estimators=100, learning_rate=0.1, max_depth=5, subsample=0.8, colsample_bytree=0.8):
    # Step 1: Import the necessary libraries
    
    # No need to import the libraries again, as they are already imported in the function definition
    
    # Step 2: Load the dataset
    df = pd.read_csv(data_file)

    # Step 3: Preprocess the data
    X = df[feature_columns].values
    y = df[target_column].values

    # Step 4: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Step 5: Build the XGBoost model
    model = XGBRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        subsample=subsample,
        colsample_bytree=colsample_bytree,
        random_state=random_state
    )

    # Step 6: Train the model
    model.fit(X_train, y_train)

    # Step 7: Make predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Step 8: Evaluate the model
    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test, y_pred_test)
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)

    print('Train Mean Squared Error:', mse_train)
    print('Test Mean Squared Error:', mse_test)
    print('Train R-squared:', r2_train)
    print('Test R-squared:', r2_test)

