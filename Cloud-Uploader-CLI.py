#! /usr/bin/python3

import os.path
import sys

filename=sys.argv[1]
s3Bucket=sys.argv[2]

s3Bucket=f"s3://{s3Bucket}/"

# Check if the file actually exists in the directory
if os.path.isfile(filename) != True:
    print("The current file path does not exist, please make sure the file is created before attempting to upload to the cloud")
    exit(1)

# Add verification for s3 bucket name


