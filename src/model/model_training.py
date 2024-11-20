import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load the data
file_path = "../data/processed_data/processed_COMREPUSQ159N.csv"
data = pd.read_csv(file_path)

# Drop rows with NaN in 'Moving_Avg'
data = data.dropna(subset=['Moving_Avg'])

# Features and target
X = data[['COMREPUSQ159N']]  # Use the COMREPUSQ159N column as the feature
y = data['Moving_Avg']  # Target is Moving_Avg

# Train-test split (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Model Performance:")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Test on some new data (optional)
print("\nSample Predictions:")
print("Actual:", y_test.values[:5])
print("Predicted:", y_pred[:5])