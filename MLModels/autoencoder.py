'''
In this advanced Autoencoder script:

The stock price data is loaded from a CSV file, assuming the file has columns named 'Date' and 'Close'.

The features and target variables are prepared. The features exclude the 'Date' column, and the target is the 'Close' column.

The features are scaled using MinMaxScaler from sklearn.preprocessing to ensure all values are in the same range.

The data is split into training and testing sets using train_test_split from sklearn.model_selection.

An Autoencoder model is defined with an input layer, an encoding layer, and a decoding layer.

The Autoencoder model is compiled and trained using the training data. The goal is to reconstruct the input data at the output layer.

The trained Autoencoder is then used to extract the encoded representations of the input data.
'''

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score

def run_autoencoder_stock_prediction(data_file):
    # Load the stock price data
    df = pd.read_csv(data_file)

    # Prepare the features and target
    X = df.drop(['Date', 'Close'], axis=1).values
    y = df['Close'].values

    # Scale the features
    scaler = MinMaxScaler(feature_range=(0, 1))
    X_scaled = scaler.fit_transform(X)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Define the Autoencoder model
    input_dim = X_train.shape[1]
    encoding_dim = int(input_dim / 2)

    input_layer = tf.keras.layers.Input(shape=(input_dim,))
    encoder = tf.keras.layers.Dense(encoding_dim, activation='relu')(input_layer)
    decoder = tf.keras.layers.Dense(input_dim, activation='relu')(encoder)
    autoencoder = tf.keras.models.Model(inputs=input_layer, outputs=decoder)

    # Compile and train the Autoencoder model
    autoencoder.compile(optimizer='adam', loss='mse')
    autoencoder.fit(X_train, X_train, epochs=100, batch_size=32, validation_data=(X_test, X_test))

    # Use the trained Autoencoder for feature extraction
    encoder_model = tf.keras.models.Model(inputs=input_layer, outputs=encoder)
    X_train_encoded = encoder_model.predict(X_train)
    X_test_encoded = encoder_model.predict(X_test)

    # Build a separate model for stock price prediction
    prediction_model = tf.keras.models.Sequential()
    prediction_model.add(tf.keras.layers.Dense(64, activation='relu', input_dim=encoding_dim))
    prediction_model.add(tf.keras.layers.Dense(1))

    # Compile and train the prediction model
    prediction_model.compile(optimizer='adam', loss='mse')
    prediction_model.fit(X_train_encoded, y_train, epochs=100, batch_size=32, validation_data=(X_test_encoded, y_test))

    # Make predictions
    y_pred_train = prediction_model.predict(X_train_encoded)
    y_pred_test = prediction_model.predict(X_test_encoded)

    # Evaluate the model
    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test, y_pred_test)
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)

    print('Train Mean Squared Error:', mse_train)
    print('Test Mean Squared Error:', mse_test)
    print('Train R-squared:', r2_train)
    print('Test R-squared:', r2_test)

