import pytest
import pandas as pd
from datetime import datetime

# Import prepare_data from your batch module
from batch import prepare_data  # adjust if your module is named differently

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)
    categorical = ['PULocationID', 'DOLocationID']

    result_df = prepare_data(df, categorical)

    # Check the number of rows after filtering
    assert len(result_df) == 2

    # Optional: Check if categorical columns are strings
    for col in categorical:
        assert result_df[col].dtype == 'object'

    # Optional: Check if duration column exists
    assert 'duration' in result_df.columns
