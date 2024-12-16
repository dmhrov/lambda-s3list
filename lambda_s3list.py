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
