import os
from google.cloud import storage
import mysql.connector
from google.auth import exceptions
import json

# Replace these variables with your information
PROJECT_ID = "doctolib-data-dev"
BUCKET_NAME = "doctolib-data-dev-doctolib-storage-data"
CLOUD_SQL_HOST = "10.39.0.3"  # Your Cloud SQL private IP
CLOUD_SQL_DB_NAME = "api_database"
CLOUD_SQL_USER = "api"
CLOUD_SQL_PASSWORD = "api"
TABLE_NAME = "products"

# Set environment variable for authentication (use service account JSON key)
def list_files_in_bucket():
    """List all files in a GCS bucket"""
    client = storage.Client(project=PROJECT_ID)
    bucket = client.get_bucket(BUCKET_NAME)
    blobs = bucket.list_blobs()
    return blobs

def upload_and_load_file(blob):
    """Upload a file to GCS and load it into Cloud SQL"""
    # Extract the file name (blob name) from the GCS object
    file_name = blob.name
    
    # Load data into Cloud SQL
    try:
        # Connect to Cloud SQL MySQL database
        connection = mysql.connector.connect(
            host=CLOUD_SQL_HOST,
            user=CLOUD_SQL_USER,
            password=CLOUD_SQL_PASSWORD,
            database=CLOUD_SQL_DB_NAME
        )
        cursor = connection.cursor()

        # Assuming CSV format for loading data into Cloud SQL
        load_data_query = f"""
            LOAD DATA INFILE 'gs://{BUCKET_NAME}/{file_name}'
            INTO TABLE {TABLE_NAME}
            FIELDS TERMINATED BY ',' 
            ENCLOSED BY '"'
            LINES TERMINATED BY '\\n'
            IGNORE 1 ROWS;  -- Optional: Ignore the header row
        """
        cursor.execute(load_data_query)
        connection.commit()
        print(f"Data from {file_name} loaded into Cloud SQL successfully.")

    except mysql.connector.Error as err:
        print(f"Error while loading data from {file_name}: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def process_all_files():
    """Process all files in the GCS bucket"""
    # List all files in the bucket
    blobs = list_files_in_bucket()
    
    # Loop through each file in the bucket
    for blob in blobs:
        print(f"Processing file: {blob.name}")
        upload_and_load_file(blob)

def main():
    process_all_files()

if __name__ == "__main__":
    main()