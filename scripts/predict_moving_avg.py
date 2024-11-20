import pandas as pd

# Load your processed dataset
file_path = "../data/processed_data/fetched_COMREPUSQ159N_with_moving_avg.csv"
data = pd.read_csv(file_path)

# Take recent data or data without a Moving_Avg
recent_data = data[['COMREPUSQ159N']].tail(5)  # Take the last 5 rows

# Use this as new data
print("Recent Data:")
print(recent_data)