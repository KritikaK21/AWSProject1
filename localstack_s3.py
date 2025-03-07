import boto3

# Define LocalStack S3 Endpoint
LOCALSTACK_ENDPOINT_URL = "http://localhost:4566"

# Create an S3 client pointing to LocalStack
s3 = boto3.client("s3", endpoint_url=LOCALSTACK_ENDPOINT_URL)

# Bucket name
BUCKET_NAME = "test-bucket"

# Step 1: Create an S3 bucket
def create_bucket():
    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
        print(f"✅ Bucket '{BUCKET_NAME}' created successfully!")
    except Exception as e:
        print(f"⚠️ Error creating bucket: {e}")

# Step 2: Upload a file to S3
def upload_file():
    file_name = "test.txt"  # Sample file to upload
    with open(file_name, "w") as f:
        f.write("Hello from LocalStack!")

    try:
        s3.upload_file(file_name, BUCKET_NAME, file_name)
        print(f"📂 File '{file_name}' uploaded to bucket '{BUCKET_NAME}'!")
    except Exception as e:
        print(f"⚠️ Error uploading file: {e}")

# Step 3: List files in the bucket
def list_files():
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if "Contents" in response:
            print("📜 Files in bucket:")
            for obj in response["Contents"]:
                print(f" - {obj['Key']}")
        else:
            print("📂 No files found in the bucket.")
    except Exception as e:
        print(f"⚠️ Error listing files: {e}")

# Step 4: Run the functions
if __name__ == "__main__":
    create_bucket()   # Create S3 bucket
    upload_file()     # Upload a file
    list_files()      # List uploaded files
