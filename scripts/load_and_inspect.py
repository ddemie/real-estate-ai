import pandas as pd

# Load the data
file_path = "../data/raw_data/COMREPUSQ159N.csv"
data = pd.read_csv(file_path)

# Inspect the data
print("First few rows of the dataset:")
print(data.head())

print("\nData Info:")
print(data.info())

print("\nColumn names:", data.columns)  # Print column names to confirm

print("\nSummary Statistics:")
print(data.describe())

# Convert DATE to datetime
data['DATE'] = pd.to_datetime(data['DATE'])

# Calculate the moving average for the 'COMREPUSQ159N' column
data['Moving_Avg'] = data['COMREPUSQ159N'].rolling(window=4).mean()

# Print the processed data to verify
print("\nProcessed Data:")
print(data.head())

processed_file_path = "../data/processed_data/processed_COMREPUSQ159N.csv"
data.to_csv(processed_file_path, index=False)
print(f"Processed data saved to {processed_file_path}")