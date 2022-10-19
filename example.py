import boto3
import uuid

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def generate_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(BUCKET_NAME):
    YOUR_BUCKET_NAME = generate_bucket_name(BUCKET_NAME)
    print(f"Your bucket name is: {YOUR_BUCKET_NAME}")
    s3_resource_status = s3_resource.create_bucket(
        Bucket=YOUR_BUCKET_NAME,
        CreateBucketConfiguration=
            {'LocationConstraint': 'eu-west-1'}
    )
    return YOUR_BUCKET_NAME

def find_my_bucket(substr):
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        if substr in bucket.get('Name'):
            print(f"Bucket: {bucket['Name']}")
            print(f"All attributes: {bucket}")
            return bucket['Name']

def delete_bucket(bucket):
    try:
        response = s3_client.delete_bucket(
            Bucket=bucket
        )
        if response['ResponseMetadata']['HTTPStatusCode'] in [204, 200]:
            return True
    except Exception as e:
        print("Failed to delete bucket")

result_of_create_bucket = create_bucket("lidor-")
bucket_name = find_my_bucket("lidor-")
result = delete_bucket(bucket_name)
print(f"Delete bucket: {result}")
