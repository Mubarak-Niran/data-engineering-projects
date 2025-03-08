# ETL Pipeline - BigQuery

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python, pulling data from a public API, transforming it, and loading it into Google BigQuery.

## Technologies
- Python
- Google Cloud Platform (BigQuery)
- Pandas

## Workflow
1. Extract data from a public API.
2. Clean and transform the data using Pandas.
3. Load the cleaned data into a BigQuery table.

## Files
- `extract.py`: Handles data extraction.
- `transform.py`: Handles data cleaning and transformation.
- `load.py`: Uploads data to BigQuery.

## Setup
- Create a service account key and set up your `GOOGLE_APPLICATION_CREDENTIALS`.
- Install dependencies using `pip install -r requirements.txt`.
