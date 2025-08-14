# BigQuery ETL Pipeline

This is a sample ETL pipeline that loads taxi trip data into BigQuery, applies SQL transformations, and runs automated tests.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set up Google Cloud credentials and export `GOOGLE_APPLICATION_CREDENTIALS`
3. Run ETL: `python etl.py`
4. Tests will run automatically via GitHub Actions.
