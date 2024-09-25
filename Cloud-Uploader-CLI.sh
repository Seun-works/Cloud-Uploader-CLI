#! /bin/bash

# Use the special commands to take into account of the passed arguments to the script
# For examople calling ./Cloud-Uploader-CLI.sh /home/fileToUpload.txt/ s3://public-bucket
FILENAME=${1%/}
S3_BUCKET=${2%/}



FILENAME="${FILENAME}"
S3_BUCKET="s3://${S3_BUCKET}"/

# Check if the file actually exists in the directory
if [[ ! -f "$FILENAME" ]]; then
    echo "$FILENAME"
    echo "The current file path does not exist, please make sure the file is created before attempting to upload to the cloud"
    exit 1
fi

# Add verification for s3 bucket name

# if [[ "$bucketName" != "$S3_BUCKET" ]]; then
#     echo "$bucketName"
#     echo "An S3 bucket has to be passed for this to work"
#     exit 1
# fi

# Add file sync for better use

# Add progress bar for loading 

response="$(aws s3 cp "$FILENAME" "$S3_BUCKET")"

if [[ $? -eq 0 ]]; then
    echo "Success: $response"
else
    echo "Error: $response"
fi