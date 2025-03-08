import pandas as pd
import json

RAW_DATA_FILE = "raw_conversions.json"
PROCESSED_FILE = "tapfiliate_conversions.parquet"

def transform_data():
    try:
        with open(RAW_DATA_FILE, "r") as f:
            conversions_data = json.load(f)
        
        if not conversions_data:
            print("No data found in extracted file.")
            return

        df = pd.DataFrame(conversions_data)

        # Drop unnecessary columns
        df.drop(columns=['meta_data'], errors='ignore', inplace=True)

        # Save processed data as Parquet
        df.to_parquet(PROCESSED_FILE, index=False, engine='pyarrow')
        print(f"Transformed data saved to {PROCESSED_FILE}")

    except Exception as e:
        print(f"Error transforming data: {e}")

if __name__ == "__main__":
    transform_data()

