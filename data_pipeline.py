import pandas as pd
import os
from glob import glob

# Path to folder containing CSV files
folder_path = r"data\raw"  # change to your folder path

# Get list of all CSV files in the folder
csv_files = glob(os.path.join(folder_path, "*.csv"))

# List to hold individual DataFrames
dfs = []

for file in csv_files:
    try:
        # Read each CSV safely
        temp_df = pd.read_csv(
            file,
            encoding='latin-1',  # handles special characters
            sep=',',             # change to ';' if needed
            engine='python'
        )
        # Clean column names
        temp_df.columns = temp_df.columns.str.strip()
        
        # Append to list
        dfs.append(temp_df)
        
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Merge all DataFrames into one
merged_df = pd.concat(dfs, ignore_index=True)

# Show all columns
pd.set_option('display.max_columns', None)

# Display first 5 rows
print(merged_df.head())

# Save merged DataFrame as a separate CSV file
output_file = r"data\raw\merged_file.csv"  # change path if needed
merged_df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Merged file saved as: {output_file}")
