import pandas as pd

def process_data(file_path):
    data = pd.read_csv(file_path)
    # Clean and preprocess data here
    data.dropna(inplace=True)
    # Feature engineering (e.g., calculate growth rates)
    return data