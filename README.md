
a) Create S3 bucket.

```
aws s3 mb s3://soloma-state --region eu-central-1
```

b) Upload any small file in it.

```
echo Hello | aws s3 cp - s3://soloma-state/test-s3list.txt
```

c) Read it from the lambda function (python3 runtime). Write Python code that list all files in s3 bucket.

```
import boto3, os

def lambda_handler(event, context):

    mys3 = boto3.client('s3')
    bucket_name = "soloma-state" # bucket name
    
    try:
        response = mys3.list_objects_v2(Bucket=bucket_name) # list all files in the bucket
        
        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
            return {
                'statusCode': 200,
                'body': f"Files in bucket {bucket_name}: {files}"
            }
        else:
            return {
                'statusCode': 200,
                'body': f"No files found in bucket {bucket_name}."
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }

```


When building the lambda function, the boto3 library helped with [S3.Client](https://boto3.amazonaws.com/v1/documentation/api/1.35.9/reference/services/s3.html ) , [llist_objects_v2](https://boto3.amazonaws.com/v1/documentation/api/1.35.9/reference/services/s3/client/list_objects_v2.html)
