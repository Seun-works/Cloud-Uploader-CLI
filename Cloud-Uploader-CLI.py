#! /usr/bin/python3

import os.path
import sys
import boto3

filePath = sys.argv[1]
s3 = boto3.resource('s3')
userBucket = sys.argv[2]
userS3BucketPath = f"s3://{sys.argv[2]}/"

# Check if the file actually exists in the directory
if os.path.isfile(filePath) != True:
    print("The current file path does not exist, please make sure the file is created before attempting to upload to the cloud")
    exit(1)

# Add verification for s3 bucket name
awsBuckets = s3.buckets.all()
for bucket in awsBuckets:
    if userBucket == bucket.name:
        print('Your bucket is definitely there')
        break
    else:
        print("A new bucket will be created for you")

fileName = os.path.basename(filePath)
# Upload file to s3 bucket
with open(f'{filePath}', 'rb') as data:
        s3.Bucket(userBucket).put_object(Key=f"{fileName}", Body=data)
        print("The file was successfully uploaded")

