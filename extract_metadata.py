import pandas as pd
import os
import time

# File details
file_path = "example.csv"
file_size = os.path.getsize(file_path)  # File size in bytes
upload_timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

# Read CSV
df = pd.read_csv(file_path)

# Extract metadata
metadata = {
    "filename": os.path.basename(file_path),
    "upload_timestamp": upload_timestamp,
    "file_size_bytes": file_size,
    "row_count": len(df),
    "column_count": len(df.columns),
    "column_names": list(df.columns)
}

# Print metadata
print(metadata)
