import os
import boto3

AWS_ENDPOINT = os.getenv("AWS_ENDPOINT", "http://localhost:4566")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET = os.getenv("S3_BUCKET_FILES", "files-bucket")

s3 = boto3.client("s3", endpoint_url=AWS_ENDPOINT, region_name=AWS_REGION)

def upload_to_s3(key: str, content: bytes, content_type: str):
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=content, ContentType=content_type)

def delete_from_s3(key: str):
    s3.delete_object(Bucket=S3_BUCKET, Key=key)

def list_s3():
    resp = s3.list_objects_v2(Bucket=S3_BUCKET)
    items = []
    for c in resp.get("Contents", []):
        items.append({"file_name": c["Key"], "uploaded_at": c["LastModified"].isoformat()})
    return items
