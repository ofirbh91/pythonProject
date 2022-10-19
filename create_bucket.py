import boto3
import uuid

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def generate_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])



# def create_bucket(bucket_prefix, s3_connection):
#     session = boto3.session.Session()
#     current_region = session.region_name
#     bucket_name = generate_bucket_name(bucket_prefix)
#     bucket_response = s3_connection.create_bucket(
#         Bucket=bucket_name,
#         CreateBucketConfiguration={
#           'LocationConstraint': "eu-west-1"})
#     print(bucket_name, current_region)
#     return bucket_name, bucket_response

def create_bucket(bucket_name, region=None):
    if region is None:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
    else:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint':region}
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration=location)


