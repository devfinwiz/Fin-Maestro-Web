'''
The models are trained using k-fold cross-validation to account for model performance variation across different folds. 
The ensemble prediction is obtained by averaging the predictions of all individual models across all folds.
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error

# Load the stock price data
data = pd.read_csv('stock_prices.csv')

# Feature engineering
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day
data['Weekday'] = data['Date'].dt.weekday
features = data[['Open', 'High', 'Low', 'Close', 'Volume', 'Month', 'Day', 'Weekday']].values
target = data['Price'].values

# Normalize the feature data
scaler = MinMaxScaler()
normalized_features = scaler.fit_transform(features)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(normalized_features, target, test_size=0.2, random_state=42)

# Define the individual models
model1 = RandomForestRegressor(n_estimators=100, random_state=42)
model2 = GradientBoostingRegressor(n_estimators=100, random_state=42)
model3 = XGBRegressor(n_estimators=100, random_state=42)
model4 = LGBMRegressor(n_estimators=100, random_state=42)

# Train the individual models using k-fold cross-validation
k = 5  # Number of folds
kf = KFold(n_splits=k, random_state=42, shuffle=True)
ensemble_preds = np.zeros_like(y_test)

for train_index, val_index in kf.split(X_train):
    X_train_fold, X_val_fold = X_train[train_index], X_train[val_index]
    y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]
    
    model1.fit(X_train_fold, y_train_fold)
    model2.fit(X_train_fold, y_train_fold)
    model3.fit(X_train_fold, y_train_fold)
    model4.fit(X_train_fold, y_train_fold)
    
    fold_preds = (model1.predict(X_val_fold) + model2.predict(X_val_fold) +
                  model3.predict(X_val_fold) + model4.predict(X_val_fold)) / 4
    ensemble_preds += (model1.predict(X_test) + model2.predict(X_test) +
                       model3.predict(X_test) + model4.predict(X_test)) / (4 * k)
    
    fold_rmse = np.sqrt(mean_squared_error(y_val_fold, fold_preds))
    print(f'Fold RMSE: {fold_rmse}')

# Ensemble evaluation
ensemble_rmse = np.sqrt(mean_squared_error(y_test, ensemble_preds))
print(f'Ensemble RMSE: {ensemble_rmse}')
