import pandas as pd
from google.cloud import bigquery

def load_to_bigquery():
    client = bigquery.Client()
    table_id = 'your-project.your_dataset.nyc_taxi'
    df = pd.read_csv('data/nyc_taxi.csv')
    job = client.load_table_from_dataframe(df, table_id)
    job.result()
    print('Data loaded to BigQuery successfully')

if __name__ == '__main__':
    load_to_bigquery()