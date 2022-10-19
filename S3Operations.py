import boto3
import pathlib
import os

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

def upload_file_using_client(file_name, bucketname, acl_args, enc_args, storage_class):
    try:
        f = file_name
        s3 = boto3.client("s3")
        bucket_name = bucketname
        object_name = file_name
        file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), file_name)
        if(storage_class != ""):
            s3.upload_file(file_name, bucket_name, object_name, ExtraArgs={
                'ACL': acl_args, 'StorageClass': storage_class
            })
            print(f"File {f} has been uploaded with {storage_class} storage class")
            return
        if (enc_args == "yes"):
            s3.upload_file(file_name, bucket_name, object_name, ExtraArgs={
                'ACL': acl_args, 'ServerSideEncryption': 'AES256'
            })
            print(f"File {f} has been uploaded with AES256 encryption")
            return
        else:
            s3.upload_file(file_name, bucket_name, object_name, ExtraArgs={
                'ACL': acl_args
            })
            if (acl_args != ""):
                print(f"File {f} has been uploaded with {acl_args} privilege")
                return
            else:
                print(f"File {f} has been uploaded")
                return
    except:
        print("Operation file upload has been faild")

def download_file(file_name , bucket_name):
    try:
        s3_resource.meta.client.download_file(bucket_name, file_name, rf'C:/Users/ofirb/PycharmProjects/pythonProject2/{file_name}')
        print(f"File {file_name} has been download")
    except:
        print("Download has been faild")

def copy_from_s3_to_s3(file_name, source_bucket_name, dest_bucket_name):
    try:
        copy_source = {
            'Bucket': source_bucket_name,
            'Key': file_name
     }
        s3_resource.meta.client.copy(copy_source, dest_bucket_name, f'copy-{file_name}')
        print(f"{file_name} has been copy from {source_bucket_name} to {dest_bucket_name}")
    except:
        print("Operation copy has been faild")
def create_bucket(bucket_name, region=None):
    if region is None:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
    else:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint':region}
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration=location)

def get_bucket_list():
    response = s3_client.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f' {bucket["Name"]}')

def delete_file_from_s3(file_name, bucket_name):
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=file_name )
        print(f"The file {file_name} has been deleted successfully from bucket {bucket_name}")
    except:
        print("Operation delete has been faild")

def change_obj_acl(bucket_name, file_name, my_acl):
    s3_resource.Object(bucket_name, file_name).put(ACL=my_acl)
    print(f"File {file_name} ACL changed to {my_acl}")

def enable_bucket_versioning(bucket_name):
    bkt_versioning = s3_resource.BucketVersioning(bucket_name)
    bkt_versioning.enable()
    print(bkt_versioning.status)