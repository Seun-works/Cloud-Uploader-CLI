# Cloud Uploader CLI

## Overview

`Cloud-Uploader-CLI.py` is a Python-based command-line interface (CLI) tool for uploading files to an Amazon S3 bucket. It verifies the existence of the specified file and ensures the specified S3 bucket is accessible before attempting the upload. This tool can be helpful for users looking to quickly upload files to S3 from the command line.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **AWS CLI and boto3**: Install and configure AWS CLI with the required IAM permissions, and make sure to install the `boto3` library to allow Python to interact with AWS services.

  ```bash
  pip install boto3
  ```

- **AWS Credentials**: Ensure that your AWS credentials are configured in `~/.aws/credentials` or set up through environment variables.

## Setup

### Installation

1. Clone or download the script to your local machine.
2. Place it in a directory accessible by your command line or add the directory to your PATH for easy access.

### Permissions

Ensure that the AWS IAM role associated with your credentials has permissions for:
- `s3:PutObject` for uploading files to the specified bucket
- `s3:ListBucket` for verifying the existence of the bucket

## Usage

Run the script from the command line with the following syntax:

```bash
python Cloud-Uploader-CLI.py <file_path> <bucket_name>
```

### Arguments
- `<file_path>`: Local path of the file to be uploaded.
- `<bucket_name>`: Name of the target S3 bucket.

### Example

```bash
python Cloud-Uploader-CLI.py /path/to/myfile.txt my-s3-bucket
```

### Workflow

1. **File Verification**: Checks if the specified file exists locally.
2. **Bucket Verification**: Ensures the specified S3 bucket exists.
3. **Upload Process**: Uploads the file to the S3 bucket if all checks pass.

## Error Handling

- **File Not Found**: If the file does not exist, the script will display an error message and terminate.
- **Bucket Not Found**: If the bucket is not accessible, an error message will be displayed, and the script will terminate.

## Troubleshooting

- **Permission Issues**: Verify your IAM role and permissions.
- **Invalid File Path**: Ensure the file path is correct and accessible from the current directory.

## Contributing

Feel free to open issues or submit pull requests to improve this tool.

---

This README provides an overview, setup instructions, usage guidance, and troubleshooting tips for using the `Cloud-Uploader-CLI.py` script. Let me know if there are specific details you'd like added or modified!
