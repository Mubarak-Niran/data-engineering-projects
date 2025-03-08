import os
from google.cloud import storage
from datetime import datetime

# GCS Configuration
BUCKET_NAME = "Data_Engineering_Project"
PROCESSED_FILE = "tapfiliate_conversions.parquet"

# Set up Google Cloud authentication
os.environ["GCLOUD_PROJECT"] = "Data_Engineering_Project"
# credential_path = 
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

# Generate timestamp-based destination path
current_time = datetime.now()
year, month, day = current_time.strftime("%Y"), current_time.strftime("%m"), current_time.strftime("%d")
timestamp = current_time.strftime("%Y%m%d_%H%M%S")
DESTINATION_BLOB_NAME = f"inbound/tapfiliate/conversions/{year}/{month}/{day}/tapfiliate_conversions_{timestamp}.parquet"

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to Google Cloud Storage with year/month/day folder structure."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {bucket_name}/{destination_blob_name}.")

        # Delete local file after upload
        if os.path.exists(source_file_name):
            os.remove(source_file_name)
            print(f"Local file {source_file_name} has been deleted.")
        else:
            print(f"Local file {source_file_name} not found.")

    except Exception as e:
        print(f"Error uploading file to GCS: {e}")

if __name__ == "__main__":
    upload_to_gcs(BUCKET_NAME, PROCESSED_FILE, DESTINATION_BLOB_NAME)
