'''
In this advanced CNN script:

The stock price data is loaded from a CSV file, assuming the file has columns named 'Date' and 'Close'.

The features and target variables are prepared. The features exclude the 'Date' column, and the target is the 'Close' column.

The features are scaled using MinMaxScaler from sklearn.preprocessing to ensure all values are in the same range.

The data is reshaped to match the input shape of the CNN, which expects a 3-dimensional input with dimensions (num_samples, num_features, 1).

The data is split into training and testing sets using train_test_split from sklearn.model_selection.

A CNN model is defined with a 1D convolutional layer, max pooling layer, flatten layer, and dense layers.

The CNN model is compiled and trained using the training data.

Predictions are made for both the training and testing data.

The model is evaluated using mean squared error (MSE) and R-squared (coefficient of determination) metrics.
'''

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score

def run_cnn_stock_prediction(data_file):
    # Load the stock price data
    df = pd.read_csv(data_file)

    # Prepare the features and target
    X = df.drop(['Date', 'Close'], axis=1).values
    y = df['Close'].values

    # Scale the features
    scaler = MinMaxScaler(feature_range=(0, 1))
    X_scaled = scaler.fit_transform(X)

    # Reshape the data for CNN input
    num_features = X_scaled.shape[1]
    num_samples = X_scaled.shape[0]
    X_reshaped = X_scaled.reshape((num_samples, num_features, 1))

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_reshaped, y, test_size=0.2, random_state=42)

    # Define the CNN model
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(num_features, 1)))
    model.add(tf.keras.layers.MaxPooling1D(pool_size=2))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(1))

    # Compile and train the CNN model
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

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

