# Demonstrates uploading and downloading a file from S3 using boto3

import boto3

s3 = boto3.client('s3')
BUCKET = 'your-bucket'
KEY = 'demo-file.txt'

def upload_file():
    # Upload a file with sample content to the specified S3 bucket
    s3.put_object(Bucket=BUCKET, Key=KEY, Body="Hello from Cloud!")

def download_file():
    # Download the file from S3 and print its contents
    obj = s3.get_object(Bucket=BUCKET, Key=KEY)
    print(obj['Body'].read().decode())

if __name__ == '__main__':
    upload_file()
    download_file()