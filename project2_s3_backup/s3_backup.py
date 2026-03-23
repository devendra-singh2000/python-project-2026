import boto3
import os

s3 = boto3.client('s3')

BUCKET_NAME = "your-bucket-name"
FOLDER_PATH = "./data"

for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    if os.path.isfile(file_path):
        print(f"Uploading {file}...")
        s3.upload_file(file_path, BUCKET_NAME, file)

print("Backup completed!")