import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import (
    Dense,
    Dropout,
    LayerNormalization,
    MultiHeadAttention,
    TimeDistributed,
)
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


# Load the stock price data
data = pd.read_csv('Dataset\Resultant Dataset\\ticker_csvs\AARTIDRUGS.csv')

# Extract the relevant features
features = data[['Open', 'High', 'Low', 'Close', 'Volume']].values

# Normalize the feature data
scaler = MinMaxScaler()
normalized_features = scaler.fit_transform(features)

# Define the temporal embedding function
def temporal_embedding(data):
    return np.concatenate([np.sin(data), np.cos(data)], axis=-1)

# Convert the sequential data into fixed-size representations
embedded_features = temporal_embedding(normalized_features)

# Split the data into training and testing sets
train_size = int(0.8 * len(embedded_features))
train_data = embedded_features[:train_size]
test_data = embedded_features[train_size:]

# Define the Transformer model
class TransformerModel(Model):
    def __init__(self, d_model, num_heads, num_layers, dropout_rate):
        super(TransformerModel, self).__init__()
        self.encoder_stack = [
            MultiHeadAttention(d_model=d_model, num_heads=num_heads),
            Dropout(dropout_rate),
            LayerNormalization(epsilon=1e-6),
        ]
        self.decoder_stack = [
            MultiHeadAttention(d_model=d_model, num_heads=num_heads),
            Dropout(dropout_rate),
            LayerNormalization(epsilon=1e-6),
            TimeDistributed(Dense(units=d_model, activation='relu')),
            Dropout(dropout_rate),
            LayerNormalization(epsilon=1e-6),
        ]
        self.final_layer = Dense(1)
    
    def call(self, inputs, training=True):
        x = inputs
        for layer in self.encoder_stack:
            x = layer(x, x, x, training=training)
        for layer in self.decoder_stack:
            x = layer(x, x, x, training=training)
        output = self.final_layer(x)
        return output

# Set hyperparameters
d_model = 128
num_heads = 4
num_layers = 2
dropout_rate = 0.2
learning_rate = 0.001
num_epochs = 100
batch_size = 32

# Create an instance of the Transformer model
model = TransformerModel(d_model, num_heads, num_layers, dropout_rate)

# Define the loss function and optimizer
loss_function = tf.keras.losses.MeanSquaredError()
optimizer = Adam(learning_rate)

# Prepare the data for training
train_dataset = tf.data.Dataset.from_tensor_slices(train_data)
train_dataset = train_dataset.batch(batch_size)

# Training loop
for epoch in range(num_epochs):
    for batch in train_dataset:
        with tf.GradientTape() as tape:
            predictions = model(batch[:, :-1, :], training=True)
            loss = loss_function(batch[:, 1:, :], predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.numpy():.4f}')

# Make predictions on the test data
test_predictions = model(test_data[:, :-1, :], training=False)

# Denormalize the predictions
denormalized_predictions = scaler.inverse_transform(test_predictions.numpy().reshape(-1, 1))

# Print the denormalized predictions
print(denormalized_predictions)
