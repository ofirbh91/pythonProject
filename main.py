import  create_bucket
import boto3
import S3Operations
import AllObjOperations
import CreateFile
s3_resource = boto3.resource('s3')
bucket_name1 = "luai-the-king"
bucket_name2 = "ofirbh1"
s3 = create_bucket
s3_client = boto3.client('s3')
# S3Operations.copy_from_s3_to_s3('first.txt', bucket_name1, bucket_name2)
# S3Operations.create_bucket(bucket_name2, "eu-west-1")
# CreateFile.create_temp_file("third.txt", "harry potter")
# S3Operations.download_file("seconed.txt", bucket_name1)
# S3Operations.delete_file_from_s3("copy-first.txt", bucket_name2)
# S3Operations.change_obj_acl(bucket_name1, "seconed.txt", "private")
# S3Operations.upload_file("third.txt", bucket_name1,"", "AES256")
# S3Operations.upload_file_using_client("seconed.txt", bucket_name1, "","", "")
# S3Operations.enable_bucket_versioning(bucket_name1)
# s3_resource.Object(bucket_name1, "seconed.txt").upload_file("third.txt")
#S3Operations.get_bucket_list()
# AllObjOperations.get_bucket_obj(bucket_name1)
# AllObjOperations.delete_all_obj_in_bucket(bucket_name2)
# AllObjOperations.get_bucket_obj(bucket_name1)
# S3Operations.upload_file_using_client("first.txt", bucket_name1,"","","")
# S3Operations.upload_file_using_client("seconed.txt", bucket_name1,"","","")
# S3Operations.upload_file_using_client("third.txt", bucket_name1,"","","")
# AllObjOperations.get_bucket_obj(bucket_name1)
#AllObjOperations.get_bucket_obj(bucket_name2)