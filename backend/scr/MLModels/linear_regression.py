import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_linear_regression_model(data_file, feature_columns, target_column, test_size=0.2, random_state=42):
    # Step 1: Import the necessary libraries
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    
    # Step 2: Load the dataset
    df = pd.read_csv(data_file)
    
    # Step 3: Preprocess the data
    X = df[feature_columns]
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Step 4: Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 5: Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print('Mean Squared Error:', mse)
    print('R-squared:', r2)

    # Step 6: Make predictions
    new_data = pd.DataFrame([[81, 79.15, 79.6, 10034667]], columns=feature_columns)
    predicted_price = model.predict(new_data)
    print('Predicted Stock Price:', predicted_price)
