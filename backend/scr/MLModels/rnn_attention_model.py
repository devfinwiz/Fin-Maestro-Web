import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, LearningRateScheduler
import matplotlib.pyplot as plt

# Load and preprocess the data
data = pd.read_csv('stock_prices.csv')  # Replace 'stock_prices.csv' with your own dataset
data = data['Close'].values  # Assuming the 'Close' column contains the target variable
data = data.reshape(-1, 1)  # Reshape to a 2D array

# Split the data into train and test sets
train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
train_data = scaler.fit_transform(train_data)
test_data = scaler.transform(test_data)

# Prepare the data for training
def prepare_data(data, time_steps):
    X, y = [], []
    for i in range(len(data) - time_steps - 1):
        X.append(data[i : (i + time_steps)])
        y.append(data[i + time_steps])
    return np.array(X), np.array(y)

time_steps = 10  # Number of previous time steps to consider for prediction
X_train, y_train = prepare_data(train_data, time_steps)
X_test, y_test = prepare_data(test_data, time_steps)

# Build the RNN-Attention model
inputs = tf.keras.Input(shape=(time_steps, 1))
gru = layers.GRU(64, return_sequences=True)(inputs)
attention = layers.Attention()(gru)
output = layers.Dense(1)(attention)
model = tf.keras.Model(inputs=inputs, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Define callbacks
checkpoint = ModelCheckpoint("model_checkpoint.h5", save_best_only=True, save_weights_only=True, verbose=1)
early_stopping = EarlyStopping(patience=10, restore_best_weights=True)
lr_scheduler = LearningRateScheduler(lambda epoch: 0.001 if epoch < 10 else 0.0001)

# Train the model
history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=32,
    validation_data=(X_test, y_test),
    callbacks=[checkpoint, early_stopping, lr_scheduler]
)

# Evaluate the model
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Denormalize the predictions
train_predictions = scaler.inverse_transform(train_predictions)
y_train = scaler.inverse_transform(y_train)
test_predictions = scaler.inverse_transform(test_predictions)
y_test = scaler.inverse_transform(y_test)

# Plot the predictions
plt.plot(y_train, label='Actual Train')
plt.plot(train_predictions, label='Predicted Train')
plt.plot(len(y_train) + np.arange(len(y_test)), y_test, label='Actual Test')
plt.plot(len(y_train) + np.arange(len(test_predictions)), test_predictions, label='Predicted Test')
plt.legend()
plt.show()
