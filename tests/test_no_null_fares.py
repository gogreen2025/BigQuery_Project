import pandas as pd

def test_no_null_fares():
    df = pd.read_csv('data/nyc_taxi.csv')
    assert df['fare_amount'].notnull().all(), 'Null fares found'