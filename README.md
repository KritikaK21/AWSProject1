# 📂 File Processing System using LocalStack 🚀

Welcome to the **File Processing System**! This project **automatically processes CSV files**, extracts metadata, and stores it in **AWS-like services** using **LocalStack**. It mimics real-world **cloud-based file processing** without incurring AWS costs. 🏗️☁️



## 🎯 **Project Overview**
### 🔹 **What This Project Does:**
- ✅ **Uploads** CSV files to an **S3 bucket** (LocalStack S3)
- ✅ **Extracts metadata** (row count, column count, column names, file size, timestamp)
- ✅ **Stores metadata** in **DynamoDB** (LocalStack DynamoDB)
- ✅ **Uses LocalStack to simulate AWS services locally**
- ✅ **Ensures a smooth pipeline from upload ➝ processing ➝ storage**



## ⚙️ **Tech Stack & Tools Used**
| Technology    | Purpose |
|--------------|---------|
| **Python** 🐍 | Core scripting language |
| **LocalStack** 🏗️ | AWS Cloud Emulator |
| **Boto3** 🔗 | AWS SDK for Python |
| **AWS S3 (LocalStack)** 📂 | Cloud storage for CSV files |
| **AWS Lambda (LocalStack)** ⚡ | Serverless file processing |
| **AWS DynamoDB (LocalStack)** 🗄️ | NoSQL database to store metadata |



## 🔧 **Setup Instructions**
### 📌 **Prerequisites:**
Make sure you have the following installed on your system:
- [Docker 🐳](https://www.docker.com/) (Ensure it's running ✅)
- [LocalStack 🏗️](https://localstack.cloud/) (AWS Cloud Emulator)
- Python (Recommended: **3.8+**)
- Pip for package management

### 🛠️ **Installation Steps:**
1️⃣ **Clone this repository:**
```
 git clone https://github.com/yourusername/FileProcessingSystem.git
 cd FileProcessingSystem
```

2️⃣ **Install required dependencies:**
```sh
pip install -r requirements.txt
```

3️⃣ **Start LocalStack in Docker mode:**
```sh
localstack start -d  # Runs in detached mode
```

4️⃣ **Verify LocalStack is running:**
```sh
localstack status
```
Expected Output:
```
Runtime status  | ✔ running (name: "localstack-main", IP: 172.17.0.2)
```



## 🚀 **How to Use**
### 🔹 **Step 1: Create an S3 Bucket**
```sh
awslocal s3 mb s3://file-processing-bucket
```

### 🔹 **Step 2: Upload a CSV File to S3**
```sh
awslocal s3 cp example.csv s3://file-processing-bucket/
```

### 🔹 **Step 3: Verify File Upload**
```sh
awslocal s3 ls s3://file-processing-bucket/
```

### 🔹 **Step 4: Extract Metadata & Store in DynamoDB**
```sh
python extract_metadata.py
```
Expected Output:
```json
{
  "filename": "example.csv",
  "upload_timestamp": "2025-03-09 12:00:16",
  "file_size_bytes": 118,
  "row_count": 3,
  "column_count": 5,
  "column_names": "['id', 'name', 'age', 'city', 'date']"
}
```

### 🔹 **Step 5: Verify Metadata is Stored in DynamoDB**
```sh
awslocal dynamodb scan --table-name FileMetadata
```
Expected Output:
```json
{
  "Items": [
    {
      "filename": { "S": "example.csv" },
      "upload_timestamp": { "S": "2025-03-09 12:00:16" },
      "file_size_bytes": { "N": "118" },
      "row_count": { "N": "3" },
      "column_count": { "N": "5" },
      "column_names": { "S": "['id', 'name', 'age', 'city', 'date']" }
    }
  ]
}
```



## 🛠️ **Troubleshooting & Common Issues**
### ❌ **LocalStack is not running?**
Run:
```sh
localstack start -d
```

### ❌ **Error: Could not connect to endpoint URL `http://localhost:4566/`?**
Check if Docker is running and restart LocalStack:
```sh
docker ps  # Ensure LocalStack container is running
localstack stop && localstack start -d
```

### ❌ **FileNotFoundError: `example.csv` not found?**
Make sure your file exists in `C:\Users\Hello\` and update your script with the correct file path.




## 📌 **Future Enhancements**
✅ Add an **AWS Lambda trigger** for automatic processing
✅ Implement **error handling & logging**
✅ Store metadata in **AWS RDS (PostgreSQL/MySQL)**



## 🎉 **Final Thoughts**
This project **simulates real AWS cloud operations** locally, making it cost-effective & developer-friendly! 🚀 If you have any suggestions or improvements, feel free to contribute! 😊



🔗 **GitHub Repository:** https://github.com/KritikaK21/AWSProject1
💬 **Need help?** Open an issue or contact me!







