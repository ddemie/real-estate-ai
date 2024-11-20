import requests
import pandas as pd

# Fetch data for COMREPUSQ159N from FRED API
api_key = "159992a2a81a3096e600ff161463392c"  # Replace with your API key
url = f"https://api.stlouisfed.org/fred/series/observations?series_id=COMREPUSQ159N&api_key={api_key}&file_type=json"

response = requests.get(url)
data = response.json()

# Convert to DataFrame
observations = data['observations']
new_data = pd.DataFrame(observations)

# Keep the relevant columns: DATE and COMREPUSQ159N
new_data = new_data[['date', 'value']].rename(columns={'date': 'DATE', 'value': 'COMREPUSQ159N'})
new_data['COMREPUSQ159N'] = pd.to_numeric(new_data['COMREPUSQ159N'])
new_data['DATE'] = pd.to_datetime(new_data['DATE'])

# Calculate the moving average with a rolling window of 4
new_data['Moving_Avg'] = new_data['COMREPUSQ159N'].rolling(window=4).mean()

# Save the data to a CSV file
output_path = "../data/processed_data/fetched_COMREPUSQ159N_with_moving_avg.csv"
new_data.to_csv(output_path, index=False)
print(f"Data saved to {output_path}")