"""
Problem statement:
    Python S3 Get Contents
    In the Python file, write a program to access the contents of the bucket coderbytechallengesandbox.
    In there might be multiple files, but your program should find the file with the prefix __cb__,
    and then output the contents of that file. You should use the boto3 module to solve this challenge.
    You do not need any access keys to access the bucket because it is public.
    This post might help you with how to access the bucket.
    Example Output
    contents of some file

"""


import boto3


def get_s3_object(bucket_name, prefix):
    import boto3
    from botocore import UNSIGNED
    from botocore.client import Config

    s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    if 'Contents' in response:
        file_key = response['Contents'][0]['Key']

        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        file_contents = response['Body'].read().decode('utf-8')

        return file_contents

    return None


if __name__ == "__main__":
    bucket_name = "coderbytechallengesandbox"
    prefix = "__cb__"

    if file_contents := get_s3_object(bucket_name, prefix):
        print("Contents of the file:")
        print(file_contents)
    else:
        print("No file found with the specified prefix.")
