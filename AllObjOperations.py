import boto3
import pathlib
import os
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

def get_bucket_obj(bucket_name):
    my_bucket = s3_resource.Bucket(bucket_name)
    print(f"All objects in {bucket_name} are: ")
    for file in my_bucket.objects.all():
        print(file.key)

def delete_all_obj_in_bucket(bucket_name):
    my_bucket = s3_resource.Bucket(bucket_name)
    my_bucket.objects.all().delete()
    print(f"All obj in {bucket_name} deleted")
