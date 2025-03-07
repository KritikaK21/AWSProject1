import boto3

# Connect to LocalStack S3
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",  # LocalStack S3 URL
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

# Bucket name
bucket_name = "my-localstack-bucket"

# Create an S3 bucket in LocalStack
s3.create_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' created successfully!")

# Upload a sample file
file_name = "example.csv"
s3.upload_file(file_name, bucket_name, file_name)
print(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'.")

# List objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
if "Contents" in response:
    for obj in response["Contents"]:
        print(f"Found file: {obj['Key']}")
else:
    print("No files found in bucket.")
