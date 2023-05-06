# Step 1: Import the necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load the dataset
df = pd.read_csv('Dataset\Resultant Dataset\\ticker_csvs\ZOMATO.csv')

# Step 3: Preprocess the data
X = df[['Open', 'High', 'Low', 'Volume']]  # Select features
y = df['Close']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the random forest regressor
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Mean Squared Error:', mse)
print('R-squared:', r2)

# Step 6: Make predictions
new_data = pd.DataFrame([[89.5,89.5,86.4,10384667]], columns=['Open', 'High', 'Low', 'Volume'])
predicted_price = model.predict(new_data)
print('Predicted Stock Price:', predicted_price)
