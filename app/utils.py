import pandas as pd
from pathlib import Path
import os

def load_data(selected_countries):
    """
    Load and merge cleaned CSV files for selected countries.
    Returns:
        pd.DataFrame: Combined data with 'Country' column
    """
    # Get absolute path to data folder
    data_dir = Path(__file__).parent.parent / "data"
    
    # Validate data directory
    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory not found at: {data_dir}")

    dfs = []
    country_files = {
        "Benin": "benin_clean.csv",
        "Sierra Leone": "sierraleone_clean.csv",
        "Togo": "togo_clean.csv"
    }

    for country in selected_countries:
        file_path = data_dir / country_files[country]
        
        # Check if file exists
        if not file_path.exists():
            raise FileNotFoundError(f"Data file missing: {file_path}")
        
        # Load and add country tag
        df = pd.read_csv(file_path)
        df['Country'] = country  # Ensure Country column exists
        dfs.append(df)

    # Merge all data
    combined = pd.concat(dfs, ignore_index=True)
    
    # Validate required columns
    required_cols = ['Country', 'GHI', 'DNI', 'DHI']
    missing = [col for col in required_cols if col not in combined.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    return combined